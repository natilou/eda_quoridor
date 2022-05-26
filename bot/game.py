from constants import URL
from adapters.websocket_client import WebsocketClient
from strategies.move_advanced_pawn import MoveAdvancedPawn
from strategies.move_pawn_random import MovePawnRandom
from strategies.front_jump import FrontJump
from strategies.put_wall_random import PutWallRandom
from bot.strategies.block_nearby_pawn import BlockNearbyPawn
import asyncio
import websockets 
import json
import sentry_sdk
import os

if os.getenv("SENTRY_DSN"):
    sentry_sdk.init(
        traces_sample_rate=1.0
    )

# Conect to websocket
async def connect():
    while True:
        try:
            print(f"Connection to {URL}")
            async with websockets.connect(URL) as websocket:
                websocket_client = WebsocketClient(websocket)
                game = Game(websocket_client)
                await game.play()
        except Exception:
            print(f"Error: {str(Exception)}")
    

# Game logic 
class Game:
    def __init__(self, client):
        self.client = client

    # Start game
    async def play(self):
        while True:
            try:
                request = await self.client.receive_request()
                print(f"Request: {request}")
                
                request_data = json.loads(request)

                if request_data['event'] == 'challenge':
                    await self.client.send(
                        'accept_challenge', 
                        {
                            'challenge_id': request_data['data']['challenge_id'],
                        }
                    )
            
                elif request_data['event'] == 'your_turn':
                    await self.play_turn(request_data)

                else:
                    print(f"Unknown event: {request_data}")

            except Exception as exc:
                print(f"Error: {exc}")
                break 
    
   
    async def play_turn(self, request_data):

        # strategies initialization 
        block_nearby_pawn = BlockNearbyPawn()
        front_jump = FrontJump()
        move_advanced_pawn = MoveAdvancedPawn
        move_pawn_random = MovePawnRandom()
        put_wall_random = PutWallRandom()

        # assign chain of responsibility
        block_nearby_pawn.set_next(front_jump)
        front_jump.set_next(move_advanced_pawn)
        move_advanced_pawn.set_next(move_pawn_random)
        move_pawn_random.set_next(put_wall_random)
        
        move = await block_nearby_pawn.perform_an_action(request_data)
        await self.client.send_message(request_data, move)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(connect())
   
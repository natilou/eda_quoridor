from bot.constants import URL
from bot.adapters.websocket_client import WebsocketClient
from bot.strategies.move_pawn_random import MovePawnRandom
from bot.strategies.put_wall_random import PutWallRandom
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
        move_pawn_random = MovePawnRandom()
        put_wall_random = PutWallRandom()
        move_pawn_random.set_next(put_wall_random)

        move = await move_pawn_random.perform_an_action(request_data)
        await self.client.send_message(request_data, move)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(connect())
   
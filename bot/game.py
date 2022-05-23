import asyncio
import websockets 
import json
from constants import URL
from adapters.websocket_client import WebsocketClient
from strategies.move_pawn import MovePawn
from strategies.put_wall import PutWall
import sentry_sdk
import os

if os.getenv("SENTRY_DSN"):
    sentry_sdk.init()

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
        move_pawn = MovePawn()
        put_wall = PutWall()
        move_pawn.set_next(put_wall)

        message = await move_pawn.perform_an_action(request_data)
        self.check_score(request_data, message.expected_score)
        await self.client.send_message(request_data, message)
    
    def check_score(self, request_data, expected_score):
        email = os.getenv("email")
        last_score = request_data['data']['score_1'] if request_data['data']['score_1'] == email else request_data['data']['score_2']
        current_score = 0 # TODO: modificar lógica

        if (last_score + expected_score) != current_score: 
            print(f"Different score: current: {current_score}, expected: {last_score + expected_score}")

        



if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(connect())
   
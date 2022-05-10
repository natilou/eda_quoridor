from abc import ABC, abstractmethod
import asyncio
import websockets 
import os
import random
import json
import sys

# Constants

URL = f'wss://4yyity02md.execute-api.us-east-1.amazonaws.com/ws?token={os.getenv("token")}'


# conect to websocket
async def connect():
    print("connection to {}".format(URL))
    async with websockets.connect(URL) as websocket:
        print("connect")
        await begin(websocket)
        await asyncio.sleep(60*60) 


async def begin(websocket):
    request = await websocket.recv()
    request_data = json.loads(request)
    
    if request_data['event'] == 'challenge':
        dict = {
            'response': 'accept_challenge', 
            'challenge':  request_data['data']['challenge_id']
        }
    elif request_data['event'] == 'your_turn':
        await Game.choose_strategy(websocket, request_data)

    else:
        pass


class Game:
    def __init__(self, strategy): 
        self.strategy = strategy
    
    @property
    def strategy(self): 
        return self.strategy
    
    @strategy.setter
    def strategy(self, strategy): 
        self.strategy = strategy

    def choose_strategy(self, websocket, request_data) -> None:
        """
        The Context delegates some work to the Strategy object instead of
        implementing multiple versions of the algorithm on its own.
        """

        if random.randint(0,5) >= 3:
            self.strategy(MovePawn(request_data))
        else:
            self.strategy(PutWalls(request_data))


class Strategy(ABC):
    @abstractmethod
    def perform_an_action(self, data):
        pass

class MovePawn(Strategy):
    def perform_an_action(self, data):
        return "mover random"

class PutWalls(Strategy): 
    def perform_an_action(self, data):
        return "poner paredes random"

# class Board():
#     def __init__(self): 
#         self = self
    
#     def makeBoard():
#         print()
        



# class Locker():
#     def __init__(self):
#         self.is_taken = False

#     @property
#     def state(self):
#         return 

if __name__ == "__main__": 
    asyncio.get_event_loop().run_until_complete(connect())
from abc import ABC, abstractmethod
import asyncio
import websockets 
import os
import random
import json

# Constants
URL = f"wss://4yyity02md.execute-api.us-east-1.amazonaws.com/ws?token={os.getenv('auth_token')}"
VISUAL_BOARD_WIDTH_AND_HEIGHT = 17
PAWN_BOARD_WIDTH_AND_HEIGHT = 9


# Conect to websocket
async def connect():
    while True:
        try:
            print(f"Connection to {URL}")
            async with websockets.connect(URL) as websocket:
                await begin(websocket)
        except Exception:
            print(f"Error: {str(Exception)}")
    

# Start game
async def begin(websocket):
    while True:
        try:
            request = await websocket.recv()
            print(f"Request: {request}")
            
            request_data = json.loads(request)
            

            if request_data['event'] == 'challenge':
                await Messenger.send(
                    websocket, 
                    'accept_challenge', 
                    {
                        'challenge_id': request_data['data']['challenge_id'],
                    }
                )
        
            elif request_data['event'] == 'your_turn':
                await Game.choose_strategy(websocket, request_data)

            else:
                print(f"Unknown event: {request_data}")

        except Exception as exc:
            print(f"Error: {exc}")
            break


# Strategy interface
class Strategy(ABC):
    @abstractmethod
    async def perform_an_action(websocket, request_data):
        pass


# Concrete Strategy
class MovePawn(Strategy):
    @staticmethod
    async def perform_an_action(websocket, request_data):
        side_to_move = request_data['data']['side']

        # normalizar tablero
        board = Board.format_board(request_data)

        # falta agregar lógica para ver cuál de los 3 peones mover

        # ver dónde estoy
        for row in range(PAWN_BOARD_WIDTH_AND_HEIGHT):
            for col in range(PAWN_BOARD_WIDTH_AND_HEIGHT):
                if board[row][col] == side_to_move:
                    from_row = row
                    from_col = col
                    to_col = col
        
        # decidir row a moverse
        to_row = from_row + (1 if side_to_move == "N" else -1)

        # verificar que row a moverse esté vacia
        if board[to_row][from_col] != ' ':
            to_row = to_row + (1 if side_to_move == 'N' else -1)

        await Messenger.send(
            websocket, 
            'move', 
            {
                'game_id': request_data['data']['game_id'], 
                'turn_token': request_data['data']['turn_token'], 
                'from_row': from_row,
                'from_col': from_col,
                'to_row': to_row,
                'to_col': to_col,
            }
        )
                

# Concrete Strategy
class PutWall(Strategy): 
    @staticmethod
    async def perform_an_action(websocket, request_data):
        row = random.randint(0, 8)
        col = random.randint(0,8)
        orientation = random.choice(['h', 'v'])
        # FALTA VERIFICAR QUE ESAS COLUMNAS Y FILAS NO ESTEN OCUPADAS
        await Messenger.send(
            websocket, 
            'wall', 
            {
                'game_id': request_data['data']['game_id'],
                'turn_token': request_data['data']['turn_token'], 
                'row': row, 
                'col': col, 
                'orientation': orientation 
            }
        )


# Game logic 
class Game:
    def __init__(self, strategy): 
        self.strategy = strategy
    
    # @property     
    # def strategy(self): 
    #     return self.strategy
    
    # @strategy.setter
    # def strategy(self, strategy): 
    #     self.strategy = strategy

    async def choose_strategy(websocket, request_data):
        allowed_strategies = []

        if request_data['data']['walls'] > 0:
            allowed_strategies.append(PutWall)

        if request_data['data']['remaining_moves'] > 0:
            allowed_strategies.append(MovePawn)

        if not allowed_strategies:
            raise Exception("No allowed strategies found")
       
        selected_strategy = random.choice(allowed_strategies)
        await selected_strategy.perform_an_action(websocket, request_data)

class Board:
    def format_board(request_data):
        board_data = request_data['data']['board']
        pawn_board = []
        length_row = VISUAL_BOARD_WIDTH_AND_HEIGHT
        num_row = 0
        for row in range(9):
            board_data_row = [board_data[num_row : length_row]]
            pawn_board.append(board_data_row)
            num_row = length_row
            length_row += VISUAL_BOARD_WIDTH_AND_HEIGHT
        return pawn_board


# Send message to websocket
class Messenger:
    @staticmethod
    async def send(websocket, action, data):
        message = json.dumps(
            {
                'action': action, 
                'data': data
            }
        )
        print(f'Sending message: {message}')
        await websocket.send(message)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(connect())
   
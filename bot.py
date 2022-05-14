from abc import ABC, abstractmethod
import asyncio
from urllib import request
import websockets 
import os
import random
import json

# Constants
URL = f"wss://4yyity02md.execute-api.us-east-1.amazonaws.com/ws?token={os.getenv('auth_token')}"
VISUAL_BOARD_WIDTH_AND_HEIGHT = 17
SQUARE_DIMENSION = 9
SLOT_DIMENSION = 8

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
        side = request_data['data']['side']

        # normalizar tablero
        board = PawnBoard(request_data)

        # elegir uno de los tres peones:
        selected_pawn = random.choice(board.get_my_pawns(request_data))
        
        # ver dónde estoy
        pawn_actual_row = selected_pawn[0] 
        pawn_actual_col = selected_pawn[1]

        # ver dónde moverse
        move_to_col = ""
        move_to_row = ""
        direction_to_move = 1 if side == "N" else -1
        
        if board.get_cell(pawn_actual_row + direction_to_move, pawn_actual_col) == " ":
            move_to_row = pawn_actual_row + direction_to_move
            move_to_col = pawn_actual_col 
        
        elif board.get_cell(pawn_actual_row + direction_to_move, pawn_actual_col) != " ":
            move_to_row = pawn_actual_row + direction_to_move * 2
            move_to_col = pawn_actual_col         


        await Messenger.send(
            websocket, 
            'move', 
            {
                'game_id': request_data['data']['game_id'], 
                'turn_token': request_data['data']['turn_token'], 
                'from_row': pawn_actual_row,
                'from_col': pawn_actual_col,
                'to_row': move_to_row,
                'to_col': move_to_col,
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


class PawnBoard:
    def __init__(self, request_data):
        self.pawn_board = self.format_pawn_board(request_data)

    def format_pawn_board(self, request_data):
        board_data = request_data['data']['board']
        pawn_board = []
        length_row = VISUAL_BOARD_WIDTH_AND_HEIGHT
        num_row = 0

        for row in range(SQUARE_DIMENSION):
            board_data_row = board_data[num_row : length_row : 2]
            pawn_board.append(list(board_data_row))
            if row != SQUARE_DIMENSION - 1:
                num_row = length_row + VISUAL_BOARD_WIDTH_AND_HEIGHT
                length_row += VISUAL_BOARD_WIDTH_AND_HEIGHT + VISUAL_BOARD_WIDTH_AND_HEIGHT
            else:
                num_row = len(board_data) - VISUAL_BOARD_WIDTH_AND_HEIGHT
                length_row = len(board_data)

        return pawn_board

    def get_pawns(self, side):
        pawns = []
        for row in range(SQUARE_DIMENSION):
            for col in range(SQUARE_DIMENSION):
                if self.pawn_board[row][col] == side:
                    pawns.append((row, col)) 
        
        print(f"pawns {pawns}")       
        return pawns
    
    def get_my_pawns(self, request_data):
        my_side = request_data['data']['side']
        my_pawns = self.get_pawns(my_side)

        return my_pawns
    
    def get_opponent_paws(self, request_data):
        opponent_side = "S" if request_data['data']['side'] == "N" else "N"
        opponent_pawns = self.get_pawns(opponent_side)

        return opponent_pawns

    def get_cell(self, row, col):
        return self.pawn_board[row][col]
       

class WallBoard:
    def __init__(self, request_data):
        self.wall_board = self.format_wall_board(request_data) 

    def format_wall_board(self, request_data):
        board_data = request['data']['board']
        wall_board = []
        length_row = VISUAL_BOARD_WIDTH_AND_HEIGHT * 2
        num_row = VISUAL_BOARD_WIDTH_AND_HEIGHT

        for row in range(SLOT_DIMENSION):
            board_data_row = board_data[num_row : length_row : 2]
            wall_board.append(list(board_data_row))
            if row != SLOT_DIMENSION - 1:
                num_row = length_row + VISUAL_BOARD_WIDTH_AND_HEIGHT
                length_row += VISUAL_BOARD_WIDTH_AND_HEIGHT + VISUAL_BOARD_WIDTH_AND_HEIGHT
            else:
                num_row = len(board_data) - VISUAL_BOARD_WIDTH_AND_HEIGHT
                length_row = len(board_data)

        return wall_board

    # def get_walls(self, side):
    #     walls = []
    #     for row in range(9):
    #         for col in range(9):
    #             if self.wall_board[row][col] == side:
    #                 walls.append((row, col)) 
        
    #     print(f"pawns {walls}")       
    #     return walls
    

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
   
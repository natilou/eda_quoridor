from abc import ABC, abstractmethod
import asyncio
from sqlite3 import adapters
from urllib import request
import websockets 
import os
import random
import json

# Constants
URL = f"wss://4yyity02md.execute-api.us-east-1.amazonaws.com/ws?token={os.getenv('auth_token')}"
VISUAL_BOARD_DIMENSION = 17
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
        board = PawnBoard(request_data['data']['board'])

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
        wall_board = WallBoard(request_data['data']['board'])

        row = random.randint(0, 8)
        col = random.randint(0,8)
        orientation = random.choice(['h', 'v'])

        # FALTA VERIFICAR QUE ESAS COLUMNAS Y FILAS NO ESTEN OCUPADAS
        if wall_board.get_cell(row, col) != " ":
            row = random.randint(0,8)
            col = random.randint(0,8)

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
    def __init__(self, board):
        self.pawn_board = self.format_pawn_board(board)

    def format_pawn_board(self, board):
        board_data = board
        pawn_board = []
        length_row = VISUAL_BOARD_DIMENSION
        num_row = 0

        for row in range(SQUARE_DIMENSION):
            board_data_row = board_data[num_row : length_row : 2]
            pawn_board.append(list(board_data_row))
            if row != SQUARE_DIMENSION - 1:
                num_row = length_row + VISUAL_BOARD_DIMENSION
                length_row += VISUAL_BOARD_DIMENSION + VISUAL_BOARD_DIMENSION
            else:
                num_row = len(board_data) - VISUAL_BOARD_DIMENSION
                length_row = len(board_data)

        return pawn_board

    def get_pawns(self, side):
        pawns = []
        for row in range(SQUARE_DIMENSION):
            for col in range(SQUARE_DIMENSION):
                if self.pawn_board[row][col] == side:
                    pawns.append((row, col)) 

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
        print(f"get cell = {self.pawn_board[row][col]}")
        return self.pawn_board[row][col]
       

class VisualBoard:
    def __init__(self, board):
        self.visual_board = self.format_board(board)

    def format_board(self,board):
        board_data = board
        formatted_board = []
        length_row = VISUAL_BOARD_DIMENSION 
        num_row = 0

        for row in range(VISUAL_BOARD_DIMENSION):
            board_data_row = board_data[num_row : length_row]
            formatted_board.append(list(board_data_row))
            num_row += VISUAL_BOARD_DIMENSION
            length_row += VISUAL_BOARD_DIMENSION

        return formatted_board

    def get_cell(self, row, col):
        cell = self.visual_board[row][col]
        return cell

    
class WallBoard():
    def __init__(self, board):
        self.board = VisualBoard(board)
    
    def get_walls_positions(self):
        walls_positions = []

        for row in range(VISUAL_BOARD_DIMENSION):
            for col in range(VISUAL_BOARD_DIMENSION):
                if self.board.get_cell(row, col) == "-" and self.board.get_cell(row, col+1) == "*" and self.board.get_cell(row, col+2) == "-":
                    walls_positions.append(((row, col), (row, col+2)))

                if self.board.get_cell(row, col) == "|" and self.board.get_cell(row+1, col) == "*" and self.board.get_cell(row+2, col) == "|":
                    walls_positions.append(((row, col), (row+2, col)))

        return walls_positions


class AdapterBoard():
    @staticmethod
    def convert_wall_positions(positions_list):
        if not positions_list:
            return []
        
        positions_dict = {
            0: 0,
            1: 0,
            2: 1,
            3: 1,
            4: 2,
            5: 2,
            6: 3,
            7: 3,
            8: 4,
            9: 4,
            10: 5, 
            11: 5,
            12: 6,
            13: 6,
            14: 7,
            15: 7,
            16: 8
        }
        adapted_positions = []
        row1 = 0
        row2 = 0
        col1 = 0
        col2 = 0

        for position in positions_list: 
            row1 = positions_dict[position[0][0]]
            col1 = positions_dict[position[0][1]]
            row2 = positions_dict[position[1][0]]
            col2 = positions_dict[position[1][1]]
            adapted_positions.append(((row1, col1), (row2, col2)))
        return adapted_positions
    

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
   
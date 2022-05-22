from strategies.strategy import Strategy
from board.visual_board import VisualBoard
from bot.board.board_expert import BoardExpert
from bot.adapters.websocket_client import WebsocketClient
import random

# Concrete Strategy
class PutWall(Strategy): 
    @staticmethod
    async def perform_an_action(request_data):
        side = request_data["data"]["side"]
        wall_board = VisualBoard(request_data['data']['board'])

        cells_to_block = BoardExpert.slots_close_to_opposing_pawns(wall_board, side)
        
        print("paredes cercanas a peones oponentes")
        
        if not cells_to_block:
            print("no puedo poner paredes, que se mueva peon")

        else:
            print("puedo poner paredes, elijo celda")
            selected_cell = random.choice(cells_to_block)

            row = selected_cell[0]
            col = selected_cell[1]
            orientation = 'h' #random.choice(['h', 'v'])

       
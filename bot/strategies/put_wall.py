from bot.strategies.strategy import Strategy
from bot.board.visual_board import VisualBoard
from bot.board.board_expert import BoardExpert
import random

# Concrete Strategy
class PutWall(Strategy): 

    async def perform_an_action(self, request_data):

        if request_data['data']['walls'] > 0:

            side = request_data["data"]["side"]
       
            # get board
            board = VisualBoard(request_data['data']['board'])
    
            # look for cells close to pawns 
            available_pawns_to_block = BoardExpert.slots_close_to_opposing_pawns(board, side)

            if available_pawns_to_block:
                # select a cell to block
                selected_cell = random.choice(list(available_pawns_to_block))
                return selected_cell
            else:       
                raise Exception("No available moves")

                
       
       
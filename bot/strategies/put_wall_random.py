from bot.board.board_expert_walls import BoardExpertWalls
from bot.strategies.strategy import Strategy
from bot.board.visual_board import VisualBoard
from bot.board.board_expert_walls import BoardExpertWalls
import random

# Concrete Strategy
class PutWallRandom(Strategy): 

    async def perform_an_action(self, request_data):

        if request_data['data']['walls'] > 0:

            side = request_data["data"]["side"]
       
            # get board
            board = VisualBoard(request_data['data']['board'])
    
            # look for cells close to pawns 
            available_pawns_to_block = BoardExpertWalls.get_available_slots(board, side)

            if available_pawns_to_block:
                # select a cell to block
                selected_cell = random.choice(available_pawns_to_block)
                return selected_cell

        if self.get_next_strategy():
            return await self.get_next_strategy().perform_an_action(request_data)

        raise Exception("No available moves")
       
       
from bot.board.board_expert import BoardExpert
from bot.strategies.strategy import Strategy
from bot.board.visual_board import VisualBoard
import random

# Concrete Strategy
class MovePawn(Strategy):
    
    async def perform_an_action(self, request_data):

        if request_data["data"]["remaining_moves"] > 0:
            side = request_data['data']['side']
            
            # get board
            board = VisualBoard(request_data['data']['board'])
    
            # look for possible actions 
            available_actions = BoardExpert.check_available_moves(board, side)

            if available_actions:
                # select a Move to perform
                selected_pawn = random.choice(available_actions)
                return selected_pawn
            else:
                return await self.get_next_strategy().perform_an_action(request_data)
        else:
             return await self.get_next_strategy().perform_an_action(request_data)

        


    
from bot.board.board_expert_pawns import BoardExpertPawns
from bot.strategies.strategy import Strategy
from bot.board.visual_board import VisualBoard
import random

# Concrete Strategy
class MovePawnRandom(Strategy):
    
    async def perform_an_action(self, request_data):

        if request_data["data"]["remaining_moves"] > 0:
            side = request_data['data']['side']
            
            # get board
            board = VisualBoard(request_data['data']['board'])
    
            # look for possible actions 
            available_actions = BoardExpertPawns.get_available_moves(board, side)

            if available_actions:
                
                # select a Move to perform
                selected_pawn = random.choice(available_actions)
                return selected_pawn
        
        if self.get_next_strategy():
            return await self.get_next_strategy().perform_an_action(request_data)

        raise Exception("No available moves")
        


    
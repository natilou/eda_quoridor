from bot.board.board_expert_pawns import BoardExpertPawns
from bot.strategies.strategy import Strategy
from bot.board.visual_board import VisualBoard
from bot.domains.sorter import Sorter

# Concrete Strategy
class MoveAdvancedPawn(Strategy):
    
    async def perform_an_action(self, request_data):

        if request_data["data"]["remaining_moves"] > 0:
            side = request_data['data']['side']
            
            # get board
            board = VisualBoard(request_data['data']['board'])
    
            # look for possible actions 
            available_actions = BoardExpertPawns.get_available_moves(board, side)

            if available_actions:
                # sort Moves by advanced cells to move
                sorted_available_actions = sorted(available_actions, key=Sorter.sort)
                
                # choose advanced pawn
                selected_pawn = sorted_available_actions[0] if side == "S" else sorted_available_actions[-1]
                return selected_pawn
        
        if self.get_next_strategy():
            return await self.get_next_strategy().perform_an_action(request_data)

        raise Exception("No available moves")
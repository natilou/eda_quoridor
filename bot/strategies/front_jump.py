from bot.board.board_expert_pawns import BoardExpertPawns
from bot.strategies.strategy import Strategy
from bot.board.visual_board import VisualBoard

# Concrete Strategy
class FrontJump(Strategy):
    
    async def perform_an_action(self, request_data):

        if request_data["data"]["remaining_moves"] > 0:
            side = request_data['data']['side']
            
            # get board
            board = VisualBoard(request_data['data']['board'])
    
            # look for possible actions 
            available_actions = BoardExpertPawns.get_available_moves(board, side)

            if available_actions:
                # check if a pawn can make a front jump
                for move in available_actions:
                    if abs(move.from_cell[0] - move.to_cell[0]) == 2:
                        return move 
        
        if self.get_next_strategy():
            return await self.get_next_strategy().perform_an_action(request_data)

        raise Exception("No available moves")
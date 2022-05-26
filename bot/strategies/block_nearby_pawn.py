from bot.board.board_expert_walls import BoardExpertWalls
from bot.strategies.strategy import Strategy
from bot.board.visual_board import VisualBoard
from bot.board.board_expert_walls import BoardExpertWalls
from bot.constants import FINAL_ROW, INITIAL_ROW
from bot.sorter_by_row import sort_by_row

# Concrete Strategy
class BlockNearbyPawn(Strategy): 

    async def perform_an_action(self, request_data):

        if request_data['data']['walls'] > 0:

            side = request_data["data"]["side"]
       
            # get board
            board = VisualBoard(request_data['data']['board'])
    
            # look for cells close to pawns 
            available_pawns_to_block = BoardExpertWalls.get_available_slots(board, side)

            if available_pawns_to_block:
                horizontal_walls = []
                for move in available_pawns_to_block:
                    if(
                        move.orientation == "h" 
                        and (side == "N" and move.to_cell[0] < FINAL_ROW or side == "S" and move.to_cell[0] > INITIAL_ROW)
                    ):
                        horizontal_walls.append(move)
                    
                
                if horizontal_walls:
                    sorted_horizontal_walls = sorted(horizontal_walls, key=sort_by_row)

                    return sorted_horizontal_walls[0] if side == "N" else sorted_horizontal_walls[-1]

        if self.get_next_strategy():
            return await self.get_next_strategy().perform_an_action(request_data)

        raise Exception("No available moves")
       
       
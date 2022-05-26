from bot.board.adapter_board import AdapterBoard
from bot.domains.move import Move
from bot.domains.wall_move import WallMove
from bot.constants import FINAL_COL, MOVE_TYPE_WALL, INITIAL_COL
from typing import List

class BoardExpertWalls: 
    
    @staticmethod
    def possible_cells_to_block(board, side) -> List[Move]:
        opponent_pawns_positions = AdapterBoard.convert_pawn_positions(board.get_opponent_pawns(side))
        in_front_of_opponent = -1 if side == "N" else 0

        cells_to_block = []

        for (row, col) in opponent_pawns_positions:
                if col < FINAL_COL:
                    cells_to_block.append(WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(row+in_front_of_opponent, col), orientation="h"))
                    cells_to_block.append(WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(row+in_front_of_opponent, col), orientation="v"))
                
                if col > INITIAL_COL:
                    cells_to_block.append(WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(row+in_front_of_opponent, col-1), orientation="h"))
                    cells_to_block.append(WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(row+in_front_of_opponent, col-1), orientation="v"))

        return cells_to_block

    @staticmethod
    def get_available_slots(board, side) -> List[Move]:
        walls_positions = AdapterBoard.convert_wall_positions(board.get_walls_positions())
        possible_cells_to_block = BoardExpertWalls.possible_cells_to_block(board, side)

        available_slots = list(possible_cells_to_block)

        for move in possible_cells_to_block:
            for (tuple1, tuple2, orientation) in walls_positions:
                if ((move.to_cell[0], move.to_cell[1]) == tuple1 or (move.to_cell[0], move.to_cell[1]) == tuple2):
                    available_slots.remove((WallMove(MOVE_TYPE_WALL, (), (move.to_cell[0], move.to_cell[1]), move.orientation)))
                    break
                if (
                    ((move.to_cell[0], move.to_cell[1]+1) == tuple1 or (move.to_cell[0], move.to_cell[1]+1) == tuple2)
                    and orientation == "h" 
                    ):
                    available_slots.remove((WallMove(MOVE_TYPE_WALL, (), (move.to_cell[0], move.to_cell[1]), move.orientation)))
                    break
                if (
                    ((move.to_cell[0]+1, move.to_cell[1]) == tuple1 or (move.to_cell[0]+1, move.to_cell[1]) == tuple2)
                    and orientation == "v" 
                    ):
                    available_slots.remove((WallMove(MOVE_TYPE_WALL, (), (move.to_cell[0], move.to_cell[1]), move.orientation)))
                    break
        
        return available_slots
        

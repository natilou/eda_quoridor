from bot.board.adapter_board import AdapterBoard
from bot.domains.move import Move
from bot.constants import MOVE_TYPE_PAWN, FINAL_ROW, FINAL_COL, INITIAL_COL, INITIAL_ROW
from typing import List


class BoardExpertPawns: 

    @staticmethod
    def check_pawns_with_walls(board, side) -> List:
             
        # get pawns and walls positions
        my_pawns_positions = AdapterBoard.convert_pawn_positions(board.get_my_pawns(side))
        walls_positions = AdapterBoard.convert_wall_positions(board.get_walls_positions())
        
        
        # check if there are walls in pawns positions
        in_front_of_opponent = -1 if side == "S" else 0
        cells_with_walls = []
        
        if walls_positions:
            for (row, col) in my_pawns_positions:
                for (tuple1, tuple2, orientation) in walls_positions:
                    if (row+in_front_of_opponent, col) == tuple1 and orientation == "h":
                        cells_with_walls.append((row, col))
                    elif (row+in_front_of_opponent, col) == tuple2 and orientation == "h":
                        cells_with_walls.append((row, col))
        
        return cells_with_walls

    @staticmethod
    def move_forward(board, side) -> List[Move]:

        # get pawns and walls positions 
        opponent_pawns_positions = AdapterBoard.convert_pawn_positions(board.get_opponent_pawns(side))
        my_pawns_positions = AdapterBoard.convert_pawn_positions(board.get_my_pawns(side))
        cells_with_walls = BoardExpertPawns.check_pawns_with_walls(board, side)
        
        move_forward = 1 if side == "N" else -1
        all_available_moves_forward = []
        
        for (row, col) in my_pawns_positions:

            # move forward            
            if (row+move_forward, col) not in opponent_pawns_positions and (row, col) not in cells_with_walls:
                all_available_moves_forward.append(
                    Move(type=MOVE_TYPE_PAWN, from_cell=(row, col), to_cell=(row+move_forward, col))
                )

            # font jump  
            if (
                ((row+move_forward) != FINAL_ROW or (row+move_forward) != INITIAL_ROW)
                and (row+move_forward, col) in opponent_pawns_positions
                and (row, col) not in cells_with_walls
                and (row+move_forward, col) not in cells_with_walls
            ):
                all_available_moves_forward.append(
                    Move(type=MOVE_TYPE_PAWN, from_cell=(row, col), to_cell=(row+move_forward+move_forward, col))
                )

            # diagonal jump 
            if (
                (row+move_forward, col) in opponent_pawns_positions 
                and (row, col) not in cells_with_walls 
                and (row+move_forward, col) in cells_with_walls 
                and (row+move_forward, col-1) not in cells_with_walls 
                and (row+move_forward, col-1) not in opponent_pawns_positions
            ):
                all_available_moves_forward.append(
                    Move(type=MOVE_TYPE_PAWN, from_cell=(row, col), to_cell=(row+move_forward, col-1))
                )
        return all_available_moves_forward

    @staticmethod
    def move_to_sides(board, side) -> List[Move]:

        # get pawns and walls positions
        opponent_pawns_positions = AdapterBoard.convert_pawn_positions(board.get_opponent_pawns(side))
        my_pawns_positions = AdapterBoard.convert_pawn_positions(board.get_my_pawns(side))
        cells_with_walls = BoardExpertPawns.check_pawns_with_walls(board, side)

        all_available_moves_to_sides = [] 

        for (row, col) in my_pawns_positions:
           
            # move to right side
            if col < FINAL_COL:
                if (row, col) in cells_with_walls and (row, col+1) not in cells_with_walls and (row, col+1) not in opponent_pawns_positions:
                    all_available_moves_to_sides.append(
                        Move(type=MOVE_TYPE_PAWN, from_cell=(row, col), to_cell=(row, col+1))
                    )
        
            # move to left side
            if col > INITIAL_COL:
                if (row, col) in cells_with_walls and (row, col-1) not in cells_with_walls and (row, col-1) not in opponent_pawns_positions:
                    all_available_moves_to_sides.append(
                        Move(type=MOVE_TYPE_PAWN, from_cell=(row, col), to_cell=(row, col-1))
                        )
              

        return all_available_moves_to_sides

    @staticmethod
    def get_available_moves(board, side) -> List[Move]:
        return BoardExpertPawns.move_forward(board, side) + BoardExpertPawns.move_to_sides(board, side)


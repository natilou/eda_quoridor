from bot.board.adapter_board import AdapterBoard
from bot.domains.move import Move
from bot.constants import MOVE_TYPE_PAWN, MOVE_TYPE_WALL
from typing import Set


class BoardExpert: 

    @staticmethod
    def check_pawns_with_walls(board, side):
             
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
    def move_forward(board, side): 
        opponent_pawns_positions = AdapterBoard.convert_pawn_positions(board.get_opponent_pawns(side))
        my_pawns_positions = AdapterBoard.convert_pawn_positions(board.get_my_pawns(side))
        cells_with_walls = BoardExpert.check_pawns_with_walls(board, side)

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
                ((row+move_forward) != 8 or (row+move_forward) != 0)
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
    def move_to_sides(board, side):
        opponent_pawns_positions = AdapterBoard.convert_pawn_positions(board.get_opponent_pawns(side))
        my_pawns_positions = AdapterBoard.convert_pawn_positions(board.get_my_pawns(side))
        cells_with_walls = BoardExpert.check_pawns_with_walls(board, side)

        all_available_moves_to_sides = [] 

        for (row, col) in my_pawns_positions:
            if side == "S":
                # move right side
                if col < 8:
                    if (row, col) in cells_with_walls and (row, col+1) not in cells_with_walls and (row, col+1) not in opponent_pawns_positions:
                        all_available_moves_to_sides.append(
                            Move(type=MOVE_TYPE_PAWN, from_cell=(row, col), to_cell=(row, col+1))
                        )
            
                # move left side
                if col > 0:
                    if (row, col) in cells_with_walls and (row, col-1) not in cells_with_walls and (row, col-1) not in opponent_pawns_positions:
                        all_available_moves_to_sides.append(
                            Move(type=MOVE_TYPE_PAWN, from_cell=(row, col), to_cell=(row, col-1))
                        )
            elif side == "N":
                # move right side
                if col < 8:
                    if (row, col) in cells_with_walls and (row, col+1) not in cells_with_walls and (row, col+1) not in opponent_pawns_positions:
                        all_available_moves_to_sides.append(
                            Move(type=MOVE_TYPE_PAWN, from_cell=(row, col), to_cell=(row, col+1))
                        )
            
                # move left side
                if col > 0:
                    if (row, col) in cells_with_walls and (row, col-1) not in cells_with_walls and (row, col-1) not in opponent_pawns_positions:
                        all_available_moves_to_sides.append(
                            Move(type=MOVE_TYPE_PAWN, from_cell=(row, col), to_cell=(row, col-1))
                        )

        return all_available_moves_to_sides

    @staticmethod
    def check_available_moves(board, side):
        return BoardExpert.move_forward(board, side) + BoardExpert.move_to_sides(board, side)

    @staticmethod
    def slots_close_to_opposing_pawns(board, side) -> Set[Move]:
        opponent_pawns_positions = AdapterBoard.convert_pawn_positions(board.get_opponent_pawns(side))
        walls_positions = AdapterBoard.convert_wall_positions(board.get_walls_positions())


        # check the positions of the opposing pawns and check if there are cells near them available to put walls
        available_slots = set()
        in_front_of_opponent = -1 if side == "N" else 0

        if walls_positions: 
            for (row, col) in opponent_pawns_positions:
                for (tuple1, tuple2, orientation) in walls_positions:
                    if(side == "N" and row > 0 or side == "S" and row < 8) and (col > 0 or col < 8):
                        if ((row+in_front_of_opponent, col) == tuple1 or (row+in_front_of_opponent, col) == tuple2) and orientation == "h":
                            if (Move("wall", (), (row+in_front_of_opponent, col))) in available_slots:
                                available_slots.remove(Move("wall", (), (row+in_front_of_opponent, col)))
                                break
                            else:
                                break
                        if (
                            (((row+in_front_of_opponent, col) == tuple1 or (row+in_front_of_opponent, col) == tuple2)) 
                            and orientation == "v"
                            ):
                            available_slots.add(Move(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(row+in_front_of_opponent, col-1)))
                        if (
                            ((((row, col) == tuple1 or (row, col) == tuple2)) 
                            and orientation == "v")
                            ):
                            available_slots.add(Move(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(row+in_front_of_opponent, col-1)))      
                        if (row+in_front_of_opponent, col) != tuple1 or (row+in_front_of_opponent, col) != tuple2:
                            available_slots.add(Move(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(row+in_front_of_opponent, col)))


        return available_slots
        


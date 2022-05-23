from bot.board.adapter_board import AdapterBoard
from bot.domains.move import Move
from bot.constants import MOVE_TYPE_PAWN, MOVE_TYPE_WALL


class BoardExpert:
   
    @staticmethod
    def check_available_moves(board, side):
             
        # get pawns and walls positions
        my_pawns_positions = AdapterBoard.convert_pawn_positions(board.get_my_pawns(side))
        opponent_pawns_positions = AdapterBoard.convert_pawn_positions(board.get_opponent_pawns(side))
        walls_positions = AdapterBoard.convert_wall_positions(board.get_walls_positions())
        
        
        # check if there are walls in pawns positions
        move_forward = 1 if side == "N" else -1
        cells_with_walls = []
        
        if walls_positions:
            for (row, col) in my_pawns_positions:
                for wall in walls_positions:
                    if side == "N":
                        if row == wall[0][0] and col == wall[0][1]:
                            cells_with_walls.append((row, col))
                        elif row == wall[1][0] and col == wall[1][1]:
                            cells_with_walls.append((row, col))
                    elif side == "S":
                        if (row-1) == wall[0][0] and col == wall[0][1]:
                            cells_with_walls.append((row, col))
                        elif (row-1) == wall[1][0] and col == wall[1][1]:
                            cells_with_walls.append((row, col))

        
        all_available_moves = []

        for (row, col) in my_pawns_positions:

            # move forward            
            if (row+move_forward, col) not in opponent_pawns_positions and (row, col) not in cells_with_walls:
                all_available_moves.append(
                    Move(type=MOVE_TYPE_PAWN, from_cell=(row, col), to_cell=(row+move_forward, col))
                )

            # font jump  
            if (
                ((row+move_forward) != 8 or (row+move_forward) != 0)
                and (row+move_forward, col) in opponent_pawns_positions
                and (row, col) not in cells_with_walls
                and (row+move_forward, col) not in cells_with_walls
            ):
                all_available_moves.append(
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
                all_available_moves.append(
                    Move(type=MOVE_TYPE_PAWN, from_cell=(row, col), to_cell=(row+move_forward, col-1))
                )

           
            if side == "S":
                # move right side
                if col < 8:
                    if (row, col) in cells_with_walls and (row, col+1) not in cells_with_walls and (row, col+1) not in opponent_pawns_positions:
                        all_available_moves.append(
                            Move(type=MOVE_TYPE_PAWN, from_cell=(row, col), to_cell=(row, col+1))
                        )
            
                # move left side
                if col > 0:
                    if (row, col) in cells_with_walls and (row, col-1) not in cells_with_walls and (row, col-1) not in opponent_pawns_positions:
                        all_available_moves.append(
                            Move(type=MOVE_TYPE_PAWN, from_cell=(row, col), to_cell=(row, col-1))
                        )
            elif side == "N":
                # move right side
                if col < 8:
                    if (row, col) in cells_with_walls and (row, col+1) not in cells_with_walls and (row, col+1) not in opponent_pawns_positions:
                        all_available_moves.append(
                            Move(type=MOVE_TYPE_PAWN, from_cell=(row, col), to_cell=(row, col+1))
                        )
            
                # move left side
                if col > 0:
                    if (row, col) in cells_with_walls and (row, col-1) not in cells_with_walls and (row, col-1) not in opponent_pawns_positions:
                        all_available_moves.append(
                            Move(type=MOVE_TYPE_PAWN, from_cell=(row, col), to_cell=(row, col-1))
                        )

        return all_available_moves

    @staticmethod
    def slots_close_to_opposing_pawns(board, side):
        opponent_pawns_positions = AdapterBoard.convert_pawn_positions(board.get_opponent_pawns(side))
        walls_positions = AdapterBoard.convert_wall_positions(board.get_walls_positions())

        # check the positions of the opposing pawns and check if there are cells near them available to put walls
        available_slots = []
        in_front_of_opponent = -1 if side == "N" else 0

        if walls_positions:    
            for wall in walls_positions:
                for (row, col) in opponent_pawns_positions:
                    if (
                        ((row+in_front_of_opponent)!= wall[0][0] and col != wall[0][1]) 
                        and ((row+in_front_of_opponent) != wall[1][0] and col != wall[1][1])
                    ):
                        available_slots.append(
                            Move(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(row+in_front_of_opponent, col))
                        )
     
        return available_slots
        


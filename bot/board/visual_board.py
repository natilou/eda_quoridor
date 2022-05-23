from bot.constants import VISUAL_BOARD_DIMENSION

class VisualBoard:
    def __init__(self, board):
        self.visual_board = self.format_board(board)

    def format_board(self,board):
        board_data = board
        formatted_board = []
        length_row = VISUAL_BOARD_DIMENSION 
        num_row = 0

        for row in range(VISUAL_BOARD_DIMENSION):
            board_data_row = board_data[num_row : length_row]
            formatted_board.append(list(board_data_row))
            num_row += VISUAL_BOARD_DIMENSION
            length_row += VISUAL_BOARD_DIMENSION

        return formatted_board

    def get_cell(self, row, col):
        return self.visual_board[row][col]

    def get_walls_positions(self):
        walls_positions = []

        for row in range(VISUAL_BOARD_DIMENSION):
            for col in range(VISUAL_BOARD_DIMENSION):
                if self.get_cell(row, col) == "-" and self.get_cell(row, col+1) == "*" and self.get_cell(row, col+2) == "-":
                    walls_positions.append(((row, col), (row, col+2)))

                if self.get_cell(row, col) == "|" and self.get_cell(row+1, col) == "*" and self.get_cell(row+2, col) == "|":
                    walls_positions.append(((row, col), (row+2, col)))

        return walls_positions

    def get_pawns(self, side):
        pawns = []
        for row in range(VISUAL_BOARD_DIMENSION):
            for col in range(VISUAL_BOARD_DIMENSION):
                if self.get_cell(row, col) == side:
                    pawns.append((row, col)) 

        return pawns
    
    def get_my_pawns(self, side_data):
        my_side = side_data
        my_pawns = self.get_pawns(my_side)

        return my_pawns
    
    def get_opponent_pawns(self, side_data):
        opponent_side = "S" if side_data == "N" else "N"
        opponent_pawns = self.get_pawns(opponent_side)

        return opponent_pawns
    
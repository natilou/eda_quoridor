
class AdapterBoard():
    @staticmethod
    def convert_pawn_positions(positions_list):
        if not positions_list:
            return []
        
        adapted_positions = []

        for (row, col) in positions_list:
            adapted_row = row // 2 
            adapted_col = col // 2
            adapted_positions.append((adapted_row, adapted_col))
        
        return adapted_positions

    @staticmethod
    def convert_wall_positions(positions_list):
        
        if not positions_list:
            return []

        adapted_positions = []
        
        for (tuple1, tuple2, orientation) in positions_list: 
            adapted_row1 = tuple1[0] // 2
            adapted_col1 = tuple1[1] // 2
            adapted_row2 = tuple2[0] // 2
            adapted_col2 = tuple2[1] // 2
            adapted_positions.append(
                (
                    (adapted_row1, adapted_col1), 
                    (adapted_row2, adapted_col2),
                    orientation
                )
            )
        
        return adapted_positions
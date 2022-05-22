
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
        
        # TODO: ver si se puede mejorar lógica
        for position in positions_list: 
            if len(positions_list) < 1:
                adapted_row1 = position[0] // 2
                adapted_col1 = position[1] // 2
                adapted_positions.append((adapted_row1, adapted_col1))
            else:
                adapted_row1 = [position[0][0]] // 2
                adapted_col1 = [position[0][1]] // 2
                adapted_row2 = [position[1][0]] // 2
                adapted_col2 = [position[1][1]] // 2
                adapted_positions.append(((adapted_row1, adapted_col1), (adapted_row2, adapted_col2)))
        
        return adapted_positions
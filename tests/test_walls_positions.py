import pytest
from test_scenarios import *
from bot.game import VisualBoard

class TestWallsPositions:
    @pytest.mark.parametrize("board,expected", [
        (
            SCENARIO_WITHOUT_S_PAWNS,
            [((3,2), (3,4)), ((4,1), (6,1))]
        ),
        (
            SCENARIO_WITH_BOTH_PAWNS, 
            [((3,2), (3,4)), ((4,1), (6,1))]
        ), 
        (
            SCENARIO_WITHOUT_N_PAWNS, 
            [((3,2), (3,4)), ((4,1), (6,1))]
        ), 
        (
            SCENARIO_WITH_HORIZONTAL_WALLS,
            [
                ((3,6), (3,8)), 
                ((3,12), (3,14)),
                ((7, 2), (7, 4)),
                ((7, 10), (7, 12)), 
                ((9, 6), (9, 8)), 
                ((11, 2), (11, 4)), 
                ((11, 10), (11, 12)), 
                ((13, 0), (13, 2))

            ]
        ), 
        (
            SCENARIO_WITH_VERTICAL_WALLS,
            [
                ((2,9), (4,9)), 
                ((4,3), (6,3)), 
                ((6,7), (8,7)), 
                ((8,15), (10,15)), 
                ((10,1), (12,1)), 
                ((10,7), (12,7)), 
                ((10,11), (12,11)), 
                ((12,5), (14,5))
            ]
        ), 
        (
            SCENARIO_WITH_BOTH_WALLS,
            [
                ((2,9), (4,9)),
                ((3,4), (3,6)), 
                ((3,12), (3,14)), 
                ((6,7), (8,7)),
                ((7,2), (7,4)),
                ((8,15), (10,15)),
                ((10,1), (12,1)),
                ((10,11), (12,11)),
                ((11,6), (11,8)),
                ((13,4), (13,6)) 
            ]
        ), 
        (
            SCENARIO_WITHOUT_WALLS,
            []
        )

    ])
    def test_get_walls_positions(self, board, expected):
        wall_board = VisualBoard(board)
        wall_positions = wall_board.get_walls_positions()
        assert wall_positions == expected

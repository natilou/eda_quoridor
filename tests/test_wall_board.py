from cmath import exp
import pytest
from test_scenarios import *
from bot.bot import WallBoard, AdapterBoard

class TestBoardPawn:
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
        wall_board = WallBoard(board)
        wall_positions = wall_board.get_walls_positions()
        assert wall_positions == expected


class TestAdapterBoard():
    @pytest.mark.parametrize("board, expected", [
        (
            SCENARIO_WITHOUT_S_PAWNS,
            [
                ((1,1), (1,2)), 
                ((2,0), (3,0))
            ]
        ),
        (
            SCENARIO_WITH_BOTH_PAWNS, 
            [
                ((1,1), (1,2)), 
                ((2,0), (3,0))
            ]
        ), 
        (
            SCENARIO_WITHOUT_N_PAWNS, 
           [
                ((1,1), (1,2)), 
                ((2,0), (3,0))
            ]
        ), 
        (
            SCENARIO_WITH_HORIZONTAL_WALLS,
            [
                ((1,3), (1,4)), 
                ((1,6), (1,7)),
                ((3, 1), (3, 2)),
                ((3, 5), (3, 6)), 
                ((4, 3), (4, 4)), 
                ((5, 1), (5, 2)), 
                ((5, 5), (5, 6)), 
                ((6, 0), (6, 1))

            ]
        ), 
        (
            SCENARIO_WITH_VERTICAL_WALLS,
            [
                ((1,4), (2,4)), 
                ((2,1), (3,1)), 
                ((3,3), (4,3)), 
                ((4,7), (5,7)), 
                ((5,0), (6,0)), 
                ((5,3), (6,3)), 
                ((5,5), (6,5)), 
                ((6,2), (7,2))
            ]
        ), 
        (
            SCENARIO_WITH_BOTH_WALLS,
            [
                ((1,4), (2,4)),
                ((1,2), (1,3)), 
                ((1,6), (1,7)), 
                ((3,3), (4,3)),
                ((3,1), (3,2)),
                ((4,7), (5,7)),
                ((5,0), (6,0)),
                ((5,5), (6,5)),
                ((5,3), (5,4)),
                ((6,2), (6,3)) 
            ]
        ), 
        (
            SCENARIO_WITHOUT_WALLS,
            []
        )
    ])
    def test_convert_wall_positions(self, board, expected):
        wall_board = WallBoard(board)
        wall_positions = wall_board.get_walls_positions()
        converted_positions = AdapterBoard.convert_wall_positions(wall_positions)
        assert converted_positions == expected


from bot.board.visual_board import VisualBoard
from bot.board.adapter_board import AdapterBoard
from test_scenarios import *
import pytest

class TestAdapterWallsPositions():
    @pytest.mark.parametrize("board, expected", [
        (
            SCENARIO_WITHOUT_S_PAWNS,
            [
                ((1,1), (1,2), "h"), 
                ((2,0), (3,0), "v")
            ]
        ),
        (
            SCENARIO_WITH_BOTH_PAWNS, 
            [
                ((1,1), (1,2), "h"), 
                ((2,0), (3,0), "v")
            ]
        ), 
        (
            SCENARIO_WITHOUT_N_PAWNS, 
            [
                ((1,1), (1,2), "h"), 
                ((2,0), (3,0), "v")
            ]
        ), 
        (
            SCENARIO_WITH_HORIZONTAL_WALLS,
            [
                ((1,3), (1,4), "h"), 
                ((1,6), (1,7), "h"),
                ((3,1), (3,2), "h"),
                ((3,5), (3,6), "h"), 
                ((4,3), (4,4), "h"), 
                ((5,1), (5,2), "h"), 
                ((5,5), (5,6), "h"), 
                ((6,0), (6,1), "h")
            ]
        ), 
        (
            SCENARIO_WITH_VERTICAL_WALLS,
            [
                ((1,4), (2,4,), "v"), 
                ((2,1), (3,1,), "v"), 
                ((3,3), (4,3,), "v"), 
                ((4,7), (5,7,), "v"), 
                ((5,0), (6,0,), "v"), 
                ((5,3), (6,3,), "v"), 
                ((5,5), (6,5,), "v"), 
                ((6,2), (7,2,), "v")
            ]
        ), 
        (
            SCENARIO_WITH_BOTH_WALLS,
            [
                ((1,4), (2,4), "v"),
                ((1,2), (1,3), "h"), 
                ((1,6), (1,7), "h"), 
                ((3,3), (4,3), "v"),
                ((3,1), (3,2), "h"),
                ((4,7), (5,7), "v"),
                ((5,0), (6,0), "v"),
                ((5,5), (6,5), "v"),
                ((5,3), (5,4), "h"),
                ((6,2), (6,3), "h") 
            ]
        ), 
        (
            SCENARIO_WITHOUT_WALLS,
            []
        ), 
        (
            SCENARIO_RANDOM, 
            [
                ((6, 0), (7, 0), 'v'), 
                ((6, 4), (6, 5), 'h'), 
                ((7, 4), (7, 5), 'h')
            ]
        ), 
        (
            SCENARIO_MIDDLE_WALLS, 
            [
                ((1, 2), (1, 3), 'h'),
                ((3, 0), (3, 1), 'h'),
                ((3, 2), (3, 3), 'h'),
                ((3, 4), (3, 5), 'h'),
                ((3, 6), (3, 7), 'h')
            ]
        )
    ])

    def test_convert_wall_positions(self, board, expected):
        wall_board = VisualBoard(board)
        wall_positions = wall_board.get_walls_positions()
        converted_positions = AdapterBoard.convert_wall_positions(wall_positions)
        assert converted_positions == expected

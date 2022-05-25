import pytest
from tests.test_scenarios import *
from bot.board.visual_board import VisualBoard

class TestWallsPositions:
    @pytest.mark.parametrize("board,expected", [
        (
            SCENARIO_WITHOUT_S_PAWNS,
            [
                ((3,2), (3,4), "h"), 
                ((4,1), (6,1), "v")
            ]
        ),
        (
            SCENARIO_WITH_BOTH_PAWNS, 
            [
                ((3,2), (3,4), "h"), 
                ((4,1), (6,1), "v")
            ]
        ), 
        (
            SCENARIO_WITHOUT_N_PAWNS, 
            [
                ((3,2), (3,4), "h"), 
                ((4,1), (6,1), "v")
            ]
        ), 
        (
            SCENARIO_WITH_HORIZONTAL_WALLS,
            [
                ((3,6), (3,8), "h"), 
                ((3,12), (3,14), "h"),
                ((7, 2), (7, 4), "h"),
                ((7, 10), (7, 12), "h"), 
                ((9, 6), (9, 8), "h"), 
                ((11, 2), (11, 4), "h"), 
                ((11, 10), (11, 12), "h"), 
                ((13, 0), (13, 2), "h" )

            ]
        ), 
        (
            SCENARIO_WITH_VERTICAL_WALLS,
            [
                ((2,9), (4,9), "v"), 
                ((4,3), (6,3), "v"), 
                ((6,7), (8,7), "v"), 
                ((8,15), (10,15), "v"), 
                ((10,1), (12,1), "v"), 
                ((10,7), (12,7), "v"), 
                ((10,11), (12,11), "v"), 
                ((12,5), (14,5), "v")
            ]
        ), 
        (
            SCENARIO_WITH_BOTH_WALLS,
            [
                ((2,9), (4,9), "v"),
                ((3,4), (3,6), "h"), 
                ((3,12), (3,14), "h"), 
                ((6,7), (8,7), "v"),
                ((7,2), (7,4), "h"),
                ((8,15), (10,15), "v"),
                ((10,1), (12,1), "v"),
                ((10,11), (12,11), "v"),
                ((11,6), (11,8), "h"),
                ((13,4), (13,6), "h") 
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

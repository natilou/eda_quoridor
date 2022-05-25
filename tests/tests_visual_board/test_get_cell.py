import pytest
from tests.test_scenarios import *
from bot.board.visual_board import VisualBoard

class TestGetCell:
    @pytest.mark.parametrize("board,row,col,expected", [
        (
            SCENARIO_WITHOUT_S_PAWNS,
            0, 0, " "
        ),
        (
            SCENARIO_WITHOUT_S_PAWNS,
            2, 2, "N"
        ), 
        (
            SCENARIO_WITH_BOTH_PAWNS, 
            16, 8, "S"
        ), 
        (
            SCENARIO_WITH_BOTH_PAWNS, 
            6, 6, "N"
        ), 
        (
            SCENARIO_WITHOUT_N_PAWNS,
            1, 1, " "
        ),
        (
            SCENARIO_WITHOUT_N_PAWNS,
            3, 4, "-"
        ), 
        (
            SCENARIO_WITH_HORIZONTAL_WALLS,
            11, 12, "-"
        ),
        (
            SCENARIO_WITH_HORIZONTAL_WALLS,
            3, 12, "-"
        ), 
        (
            SCENARIO_WITH_VERTICAL_WALLS,
            10, 15, "|"
        ),
        (
            SCENARIO_WITH_VERTICAL_WALLS,
            14, 12, "S"
        ), 
        (
            SCENARIO_WITH_BOTH_WALLS,
            3, 6, "-"
        ),
        (
            SCENARIO_WITH_BOTH_WALLS,
            12, 11, "|"
        ),
        (
            SCENARIO_WITHOUT_WALLS,
            0, 8, " "
        ),
        (
            SCENARIO_WITHOUT_WALLS,
            4, 8, "N"
        ),
    ])
    def test_get_cell(self, board, row, col, expected):
        board = VisualBoard(board)
        cell = board.get_cell(row, col)
        assert cell == expected
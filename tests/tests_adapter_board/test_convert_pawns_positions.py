from bot.board.visual_board import VisualBoard
from bot.board.adapter_board import AdapterBoard
from test_scenarios import *
import pytest

class TestAdapterWallsPositions():
    @pytest.mark.parametrize("board,side,expected", [
        (
            SCENARIO_WITHOUT_S_PAWNS,
            "S",
            []
        ),
        (
            SCENARIO_WITHOUT_S_PAWNS,
            "N",
            [(1,1), (4,0), (4,4)]
        ), 
        (
            SCENARIO_WITH_BOTH_PAWNS, 
            "S",
            [(5,3), (6,6), (8,4)]
        ), 
        (
            SCENARIO_WITH_BOTH_PAWNS, 
            "N",
            [(0,6), (3,3), (6,4)]
        ), 
        (
            SCENARIO_WITHOUT_N_PAWNS,
            "N",
            []
        ),
        (
            SCENARIO_WITHOUT_N_PAWNS,
            "S",
            [(1,1), (4,0), (4,4)]
        ), 
        (
            SCENARIO_WITH_HORIZONTAL_WALLS,
            "N",
            [(0,4),(2,8), (3,1)]
        ),
        (
            SCENARIO_WITH_HORIZONTAL_WALLS,
            "S",
            [(2,0), (5,3), (6,7)]
        ), 
        (
            SCENARIO_WITH_VERTICAL_WALLS,
            "N",
            [(1,2), (2,7), (3,4)]
        ),
        (
            SCENARIO_WITH_VERTICAL_WALLS,
            "S",
            [(2,1), (4,3), (7,6)]
        ), 
        (
            SCENARIO_WITH_BOTH_WALLS,
            "N",
            [(1,3), (4,6), (5,4)]
        ),
        (
            SCENARIO_WITH_BOTH_WALLS,
            "S",
            [(2,0), (4,2), (7,7)]
        ),
        (
            SCENARIO_WITHOUT_WALLS,
            "S",
            [(1,1), (2,7), (4,4)]
        ),
        (
            SCENARIO_WITHOUT_WALLS,
            "N",
            [(2,4), (6,2), (7,6)]
        ),
        (
            SCENARIO_RANDOM,
            "S",
            [(1, 3), (1, 7), (3, 7)]
        ),
        (
            SCENARIO_RANDOM,
            "N",
            [(0, 7), (0, 8), (1, 2)]
        ),
        (
            SCENARIO_MIDDLE_WALLS,
            "S",
            [(4, 8), (5, 3), (7, 2)]
        ),
        (
            SCENARIO_MIDDLE_WALLS,
            "N",
            [(0, 1), (1, 3), (3, 7)]
        ),
        (
            SCENARIO_RANDOM2, 
            "N", 
            [(5, 7), (5, 8), (7, 6)]
        ), 
        (
            SCENARIO_RANDOM2, 
            "S", 
            [(4, 3), (8, 4), (8, 7)]
        )

    ])    
    def test_convert_pawn_positions(self, board, side, expected):
        pawn_board = VisualBoard(board)
        pawn_positions = pawn_board.get_my_pawns(side)
        convert_positions = AdapterBoard.convert_pawn_positions(pawn_positions)
        assert convert_positions == expected

    

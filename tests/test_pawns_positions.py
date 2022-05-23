import pytest
from test_scenarios import *
from bot.board.visual_board import VisualBoard

class TestPawnsPositions:
    @pytest.mark.parametrize("board,side,expected", [
        (
            SCENARIO_WITHOUT_S_PAWNS,
            "S",
            []
        ),
        (
            SCENARIO_WITHOUT_S_PAWNS,
            "N",
            [(2,2), (8,0), (8,8)]
        ), 
        (
            SCENARIO_WITH_BOTH_PAWNS, 
            "S",
            [(10,6), (12,12), (16,8)]
        ), 
        (
            SCENARIO_WITH_BOTH_PAWNS, 
            "N",
            [(0,12), (6,6), (12,8)]
        ), 
        (
            SCENARIO_WITHOUT_N_PAWNS,
            "N",
            []
        ),
        (
            SCENARIO_WITHOUT_N_PAWNS,
            "S",
            
        ), 
        (
            SCENARIO_WITH_HORIZONTAL_WALLS,
            "N",
            [(0,8),(4,16), (6,2)]
        ),
        (
            SCENARIO_WITH_HORIZONTAL_WALLS,
            "S",
            [(4,0), (10,6), (12,14)]
        ), 
        (
            SCENARIO_WITH_VERTICAL_WALLS,
            "N",
            [(2,4), (4,14), (6,8)]
        ),
        (
            SCENARIO_WITH_VERTICAL_WALLS,
            "S",
            [(4,2), (8,6), (14,12)]
        ), 
        (
            SCENARIO_WITH_BOTH_WALLS,
            "N",
            [(2,6), (8,12), (10,8)]
        ),
        (
            SCENARIO_WITH_BOTH_WALLS,
            "S",
            [(4,0), (8,4), (14,14)]
        ),
        (
            SCENARIO_WITHOUT_WALLS,
            "S",
            [(2,2), (4,14), (8,8)]
        ),
        (
            SCENARIO_WITHOUT_WALLS,
            "N",
            [(4,8), (12,4), (14,12)]
        ),
    ])
    
    def test_get_pawns(self, board, side, expected):
        pawn_board = VisualBoard(board)
        pawns_positions = pawn_board.get_pawns(side)
        assert pawns_positions == expected
   
  
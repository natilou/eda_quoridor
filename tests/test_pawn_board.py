import pytest
from test_scenarios import *
from bot.bot import PawnBoard

class TestBoardPawn:
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
        )
    ])
    
    def test_get_pawns(self, board, side, expected):
        pawn_board = PawnBoard(board)
        pawns_positions = pawn_board.get_pawns(side)
        assert pawns_positions == expected
   
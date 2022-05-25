from bot.board.visual_board import VisualBoard
from bot.board.board_expert_pawns import BoardExpertPawns
from bot.domains.move import Move
from bot.constants import MOVE_TYPE_PAWN
from test_scenarios import *
import pytest

class TestBoardExpertPawns():
    @pytest.mark.parametrize("board,side,expected", [
        (
            SCENARIO_WITHOUT_S_PAWNS,
            "S", 
            []
        ),
        (
            SCENARIO_WITH_BOTH_PAWNS, 
            "N",
            [
                Move(type=MOVE_TYPE_PAWN, from_cell=(0,6), to_cell=(1,6)),
                Move(type=MOVE_TYPE_PAWN, from_cell=(3,3), to_cell=(4,3)),
                Move(type=MOVE_TYPE_PAWN, from_cell=(6,4), to_cell=(7,4)),
            ]
        ),
        (
            SCENARIO_WITH_BOTH_PAWNS,
            "S", 
            [
                Move(type=MOVE_TYPE_PAWN, from_cell=(5,3), to_cell=(4,3)),
                Move(type=MOVE_TYPE_PAWN, from_cell=(6,6), to_cell=(5,6)),
                Move(type=MOVE_TYPE_PAWN, from_cell=(8,4), to_cell=(7,4)),
            ]
        ), 
        (
            SCENARIO_WITHOUT_N_PAWNS, 
            "S",
            [
                Move(type=MOVE_TYPE_PAWN, from_cell=(1,1), to_cell=(0,1)),
                Move(type=MOVE_TYPE_PAWN, from_cell=(4,0), to_cell=(3,0)),
                Move(type=MOVE_TYPE_PAWN, from_cell=(4,4), to_cell=(3,4)),    
            ]
        ), 
        (
            SCENARIO_WITH_HORIZONTAL_WALLS,
           "S",
            [
                Move(type=MOVE_TYPE_PAWN, from_cell=(2,0), to_cell=(1,0)),
                Move(type=MOVE_TYPE_PAWN, from_cell=(6,7), to_cell=(5,7)),
                Move(type=MOVE_TYPE_PAWN, from_cell=(5,3), to_cell=(5,4)),
                Move(type=MOVE_TYPE_PAWN, from_cell=(5,3), to_cell=(5,2)),
                 
            ],
            
        ), 
        (
            SCENARIO_WITH_HORIZONTAL_WALLS,
           "N",
            [
                Move(type=MOVE_TYPE_PAWN, from_cell=(0,4), to_cell=(1,4)),
                Move(type=MOVE_TYPE_PAWN, from_cell=(2,8), to_cell=(3,8)),
                Move(type=MOVE_TYPE_PAWN, from_cell=(3,1), to_cell=(3,2)),
                Move(type=MOVE_TYPE_PAWN, from_cell=(3,1), to_cell=(3,0)),
            ],
        ), 
        (
            SCENARIO_WITH_VERTICAL_WALLS,
            "N",
            [
                Move(type=MOVE_TYPE_PAWN, from_cell=(1,2), to_cell=(2,2)),
                Move(type=MOVE_TYPE_PAWN, from_cell=(2,7), to_cell=(3,7)),
                Move(type=MOVE_TYPE_PAWN, from_cell=(3,4), to_cell=(4,4)),
            ], 
        ),
        (
            SCENARIO_WITH_VERTICAL_WALLS,
            "S",
            [
                Move(type=MOVE_TYPE_PAWN, from_cell=(2,1), to_cell=(1,1)),
                Move(type=MOVE_TYPE_PAWN, from_cell=(4,3), to_cell=(3,3)),
                Move(type=MOVE_TYPE_PAWN, from_cell=(7,6), to_cell=(6,6)),
            ], 
        ),  
        (
            SCENARIO_WITHOUT_WALLS2,
            "S",
            [
                Move(type=MOVE_TYPE_PAWN, from_cell=(1,1), to_cell=(0,1)),
                Move(type=MOVE_TYPE_PAWN, from_cell=(4,4), to_cell=(3,4)),
                Move(type=MOVE_TYPE_PAWN, from_cell=(7,2), to_cell=(5,2)) 
                
            ]
        )
    ])
    def test_check_available_moves(self, board, side, expected):
        board = VisualBoard(board)
        result = BoardExpertPawns.get_available_moves(board, side)
        assert result == expected
from bot.board.visual_board import VisualBoard
from bot.board.board_expert import BoardExpert
from bot.domains.move import Move
from bot.constants import MOVE_TYPE_PAWN, MOVE_TYPE_WALL
from test_scenarios import *
import pytest

class TestBoardExpert():
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
                Move(type=MOVE_TYPE_PAWN, from_cell=(4,0), to_cell=(4, 1)), # TODO: piensa que hay una pared horizontal, y es vertical
                Move(type=MOVE_TYPE_PAWN, from_cell=(4,4), to_cell=(3,4)),
                #Move(type=MOVE_TYPE_PAWN, from_cell=(4,0), to_cell=(3,0)), # TODO: Hay una pared vertical, pero no le impide moverse hacia delante, ver cómo solucionarlo
            ]
        ), 
        (
            SCENARIO_WITH_HORIZONTAL_WALLS,
           "S",
            [
                Move(type=MOVE_TYPE_PAWN, from_cell=(2,0), to_cell=(1,0)),
                Move(type=MOVE_TYPE_PAWN, from_cell=(5,3), to_cell=(5,4)),
                Move(type=MOVE_TYPE_PAWN, from_cell=(5,3), to_cell=(5,2)),
                Move(type=MOVE_TYPE_PAWN, from_cell=(6,7), to_cell=(5,7)),
                
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
        # TODO: corregir lógica para que no confunda paredes verticales con horizontales
        # (
        #     SCENARIO_WITH_VERTICAL_WALLS,
        #     "N", 
        #     {
        #         "my_pawns": [(1,2), (2,7), (3,4)], 
        #         "oponent_pawns": [(2,1), (4,3), (7,6)], 
        #         "walls": [
        #             ((1,4), (2,4)), 
        #             ((2,1), (3,1)), 
        #             ((3,3), (4,3)), 
        #             ((4,7), (5,7)), 
        #             ((5,0), (6,0)), 
        #             ((5,3), (6,3)), 
        #             ((5,5), (6,5)), 
        #             ((6,2), (7,2))
        #         ],
        #     }
        # ),  
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
        result = BoardExpert.check_available_moves(board, side)
        assert result == expected


    @pytest.mark.parametrize("board,side,expected", [
        (
            SCENARIO_WITHOUT_S_PAWNS,
            "S", 
            [
                Move(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(4,0)),
                Move(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(4,4)),
            ]
        ),
        (
            SCENARIO_WITHOUT_S_PAWNS,
            "N", 
            []
        ),
        (
            SCENARIO_WITH_BOTH_PAWNS, 
            "N",
            [
                Move(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(5,3)),
                Move(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(6,6)),
                Move(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(8,4)),
            ]
        ),
        (
            SCENARIO_WITH_BOTH_PAWNS,
            "S", 
            [
                Move(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(0,6)),
                Move(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(3,3)),
                Move(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(6,4)),
            ]
        ), 
        (
            SCENARIO_WITHOUT_N_PAWNS, 
            "S",
            []
        ), 
        (
            SCENARIO_WITH_HORIZONTAL_WALLS,
           "S",
            [
                Move(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(0,4)),
                Move(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(2,8)),              
            ]            
        ), 
        (
            SCENARIO_WITH_HORIZONTAL_WALLS,
           "N",
            [
                Move(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(1,0)),
                Move(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(4,3)),
                Move(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(5,7)),
                Move(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(2,0)),
               
            ],
        ), 
        # TODO: corregir lógica para que no confunda paredes verticales con horizontales
        # (
        #     SCENARIO_WITH_VERTICAL_WALLS,
        #     "N", 
        #     {
        #         "my_pawns": [(1,2), (2,7), (3,4)], 
        #         "oponent_pawns": [(2,1), (4,3), (7,6)], 
        #         "walls": [
        #             ((1,4), (2,4)), 
        #             ((2,1), (3,1)), 
        #             ((3,3), (4,3)), 
        #             ((4,7), (5,7)), 
        #             ((5,0), (6,0)), 
        #             ((5,3), (6,3)), 
        #             ((5,5), (6,5)), 
        #             ((6,2), (7,2))
        #         ],
        #     }
        # ),  
       
    ])
    def test_slots_close_to_opposing_pawns(self, board, side, expected):
        board = VisualBoard(board)
        result = BoardExpert.slots_close_to_opposing_pawns(board, side)
        assert result == expected
    
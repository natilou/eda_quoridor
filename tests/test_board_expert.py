from bot.board.visual_board import VisualBoard
from bot.board.board_expert import BoardExpert
from test_scenarios import *
import pytest

class TestBoardExpert():
    @pytest.mark.parametrize("board,side,expected", [
        # (
        #     SCENARIO_WITHOUT_S_PAWNS,
        #     "S", 
        #     {
        #         "my_pawns": [], 
        #         "oponent_pawns": [(1,1), (4,0), (4,4)], 
        #         "walls": [
        #             ((1,1), (1,2)), 
        #             ((2,0), (3,0))
        #         ],
        #     }
            
        # ),
        # (
        #     SCENARIO_WITH_BOTH_PAWNS, 
        #     "N",
        #     {
        #         "my_pawns": [(0,6), (3,3), (6,4)], 
        #         "oponent_pawns": [(5,3), (6,6), (8,4)], 
        #         "walls": [
        #             ((1,1), (1,2)), 
        #             ((2,0), (3,0))
        #         ],
        #     }
        # ), 
        # (
        #     SCENARIO_WITHOUT_N_PAWNS, 
        #     "S",
        #     {
        #         "my_pawns": [(1,1), (4,0), (4,4)], 
        #         "oponent_pawns": [], 
        #         "walls": [
        #             ((1,1), (1,2)), 
        #             ((2,0), (3,0))
        #         ],
        #     }
        # ), 
        # (
        #     SCENARIO_WITH_HORIZONTAL_WALLS,
        #    "S",
        #     {
        #         "my_pawns": [(2,0), (5,3), (6,7)], 
        #         "oponent_pawns": [(0,4),(2,8), (3,1)], 
        #         "walls": [
        #             ((1,3), (1,4)), 
        #             ((1,6), (1,7)),
        #             ((3, 1), (3, 2)),
        #             ((3, 5), (3, 6)), 
        #             ((4, 3), (4, 4)), 
        #             ((5, 1), (5, 2)), 
        #             ((5, 5), (5, 6)), 
        #             ((6, 0), (6, 1))
        #         ],
        #     }
        # ), 
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
            SCENARIO_WITH_BOTH_WALLS,
            "N", 
            {
                "pawn": {
                    (1,3): {},
                    (4,6): {
                        "move-forward": (5,6)
                        }, 
                    (5,4): {},
                }, 
                "opponent_pawns": [(2,0), (4,2), (7,7)],
                "block_advance": [(1,0), (6,7)],  
                "forbidden_cells": [
                    (4, 6),
                    ((1, 4), (2, 4)),
                    ((1, 2), (1, 3)),
                    ((1, 6), (1, 7)),
                    ((3, 3), (4, 3)),
                    ((3, 1), (3, 2)),
                    ((4, 7), (5, 7)),
                    ((5, 0), (6, 0)),
                    ((5, 5), (6, 5)),
                    ((5, 3), (5, 4)),
                    ((6, 2), (6, 3))
                ],
            }
        ), 
        (
            SCENARIO_WITHOUT_WALLS2,
            "S", 
             {
                "pawn": {
                    (1,1): {
                        "move-forward": (0,1)
                    }, 
                    (7,2): {
                        "front-jump": (5,2)
                    }, 
                    (4,4): {
                        "move-forward": (3, 4)
                    }
                }, 
                "opponent_pawns": [(2,4), (6,2), (7,6)],
                "block_advance": [(2,4), (6,2), (7,6)], 
                "forbidden_cells": [(1,1), (4,4)],
            }
        )
    ])

    def test_check_available_actions(self, board, side, expected):
        board = VisualBoard(board)
        dict = BoardExpert.check_available_moves(board, side)
        assert dict == expected
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
        )
    ])

    def test_convert_wall_positions(self, board, expected):
        wall_board = VisualBoard(board)
        wall_positions = wall_board.get_walls_positions()
        converted_positions = AdapterBoard.convert_wall_positions(wall_positions)
        assert converted_positions == expected


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
    ])
    
    def test_convert_pawn_positions(self, board, side, expected):
        pawn_board = VisualBoard(board)
        pawn_positions = pawn_board.get_my_pawns(side)
        convert_positions = AdapterBoard.convert_pawn_positions(pawn_positions)
        assert convert_positions == expected

    

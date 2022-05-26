from bot.board.visual_board import VisualBoard
from bot.board.board_expert_walls import BoardExpertWalls, WallMove
from bot.domains.wall_move import WallMove
from bot.constants import MOVE_TYPE_WALL
from test_scenarios import *
import pytest

class TestBoardExpertWalls():

    @pytest.mark.parametrize("board,side,expected", [
        (  
            SCENARIO_WITHOUT_S_PAWNS,  
            "S", 
            [
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(1,0), orientation="h"),
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(1,0), orientation="v"),
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(4,0), orientation="h"),
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(4,0), orientation="v"),
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(4,4), orientation="h"),
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(4,4), orientation="v"),
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(4,3), orientation="h"),
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(4,3), orientation="v"),
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
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(4,3), orientation="h"),
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(4,3), orientation="v"),
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(4,2), orientation="h"),
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(4,2), orientation="v"),
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(5,6), orientation="h"),
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(5,6), orientation="v"),
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(5,5), orientation="h"),
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(5,5), orientation="v"),
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(7,4), orientation="h"),
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(7,4), orientation="v"),
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(7,3), orientation="h"),
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(7,3), orientation="v"),
            ]
        ),
        (
            SCENARIO_WITH_BOTH_PAWNS,
            "S",
            [
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(0,6), orientation="h"),
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(0,6), orientation="v"),
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(0,5), orientation="h"),
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(0,5), orientation="v"),
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(3,3), orientation="h"), 
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(3,3), orientation="v"),
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(3,2), orientation="h"), 
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(3,2), orientation="v"),  
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(6,4), orientation="h"),
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(6,4), orientation="v"),
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(6,3), orientation="h"),
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(6,3), orientation="v"),
                 
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
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(0,4), orientation="h"),
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(0,4), orientation="v"),
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(0,3), orientation="h"),
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(0,3), orientation="v"),   
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(2,7), orientation="h"),
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(2,7), orientation="v"),
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(3,0), orientation="h"),
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(3,0), orientation="v"),
                                
            ]            
        ), 
        (
            SCENARIO_WITH_HORIZONTAL_WALLS,
            "N",
            [
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(1,0), orientation="h"),
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(1,0), orientation="v"),  
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(4,2), orientation="h"),
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(4,2), orientation="v"),
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(5,7), orientation="h"),
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(5,7), orientation="v"),           
            ],
        ),
        (
            SCENARIO_WITH_VERTICAL_WALLS,
            "N",
            [   
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(1,1), orientation="h"),
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(1,1), orientation="v"),
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(1,0), orientation="h"),
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(1,0), orientation="v"),
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(3,2), orientation="h"),
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(3,2), orientation="v"),
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(6,6), orientation="h"),
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(6,6), orientation="v"),        
            ],
        ), 
        (
            SCENARIO_RANDOM, 
            "S", 
            [
                WallMove(type='wall', from_cell=(), to_cell=(0, 7), orientation='h'),
                WallMove(type='wall', from_cell=(), to_cell=(0, 7), orientation='v'),
                WallMove(type='wall', from_cell=(), to_cell=(0, 6), orientation='h'),
                WallMove(type='wall', from_cell=(), to_cell=(0, 6), orientation='v'),
                WallMove(type='wall', from_cell=(), to_cell=(0, 7), orientation='h'),
                WallMove(type='wall', from_cell=(), to_cell=(0, 7), orientation='v'),
                WallMove(type='wall', from_cell=(), to_cell=(1, 2), orientation='h'),
                WallMove(type='wall', from_cell=(), to_cell=(1, 2), orientation='v'),
                WallMove(type='wall', from_cell=(), to_cell=(1, 1), orientation='h'),
                WallMove(type='wall', from_cell=(), to_cell=(1, 1), orientation='v'),
            ]
        ),
        (
            SCENARIO_RANDOM, 
            "N", 
            [
                WallMove(type='wall', from_cell=(), to_cell=(0, 3), orientation='h'),
                WallMove(type='wall', from_cell=(), to_cell=(0, 3), orientation='v'),
                WallMove(type='wall', from_cell=(), to_cell=(0, 2), orientation='h'),
                WallMove(type='wall', from_cell=(), to_cell=(0, 2), orientation='v'),
                WallMove(type='wall', from_cell=(), to_cell=(0, 7), orientation='h'),
                WallMove(type='wall', from_cell=(), to_cell=(0, 7), orientation='v'),
                WallMove(type='wall', from_cell=(), to_cell=(0, 6), orientation='h'),
                WallMove(type='wall', from_cell=(), to_cell=(0, 6), orientation='v'),
                WallMove(type='wall', from_cell=(), to_cell=(2, 7), orientation='h'),
                WallMove(type='wall', from_cell=(), to_cell=(2, 7), orientation='v'),
                WallMove(type='wall', from_cell=(), to_cell=(2, 6), orientation='h'),
                WallMove(type='wall', from_cell=(), to_cell=(2, 6), orientation='v'),
            ]
        ), 
        (
            SCENARIO_MIDDLE_WALLS, 
            "S", 
            [
                WallMove(type='wall', from_cell=(), to_cell=(0, 1), orientation='h'),
                WallMove(type='wall', from_cell=(), to_cell=(0, 1), orientation='v'),
                WallMove(type='wall', from_cell=(), to_cell=(0, 0), orientation='h'),
                WallMove(type='wall', from_cell=(), to_cell=(0, 0), orientation='v'),
            ]
        ), 
        (
            SCENARIO_MIDDLE_WALLS, 
            "N", 
            [
                WallMove(type='wall', from_cell=(), to_cell=(4, 3), orientation='h'),
                WallMove(type='wall', from_cell=(), to_cell=(4, 3), orientation='v'),
                WallMove(type='wall', from_cell=(), to_cell=(4, 2), orientation='h'),
                WallMove(type='wall', from_cell=(), to_cell=(4, 2), orientation='v'),
                WallMove(type='wall', from_cell=(), to_cell=(6, 2), orientation='h'),
                WallMove(type='wall', from_cell=(), to_cell=(6, 2), orientation='v'),
                WallMove(type='wall', from_cell=(), to_cell=(6, 1), orientation='h'),
                WallMove(type='wall', from_cell=(), to_cell=(6, 1), orientation='v'),
            ]
        ) 
    ])
    def test_get_available_cells(self, board, side, expected):
        board = VisualBoard(board)
        result = BoardExpertWalls.get_available_slots(board, side)
        assert result == expected
    

    @pytest.mark.parametrize("board,side,expected", [
        (
            SCENARIO_WITHOUT_S_PAWNS,
            "S", 
            [
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(1,1), orientation="h"),
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(1,1), orientation="v"),
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(1,0), orientation="h"),
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(1,0), orientation="v"),
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(4,0), orientation="h"), 
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(4,0), orientation="v"), 
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(4,4), orientation="h"),
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(4,4), orientation="v"),
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(4,3), orientation="h"),
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(4,3), orientation="v"),
            ]
        ),
        (
            SCENARIO_WITH_BOTH_PAWNS, 
            "N",
            [
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(4,3), orientation="h"),
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(4,3), orientation="v"),
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(4,2), orientation="h"),
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(4,2), orientation="v"),
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(5,6), orientation="h"),
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(5,6), orientation="v"),
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(5,5), orientation="h"),
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(5,5), orientation="v"),
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(7,4), orientation="h"),
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(7,4), orientation="v"),
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(7,3), orientation="h"),
                WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(7,3), orientation="v"),
            ]
        ),
        (
            SCENARIO_WITH_BOTH_PAWNS,
            "S", 
            [
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(0,6), orientation="h"),
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(0,6), orientation="v"),
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(0,5), orientation="h"),
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(0,5), orientation="v"),
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(3,3), orientation="h"), 
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(3,3), orientation="v"), 
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(3,2), orientation="h"),
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(3,2), orientation="v"),
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(6,4), orientation="h"),
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(6,4), orientation="v"),
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(6,3), orientation="h"),
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(6,3), orientation="v"),
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
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(0,4), orientation="h"),
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(0,4), orientation="v"),
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(0,3), orientation="h"),
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(0,3), orientation="v"),
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(2,7), orientation="h"),
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(2,7), orientation="v"),
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(3,1), orientation="h"),
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(3,1), orientation="v"),
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(3,0), orientation="h"),
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(3,0), orientation="v"),
            ]           
        ), 
        (
            SCENARIO_WITH_HORIZONTAL_WALLS,
           "N",
            [
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(1,0), orientation="h"),
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(1,0), orientation="v"),
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(4,3), orientation="h"), 
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(4,3), orientation="v"), 
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(4,2), orientation="h"),
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(4,2), orientation="v"),
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(5,7), orientation="h"),
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(5,7), orientation="v"),
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(5,6), orientation="h"),
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(5,6), orientation="v"),
            ]  
        ),
        (
            SCENARIO_WITH_VERTICAL_WALLS,
            "N",
            [
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(1,1), orientation="h"),
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(1,1), orientation="v"),
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(1,0), orientation="h"),
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(1,0), orientation="v"),
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(3,3), orientation="h"), 
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(3,3), orientation="v"), 
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(3,2), orientation="h"),
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(3,2), orientation="v"),
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(6,6), orientation="h"),
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(6,6), orientation="v"),
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(6,5), orientation="h"),
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(6,5), orientation="v"),
            ]  
        ),
        (
            SCENARIO_WITH_VERTICAL_WALLS,
            "S",
            [
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(1,2), orientation="h"),
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(1,2), orientation="v"),
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(1,1), orientation="h"),
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(1,1), orientation="v"),
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(2,7), orientation="h"), 
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(2,7), orientation="v"), 
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(2,6), orientation="h"),
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(2,6), orientation="v"),
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(3,4), orientation="h"),
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(3,4), orientation="v"),
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(3,3), orientation="h"),
               WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(3,3), orientation="v"),
            ]  
        ), 
        (
            SCENARIO_RANDOM, 
            "S", 
            [
                WallMove(type='wall', from_cell=(), to_cell=(0, 7), orientation='h'),
                WallMove(type='wall', from_cell=(), to_cell=(0, 7), orientation='v'),
                WallMove(type='wall', from_cell=(), to_cell=(0, 6), orientation='h'),
                WallMove(type='wall', from_cell=(), to_cell=(0, 6), orientation='v'),
                WallMove(type='wall', from_cell=(), to_cell=(0, 7), orientation='h'),
                WallMove(type='wall', from_cell=(), to_cell=(0, 7), orientation='v'),
                WallMove(type='wall', from_cell=(), to_cell=(1, 2), orientation='h'),
                WallMove(type='wall', from_cell=(), to_cell=(1, 2), orientation='v'),
                WallMove(type='wall', from_cell=(), to_cell=(1, 1), orientation='h'),
                WallMove(type='wall', from_cell=(), to_cell=(1, 1), orientation='v'),
            ]
        ), 
        (
            SCENARIO_MIDDLE_WALLS, 
            "S", 
            [
                WallMove(type='wall', from_cell=(), to_cell=(0, 1), orientation='h'),
                WallMove(type='wall', from_cell=(), to_cell=(0, 1), orientation='v'),
                WallMove(type='wall', from_cell=(), to_cell=(0, 0), orientation='h'),
                WallMove(type='wall', from_cell=(), to_cell=(0, 0), orientation='v'),
                WallMove(type='wall', from_cell=(), to_cell=(1, 3), orientation='h'),
                WallMove(type='wall', from_cell=(), to_cell=(1, 3), orientation='v'),
                WallMove(type='wall', from_cell=(), to_cell=(1, 2), orientation='h'),
                WallMove(type='wall', from_cell=(), to_cell=(1, 2), orientation='v'),
                WallMove(type='wall', from_cell=(), to_cell=(3, 7), orientation='h'),
                WallMove(type='wall', from_cell=(), to_cell=(3, 7), orientation='v'),
                WallMove(type='wall', from_cell=(), to_cell=(3, 6), orientation='h'),
                WallMove(type='wall', from_cell=(), to_cell=(3, 6), orientation='v'), 
            ]
        ), 
        (
            SCENARIO_MIDDLE_WALLS, 
            "N", 
            [
                WallMove(type='wall', from_cell=(), to_cell=(3, 7), orientation='h'),
                WallMove(type='wall', from_cell=(), to_cell=(3, 7), orientation='v'),
                WallMove(type='wall', from_cell=(), to_cell=(4, 3), orientation='h'),
                WallMove(type='wall', from_cell=(), to_cell=(4, 3), orientation='v'),
                WallMove(type='wall', from_cell=(), to_cell=(4, 2), orientation='h'),
                WallMove(type='wall', from_cell=(), to_cell=(4, 2), orientation='v'),
                WallMove(type='wall', from_cell=(), to_cell=(6, 2), orientation='h'),
                WallMove(type='wall', from_cell=(), to_cell=(6, 2), orientation='v'),
                WallMove(type='wall', from_cell=(), to_cell=(6, 1), orientation='h'),
                WallMove(type='wall', from_cell=(), to_cell=(6, 1), orientation='v'),
            ]
        )

    ])   
    def test_possible_cells_to_block(self, board, side, expected):
        board = VisualBoard(board)
        result = BoardExpertWalls.possible_cells_to_block(board, side)
        assert result == expected   
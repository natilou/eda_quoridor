from bot.strategies.move_advanced_pawn import MoveAdvancedPawn
from bot.strategies.block_nearby_pawn import BlockNearbyPawn
from bot.domains.wall_move import WallMove
from bot.domains.move import Move
from bot.constants import MOVE_TYPE_WALL, MOVE_TYPE_PAWN
from test_scenarios import *
import pytest

class TestMovePawn:
    @pytest.mark.parametrize("board,walls,side,expected", [
        (
            SCENARIO_WITHOUT_S_PAWNS,
            10,
            "S",
            WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(4,3), orientation="h")
        ), 
        (
            SCENARIO_WITH_BOTH_PAWNS, 
            5,
            "N",
            WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(4,3), orientation="h")
        ),
        (
            SCENARIO_WITH_BOTH_PAWNS,
            10,
            "S",
            WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(6,3), orientation="h")
        ), 
        (
            SCENARIO_WITHOUT_N_PAWNS, 
            1,
            "N", 
            WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(0,1), orientation="h")
        ), 
        (
            SCENARIO_WITH_HORIZONTAL_WALLS,
            3,
            "S",
            WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(3,0), orientation="h"),
        ), 
        (
            SCENARIO_WITH_HORIZONTAL_WALLS,
            7,
            "N",
            WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(1,0), orientation="h"),
        ), 
        (
            SCENARIO_WITH_VERTICAL_WALLS,
            9,
            "N",
            WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(1,1), orientation="h"),
        ),
        (
            SCENARIO_WITH_VERTICAL_WALLS,
            10,
            "S",
            WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(3, 4), orientation='h')
        ),  
        (
            SCENARIO_WITHOUT_WALLS2,
            1,
            "S",
            WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(7, 5), orientation='h')
        ), 
        (
            SCENARIO_RANDOM, 
            10, 
            "S",
            WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(1, 1), orientation='h')
        ),
        ( 
            SCENARIO_RANDOM, 
            10, 
            "N",
            WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(0, 3), orientation='h')
        ), 
        (
            SCENARIO_MIDDLE_WALLS, 
            10, 
            "N",
            WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(4, 3), orientation='h')
        ), 
        (
            SCENARIO_MIDDLE_WALLS, 
            10, 
            "S",
            Move(type=MOVE_TYPE_PAWN, from_cell=(4, 8), to_cell=(3, 8))
        ), 
        (
            SCENARIO_RANDOM2, 
            5, 
            "S",
            Move(type=MOVE_TYPE_PAWN, from_cell=(4, 3), to_cell=(3, 3))
        )
    ])
    @pytest.mark.asyncio
    async def test_perform_an_action(self, board, walls, side, expected):
        request_data = {
            "data": {
                "board": board, 
                "side": side, 
                "walls": walls,
                "remaining_moves": 50
            }
        }
        move_advanced_pawn = MoveAdvancedPawn()
        put_wall = BlockNearbyPawn()
        put_wall.set_next(move_advanced_pawn)
        move = await put_wall.perform_an_action(request_data)
        assert move == expected
   
import pytest
from test_scenarios import *
from bot.strategies.move_pawn_random import MovePawnRandom
from bot.strategies.put_wall_random import PutWallRandom
from bot.domains.wall_move import WallMove
from bot.constants import MOVE_TYPE_WALL

class TestMovePawn:
    @pytest.mark.parametrize("board,walls,side,expected", [
        (
            SCENARIO_WITHOUT_S_PAWNS,
            10,
            "S",
            WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(4, 3), orientation='h')
        ),
        (
            SCENARIO_WITHOUT_S_PAWNS,
            3,
            "S",
            WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(4, 3), orientation='h')
        ), 
        (
            SCENARIO_WITH_BOTH_PAWNS, 
            5,
            "N",
            WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(5, 5), orientation='h')
        ),
        (
            SCENARIO_WITH_BOTH_PAWNS,
            10,
            "S",
            WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(3, 2), orientation='h')
        ), 
        (
            SCENARIO_WITHOUT_N_PAWNS, 
            1,
            "N", 
            WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(3, 3), orientation="h")
        ), 
        (
            SCENARIO_WITH_HORIZONTAL_WALLS,
            3,
            "S",
            WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(2, 7), orientation='h')
            
        ), 
        (
            SCENARIO_WITH_HORIZONTAL_WALLS,
            7,
            "N",
            WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(4, 2), orientation='v')
        ), 
        (
            SCENARIO_WITH_VERTICAL_WALLS,
            9,
            "N",
            WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(6, 6), orientation='h')
        ),
        (
            SCENARIO_WITH_VERTICAL_WALLS,
            10,
            "S",
            WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(2, 6), orientation='h')
        ),  
        (
            SCENARIO_WITHOUT_WALLS2,
            1,
            "S",
            WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(6, 1), orientation='h')
        )
    ])
    @pytest.mark.asyncio
    async def test_perform_an_action(self, board, walls, side, expected, random_seed):
        request_data = {
            "data": {
                "board": board, 
                "side": side, 
                "walls": walls,
            }
        }
        move_pawn_random = MovePawnRandom()
        put_wall_random = PutWallRandom()
        put_wall_random.set_next(move_pawn_random)
        move = await put_wall_random.perform_an_action(request_data)
        assert move == expected
   
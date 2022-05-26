from bot.strategies.move_advanced_pawn import MoveAdvancedPawn
from bot.strategies.put_wall_random import PutWallRandom
from bot.domains.move import Move
from bot.constants import MOVE_TYPE_PAWN
import pytest
from test_scenarios import *

class TestMovePawn:
    @pytest.mark.parametrize("board,moves,side,expected", [
        (
            SCENARIO_WITHOUT_S_PAWNS,
            100,
            "N",
            Move(type=MOVE_TYPE_PAWN, from_cell=(4, 4), to_cell=(5, 4))
        ),
        (
            SCENARIO_WITHOUT_S_PAWNS,
            50,
            "N",
            Move(type=MOVE_TYPE_PAWN, from_cell=(4, 4), to_cell=(5, 4))
        ), 
        (
            SCENARIO_WITH_BOTH_PAWNS, 
            100,
            "N",
            Move(type=MOVE_TYPE_PAWN, from_cell=(6,4), to_cell=(7,4))
        ),
        (
            SCENARIO_WITH_BOTH_PAWNS,
            2,
            "S",
            Move(type=MOVE_TYPE_PAWN, from_cell=(5,3), to_cell=(4,3))
        ), 
        (
            SCENARIO_WITHOUT_N_PAWNS, 
            45,
            "S",
             Move(type=MOVE_TYPE_PAWN, from_cell=(1,1), to_cell=(0,1))
        ), 
        (
            SCENARIO_WITH_HORIZONTAL_WALLS,
            3,
            "S",
            Move(type=MOVE_TYPE_PAWN, from_cell=(2,0), to_cell=(1,0))          
        ), 
        (
            SCENARIO_WITH_HORIZONTAL_WALLS,
            1,
            "N",
            Move(type=MOVE_TYPE_PAWN, from_cell=(3,1), to_cell=(3,0)),
        ), 
        (
            SCENARIO_WITH_VERTICAL_WALLS,
            35,
            "N",
            Move(type=MOVE_TYPE_PAWN, from_cell=(3,4), to_cell=(4,4))
        ),
        (
            SCENARIO_WITH_VERTICAL_WALLS,
            2,
            "S",
            Move(type=MOVE_TYPE_PAWN, from_cell=(2,1), to_cell=(1,1))
        ),  
        (
            SCENARIO_WITHOUT_WALLS2,
            105,
            "S",
            Move(type=MOVE_TYPE_PAWN, from_cell=(1,1), to_cell=(0,1))
        ), 
        (
            SCENARIO_RANDOM, 
            9, 
            "S",
             Move(type=MOVE_TYPE_PAWN, from_cell=(1, 3), to_cell=(0, 3))
        ),
        (
            SCENARIO_RANDOM, 
            1, 
            "N",
            Move(type=MOVE_TYPE_PAWN, from_cell=(1, 2), to_cell=(2, 2))
        ),
        (
            SCENARIO_MIDDLE_WALLS, 
            9, 
            "N",
            Move(type=MOVE_TYPE_PAWN, from_cell=(3, 7), to_cell=(3, 6))
        ),
        (
            SCENARIO_MIDDLE_WALLS, 
            9, 
            "S",
            Move(type=MOVE_TYPE_PAWN, from_cell=(4, 8), to_cell=(3, 8))
        )
    ])
    @pytest.mark.asyncio
    async def test_perform_an_action(self, board, moves, side, expected):
        request_data = {
            "data": {
                "board": board, 
                "side": side, 
                "remaining_moves": moves,
            }
        }
        put_wall_random = PutWallRandom()
        move_advanced_pawn = MoveAdvancedPawn()
        move_advanced_pawn.set_next(put_wall_random)
        move = await move_advanced_pawn.perform_an_action(request_data)
        assert move == expected
   
from bot.constants import MOVE_TYPE_PAWN, MOVE_TYPE_WALL
from bot.game import Game
from bot.domains.wall_move import WallMove
from bot.domains.wall_move import Move
from bot.adapters.websocket_client import WebsocketClient
from bot.strategies.move_advanced_pawn import MoveAdvancedPawn
from bot.strategies.move_pawn_random import MovePawnRandom
from bot.strategies.front_jump import FrontJump
from bot.strategies.put_wall_random import PutWallRandom
from bot.strategies.block_nearby_pawn import BlockNearbyPawn
from test_scenarios import *
import pytest

class TestGame:
    @pytest.mark.parametrize("board,side,moves,walls,expected",[
        (
            SCENARIO_WITHOUT_S_PAWNS,
            "S",
            50, 
            10,
            WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(4,3), orientation="h")
        ), 
        (
            SCENARIO_WITHOUT_WALLS2,
            "S",
            105,
            10,             
            Move(type=MOVE_TYPE_PAWN, from_cell=(7,2), to_cell=(5,2))
        ), 
        (
            SCENARIO_WITH_BOTH_PAWNS, 
            "N",
            100,
            0,           
            Move(type=MOVE_TYPE_PAWN, from_cell=(6,4), to_cell=(7,4))
        ), 
        ( 
            SCENARIO_RANDOM, 
            "N",
            50,
            10, 
            Move(type=MOVE_TYPE_PAWN, from_cell=(0,7), to_cell=(2,7))
        ), 
        (
            SCENARIO_WITH_VERTICAL_WALLS,
            "S",
            10,
            8,
            WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(3, 4), orientation='h')
        ), 
        (
            SCENARIO_WITH_HORIZONTAL_WALLS,
            "S",
            3,
            0,
            Move(type=MOVE_TYPE_PAWN, from_cell=(2,0), to_cell=(1,0)) 
        )
    ])
    @pytest.mark.asyncio
    async def test_play_turn(self, board, side, moves, walls, expected):
        # request_data
        request_data = {
            "data":{
                "side": side, 
                "board": board,
                "remaining_moves": moves,
                "walls": walls,
            }
        }

        # strategies initialization 
        front_jump = FrontJump()
        block_nearby_pawn = BlockNearbyPawn()
        move_advanced_pawn = MoveAdvancedPawn()
        move_pawn_random = MovePawnRandom()
        put_wall_random = PutWallRandom()

        # assign chain of responsibility
        front_jump.set_next(block_nearby_pawn)
        block_nearby_pawn.set_next(move_advanced_pawn)
        move_advanced_pawn.set_next(move_pawn_random)
        move_pawn_random.set_next(put_wall_random)
        move = await front_jump.perform_an_action(request_data)
        assert Game.show_move(move) == expected

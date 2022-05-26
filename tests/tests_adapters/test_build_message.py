from bot.constants import MOVE_TYPE_PAWN, MOVE_TYPE_WALL
from bot.adapters.websocket_client import WebsocketClient
from bot.domains.move import Move
from bot.domains.wall_move import WallMove
from test_scenarios import *
import pytest

class TestWebSocketClient:
    @pytest.mark.parametrize("move,expected", [
        (
            Move(type=MOVE_TYPE_PAWN, from_cell=(5,3), to_cell=(4,3)),
            {
                "action": MOVE_TYPE_PAWN, 
                "data": {
                "game_id": "c5151748-dd09-11ec-aef0-7ecdf393f9cc",
                "turn_token": "12767c12-5484-4fdb-843f-6192bb65aa65",
                'from_row': 5,
                'from_col': 3,
                'to_row':  4,
                'to_col':  3,
                }
            } 
        ), 
        (
            Move(type=MOVE_TYPE_PAWN, from_cell=(3, 7), to_cell=(3, 8)),
            {
                "action": MOVE_TYPE_PAWN, 
                "data": {
                "game_id": "c5151748-dd09-11ec-aef0-7ecdf393f9cc",
                "turn_token": "12767c12-5484-4fdb-843f-6192bb65aa65",
                'from_row': 3,
                'from_col': 7,
                'to_row':  3,
                'to_col':  8,
                }
            } 
        ), 
        (
            Move(type=MOVE_TYPE_PAWN, from_cell=(7,2), to_cell=(5,2)),
            {
                "action": MOVE_TYPE_PAWN, 
                "data": {
                "game_id": "c5151748-dd09-11ec-aef0-7ecdf393f9cc",
                "turn_token": "12767c12-5484-4fdb-843f-6192bb65aa65",
                'from_row': 7,
                'from_col': 2,
                'to_row':  5,
                'to_col':  2,
                }
            } 
        ), 
        (
            WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(4, 3), orientation='h'),
            {
                "action": MOVE_TYPE_WALL, 
                "data": {
                "game_id": "c5151748-dd09-11ec-aef0-7ecdf393f9cc",
                "turn_token": "12767c12-5484-4fdb-843f-6192bb65aa65",
                'row': 4, 
                'col': 3, 
                'orientation':"h"
                }
            } 
        ), 
        (
            WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(4, 2), orientation='v'),
            {
                "action": MOVE_TYPE_WALL, 
                "data": {
                "game_id": "c5151748-dd09-11ec-aef0-7ecdf393f9cc",
                "turn_token": "12767c12-5484-4fdb-843f-6192bb65aa65",
                'row': 4, 
                'col': 2, 
                'orientation':"v"
                }
            } 
        ), 
        (
            WallMove(type=MOVE_TYPE_WALL, from_cell=(), to_cell=(0,1), orientation="h"),
            {
                "action": MOVE_TYPE_WALL, 
                "data": {
                "game_id": "c5151748-dd09-11ec-aef0-7ecdf393f9cc",
                "turn_token": "12767c12-5484-4fdb-843f-6192bb65aa65",
                'row': 0, 
                'col': 1, 
                'orientation':"h"
                }
            } 
        )

    ])
    def test_build_message(self, move, expected):
        request_data = {
            "data":{
                "game_id": "c5151748-dd09-11ec-aef0-7ecdf393f9cc",
                "turn_token": "12767c12-5484-4fdb-843f-6192bb65aa65"
            }
        }
        message = WebsocketClient.build_message(move, request_data)
        assert message == expected

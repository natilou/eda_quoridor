from bot.constants import MOVE_TYPE_PAWN, MOVE_TYPE_WALL
from adapters.client import Client
import json


class WebsocketClient(Client):

    def __init__(self, client):
        self.client = client

    async def send(self, action, data):
        message = json.dumps(
            {
                'action': action, 
                'data': data
            }
        )
        print(f'Sending message: {message}')
        await self.client.send(message)
    
    async def send_message(self, request_data, move):

        if move.type == MOVE_TYPE_PAWN:
            action = move.type
            data = {
                    'game_id': request_data['data']['game_id'], 
                    'turn_token': request_data['data']['turn_token'], 
                    'from_row': move.from_cell[0],
                    'from_col':  move.from_cell[1],
                    'to_row':  move.to_cell[0],
                    'to_col':  move.to_cell[1],
            }

        elif move.type == MOVE_TYPE_WALL:
            action = move.type 
            data = {
                'game_id': request_data['data']['game_id'],
                'turn_token': request_data['data']['turn_token'], 
                'row': move.to_cell[0], 
                'col': move.to_cell[1], 
                'orientation': move.orientation
            }

        else:
            raise Exception("Invalid message type")
        
        await self.send(action, data)

    async def receive_request(self):
        return await self.client.recv()

            


            
    
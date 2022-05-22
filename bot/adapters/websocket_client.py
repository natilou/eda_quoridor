from constants import MOVE_TYPE_PAWN, MOVE_TYPE_WALL
from bot.adapters.client import Client
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
    
    async def send_message(self, request_data, message):

        if message.type == MOVE_TYPE_PAWN:
            action = message.type
            data = {
                    'game_id': request_data['data']['game_id'], 
                    'turn_token': request_data['data']['turn_token'], 
                    'from_row': message.from_cells[0],
                    'from_col':  message.from_cells[1],
                    'to_row':  message.to_cells[0],
                    'to_col':  message.to_cells[1],
            }

        elif message.type == MOVE_TYPE_WALL:
            action = message.type 
            data = {
                'game_id': request_data['data']['game_id'],
                'turn_token': request_data['data']['turn_token'], 
                'row': message.to_cells[0], 
                'col': message.to_cells[1], 
                'orientation': 'h'
            }

        else:
            raise Exception("Invalid message type")
        
        await self.send(action, data)

    async def receive_request(self):
        return await self.client.recv()

            


            
    
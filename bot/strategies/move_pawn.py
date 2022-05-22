from bot.board.board_expert import BoardExpert
from strategies.strategy import Strategy
from bot.adapters.websocket_client import WebsocketClient
from board.visual_board import VisualBoard
import random

# Concrete Strategy
class MovePawn(Strategy):
    @staticmethod
    async def perform_an_action(request_data):
        side = request_data['data']['side']

        # normalizar tablero
        board = VisualBoard(request_data['data']['board'])
   
        # buscar actiones posibles 
        available_actions = BoardExpert.check_available_moves(board, side)
        
        available_pawns = []

        for pawn, value in available_actions.items():
            if "move-forward" in available_actions[pawn] or "front-jump" in available_actions[pawn] or "diagonal-jump" in available_actions[pawn]:
                available_pawns.append({"pawn": pawn, "actions": available_actions[pawn]})
        
        selected_pawn = ""
        if not available_actions:
            super().get_next_strategy().perform_an_action(request_data)
        else:        
            # elegir uno de los tres peones:
            selected_pawn = random.choice(available_pawns)
                  
            # ver dónde estoy
            pawn_actual_row = selected_pawn["pawn"][0] 
            pawn_actual_col = selected_pawn["pawn"][1]

            # ver dónde moverse
            move_to_col = ""
            move_to_row = ""
            
            
            if "frontal-jump" in selected_pawn["actions"]:
                move_to_row = selected_pawn["actions"]["frontal-jump"][0]
                move_to_col = selected_pawn["actions"]["frontal-jump"][1]

            elif "move-forward" in selected_pawn["actions"]:
                move_to_row = selected_pawn["actions"]["move-forward"][0]
                move_to_col = selected_pawn["actions"]["move-forward"][1]
           
            elif "diagonal-jump" in selected_pawn["actions"]:
                move_to_row = selected_pawn["actions"]["diagonal-jump"][0]
                move_to_col = selected_pawn["actions"]["diagonal-jump"][1]


    
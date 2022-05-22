import os

# Constants
URL = f"wss://4yyity02md.execute-api.us-east-1.amazonaws.com/ws?token={os.getenv('auth_token')}"
VISUAL_BOARD_DIMENSION = 17
SQUARE_DIMENSION = 9
SLOT_DIMENSION = 8
MOVE_TYPE_PAWN = "move"
MOVE_TYPE_WALL = "wall"


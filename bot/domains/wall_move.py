from dataclasses import dataclass
from bot.domains.move import Move 

@dataclass(frozen=True)
class WallMove(Move):
    orientation: str

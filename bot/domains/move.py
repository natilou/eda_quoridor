from dataclasses import dataclass

@dataclass(frozen=True)
class Move():
    type: str
    from_cell: tuple
    to_cell: tuple
    


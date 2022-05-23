from dataclasses import dataclass

@dataclass
class Move():
    type: str
    from_cell: tuple[int, int]
    to_cell: tuple[int, int]
    


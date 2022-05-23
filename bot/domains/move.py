from dataclasses import dataclass

@dataclass
class Move():
    type: str
    from_cell: tuple
    to_cell: tuple
    


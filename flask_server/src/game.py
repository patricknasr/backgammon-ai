from dataclasses import dataclass, field
from .errors import InvalidColour
import random
import enum

MIN_POINT_POS = 0
MAX_POINT_POS = 26

class Piece(enum.Enum):
    LIGHT = 1
    DARK = 2

@dataclass
class Point:
    pieces: list[Piece] = field(default_factory=list)

@dataclass
class Board:
    points: list[Point] = field(default_factory=list)

def roll_dice() -> int:
        return random.randint(1, 6)

class BoardView:
    def __init__(self):
        self._board = Board(points=[Point() for _ in range(26)])

        self._board.points[1].pieces = [Piece.LIGHT for _ in range(15)]

        self._board.points[24].pieces = [Piece.DARK for _ in range(15)]
    
    def move_piece(self, colour: Piece, original_position: int, move_by: int):
        if colour == Piece.LIGHT:
            new_position = min(original_position+move_by, MAX_POINT_POS)
        elif colour == Piece.DARK:
            new_position = max(original_position-move_by, 0)
        else:
            raise InvalidColour
        
        self._board.points[original_position].pieces.remove(colour)
        self._board.points[new_position].pieces.remove(colour)
    
    def has_game_been_won(self) -> bool:
        if (len(self._board.points[0].pieces) or len(self._board.points[26].pieces)) == 15:
            return True
        
        return False
    
    def can_capture_opponent(self, attacking_piece_type: Piece, point_position: int) -> bool:
        if len(self._board.points[point_position].pieces) == 1 and self._board.points[point_position].pieces[0] is not attacking_piece_type:
            return True
        
        return False

def main():
    initialise_board = BoardView()

if __name__ == "__main__":
    main()
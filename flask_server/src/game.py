from dataclasses import dataclass, field
# from .errors import InvalidColour, NegativePiecesCountAtPoint
import random
import enum

MIN_POINT_POS = 0
MAX_POINT_POS = 25

class Piece(enum.Enum):
    LIGHT = 1
    DARK = 2

@dataclass
class Point:
    pieces: list[Piece] = field(default_factory=list)

@dataclass
class Board:
    points: list[Point] = field(default_factory=list)
    
class BoardView:
    def __init__(self):
        self._board = Board(points=[Point() for _ in range(26)])

        self._board.points[1].pieces = [Piece.LIGHT for _ in range(15)]

        self._board.points[24].pieces = [Piece.DARK for _ in range(15)]
    
    def move_piece(self, move_colour: Piece, original_position: int, move_by: int) -> bool:
        if move_colour == Piece.LIGHT:
            new_position = min(original_position+move_by, MAX_POINT_POS)
        elif move_colour == Piece.DARK:
            new_position = max(original_position-move_by, 0)
        else:
            # raise InvalidColour
            return False
        
        self._board.points[original_position].pieces.remove(move_colour)
        self._board.points[new_position].pieces.append(move_colour)

        return True

def roll_dice() -> tuple[int, int]:
        return (random.randint(1, 6), random.randint(1, 6))

def computer_piece_type(player_piece_type: Piece) -> Piece:
        if player_piece_type == Piece.LIGHT:
            return Piece.DARK
        elif player_piece_type == Piece.DARK:
            return Piece.LIGHT
        else:
            # raise InvalidColour
            pass
        
def has_game_been_won(board_view: BoardView) -> bool:
    if len(board_view._board.points[MIN_POINT_POS].pieces) == 15 or len(board_view._board.points[MAX_POINT_POS].pieces) == 15:
        return True
    
    return False

def point_is_empty(board_view: BoardView, point_index: int) -> bool:
    if len(board_view._board.points[point_index].pieces) == 0:
        return True
    elif len(board_view._board.points[point_index].pieces) > 0:
        return False
    else:
        # raise NegativePiecesCountAtPoint
        pass

def can_place_on_point(board_view: BoardView, player_piece_type: Piece, point_index: int) -> bool:
    if board_view.point_is_empty(point_index) or \
        len(board_view._board.points[point_index].pieces) == 1 \
            or board_view._board.points[point_index].pieces[0] is not computer_piece_type(player_piece_type):
            # something about being in bounds \
        return True

    return False


def print_board_to_cli(board_view: BoardView):
        print("\n")
        for idx, point in enumerate(board_view._board.points):
            light_count = point.pieces.count(Piece.LIGHT)
            dark_count = point.pieces.count(Piece.DARK)

            pieces_str = ""
            if light_count > 0:
                pieces_str += f"(L - {light_count}) "
            if dark_count > 0:
                pieces_str += f"(D - {dark_count})"

            print(f"{idx:02d}: {pieces_str.strip()}")

def main():
    initialise_board = BoardView()
    print_board_to_cli(initialise_board)
    (die_a, die_b) = roll_dice()
    initialise_board.move_piece(move_colour=Piece.LIGHT, original_position=1, move_by=die_a)
    initialise_board.move_piece(move_colour=Piece.LIGHT, original_position=1, move_by=die_b)
    print_board_to_cli(initialise_board)
    (die_a, die_b) = roll_dice()
    initialise_board.move_piece(move_colour=Piece.DARK, original_position=24, move_by=die_a)
    initialise_board.move_piece(move_colour=Piece.DARK, original_position=24, move_by=die_b)
    print_board_to_cli(initialise_board)
    (die_a, die_b) = roll_dice()
    initialise_board.move_piece(move_colour=Piece.LIGHT, original_position=1, move_by=die_a)
    initialise_board.move_piece(move_colour=Piece.LIGHT, original_position=1, move_by=die_b)
    print_board_to_cli(initialise_board)
    (die_a, die_b) = roll_dice()
    initialise_board.move_piece(move_colour=Piece.DARK, original_position=24, move_by=die_a)
    initialise_board.move_piece(move_colour=Piece.DARK, original_position=24, move_by=die_b)
    print_board_to_cli(initialise_board)

if __name__ == "__main__":
    main()
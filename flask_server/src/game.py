from dataclasses import dataclass, field
# from .errors import InvalidColour, NegativePiecesCountAtPoint, TooManyPiecesCountAtPoint
import random
import enum

UNINITIALISED = -1 
MIN_POINT_POS = 0
MAX_POINT_POS = 25
HOME_QUARTER_SIZE_MIN = 7
HOME_QUARTER_SIZE_MAX = 18
NUM_OF_PIECES = 15
NUM_OF_POINTS = 24

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
        self._board = Board(points=[Point() for _ in range(NUM_OF_POINTS + 2)])

        self._board.points[1].pieces = [Piece.LIGHT for _ in range(NUM_OF_PIECES)]

        self._board.points[24].pieces = [Piece.DARK for _ in range(NUM_OF_PIECES)]
    
    # if no viable moves just return true
    def move_piece(self, move_colour: Piece, original_position: int, move_by: int) -> bool:
        new_position = UNINITIALISED
        if move_colour == Piece.LIGHT:
            new_position = min(original_position+move_by, MAX_POINT_POS)
            if min(original_position+move_by, MAX_POINT_POS) == MAX_POINT_POS:
                if all_pieces_in_last_quarter(self, move_colour) is False:
                    return False
                elif original_position+move_by > MAX_POINT_POS and piece_can_be_removed_from_board(self, move_colour, move_by) is False:
                    return False
        elif move_colour == Piece.DARK:
            new_position = max(original_position-move_by, MIN_POINT_POS)
            if max(original_position-move_by, MIN_POINT_POS) == MIN_POINT_POS:
                if all_pieces_in_last_quarter(self, move_colour) is False:
                    return False
                elif original_position-move_by < MAX_POINT_POS and piece_can_be_removed_from_board(self, move_colour, move_by) is False:
                    return False
        else:
            # raise InvalidColour
            return False

        if new_position < MIN_POINT_POS or new_position > MAX_POINT_POS:
            return False
        
   
        # all the pieces are in home but there a
        
        self._board.points[original_position].pieces.remove(move_colour)
        self._board.points[new_position].pieces.append(move_colour)

        return True


def roll_dice() -> tuple[int, int]:
        return (random.randint(1, 6), random.randint(1, 6))


def piece_can_be_removed_from_board(board_view: Board, piece_type: Piece, move_by: int):
    # or you cant be able to move pieces that will land on original_position+move_by == MAX_POINT_POS -1
    count = 0
    if piece_type == Piece.LIGHT:
        point = MAX_POINT_POS - move_by
        if board_view.points[point].pieces.count(piece_type) >= 1:
             return False
        for point_index in range(MAX_POINT_POS, HOME_QUARTER_SIZE_MAX, -1):
            if board_view.points[point_index].pieces.count(piece_type) >= 1:
                 return False
                     
    elif piece_type == Piece.DARK:
        point = MIN_POINT_POS + move_by
        if board_view.points[point].pieces.count(piece_type) >= 1:
             return False
        for point_index in range(MIN_POINT_POS, HOME_QUARTER_SIZE_MIN):
            if board_view.points[point_index].pieces.count(piece_type) >= 1:
                 return False
    
    return True


def all_pieces_in_last_quarter(board_view: BoardView, piece_type: Piece) -> bool:
    count = 0
    if piece_type == Piece.LIGHT:
        for point_index in range(MAX_POINT_POS, HOME_QUARTER_SIZE_MAX, -1):
                count += board_view.points[point_index].pieces.count(piece_type)
    elif piece_type == Piece.DARK:
        for point_index in range(MIN_POINT_POS, HOME_QUARTER_SIZE_MIN):
                count += board_view.points[point_index].pieces.count(piece_type)
    else:
        # raise InvalidColour
        return False
    
    if count is not 15:
        return False
    else:
        return True


def has_game_been_won(board_view: BoardView) -> bool:
    if number_of_pieces_on_point(board_view, MIN_POINT_POS) == 15 or number_of_pieces_on_point(board_view, MAX_POINT_POS):
        return True

    return False


def opposite_piece_type(piece_type: Piece) -> Piece:
        if piece_type == Piece.LIGHT:
            return Piece.DARK
        elif piece_type == Piece.DARK:
            return Piece.LIGHT
        else:
            # raise InvalidColour
            return Piece.DARK
        

def number_of_pieces_on_point(board_view: BoardView, point_index: int) -> int:
    pieces_count = len(board_view._board.points[point_index].pieces)

    if pieces_count < 0:
        # raise NegativePiecesCountAtPoint
        return 0
    elif pieces_count > 16:
        # raise TooManyPiecesCountAtPoint
        return 0
    else:
        return pieces_count


def get_first_piece(board_view: BoardView, point_index: int):
    return board_view._board.points[point_index].pieces[0] 


def can_place_on_point(board_view: BoardView, move_piece_type: Piece, point_index: int) -> bool:
    if number_of_pieces_on_point(board_view, point_index) == 0 or \
       number_of_pieces_on_point(board_view, point_index) == 1 or \
       get_first_piece(board_view, point_index) is not opposite_piece_type(move_piece_type):
        return True

    return False


def print_board_to_cli(board_view: BoardView):
        print("\n")
        for idx, point in enumerate(board_view._board.points):
            light_count = point.pieces.count(Piece.LIGHT)
            dark_count = point.pieces.count(Piece.DARK)

            pieces_str = ""
            if light_count > 0:
                pieces_str += f"(L - {light_count})"
            if dark_count > 0:
                pieces_str += f"(D - {dark_count})"

            print(f"{idx:02d}: {pieces_str.strip()}")


def main():
    game_over = False

    # while game_over == False:
    #     pass 

    initialise_board = BoardView()
    print_board_to_cli(initialise_board)
    (die_a, die_b) = roll_dice()
    initialise_board.move_piece(move_colour=Piece.LIGHT, original_position=1, move_by=die_a)
    game_over = has_game_been_won(initialise_board)
    initialise_board.move_piece(move_colour=Piece.LIGHT, original_position=1, move_by=die_b)
    game_over = has_game_been_won(initialise_board)
    print_board_to_cli(initialise_board)
    (die_a, die_b) = roll_dice()
    initialise_board.move_piece(move_colour=Piece.DARK, original_position=24, move_by=die_a)
    game_over = has_game_been_won(initialise_board)
    initialise_board.move_piece(move_colour=Piece.DARK, original_position=24, move_by=die_b)
    game_over = has_game_been_won(initialise_board)
    print_board_to_cli(initialise_board)
    (die_a, die_b) = roll_dice()
    initialise_board.move_piece(move_colour=Piece.LIGHT, original_position=1, move_by=die_a)
    game_over = has_game_been_won(initialise_board)
    initialise_board.move_piece(move_colour=Piece.LIGHT, original_position=1, move_by=die_b)
    game_over = has_game_been_won(initialise_board)
    print_board_to_cli(initialise_board)
    (die_a, die_b) = roll_dice()
    initialise_board.move_piece(move_colour=Piece.DARK, original_position=24, move_by=die_a)
    game_over = has_game_been_won(initialise_board)
    initialise_board.move_piece(move_colour=Piece.DARK, original_position=24, move_by=die_b)
    game_over = has_game_been_won(initialise_board)
    print_board_to_cli(initialise_board)

if __name__ == "__main__":
    main()
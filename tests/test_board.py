from game.board import Board


def test_display_board():
    board = Board()
    print("\n")
    board.print_board()


def test_display_heuristics_board():
    print("\n")
    board = Board()
    board.print_board()
    print("\n")
    print(board.heuristics_board(0, 1))


def test_heuristics_board():
    print("\n")
    board = Board()
    board.print_board()
    print("\n")
    print(board.heuristics_board(0, 0))
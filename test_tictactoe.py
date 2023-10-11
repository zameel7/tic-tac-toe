from tictactoe import choose_first, space_check, full_board_check, marker_position

# unit tests for the code implemented

def test_full_board_check():
    assert not full_board_check([" "]*10)

def test_choose_first():
    assert choose_first("X") == "Player 1"
    assert choose_first("O") == "Player 2"

def test_space_check():
    assert space_check([" "] * 10, 3)

def test_marker_position():
    assert marker_position(2)
    assert not marker_position(12)

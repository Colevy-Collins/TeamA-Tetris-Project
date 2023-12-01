import random
import pytest
from src.TetrisBlock import TetrisBlock

@pytest.fixture
def tetris_block():
    return TetrisBlock()

def test_TetrisBlock_init(tetris_block):
    assert tetris_block.current_figure_type == 0
    assert tetris_block.current_figure_color == 0
    assert tetris_block.current_rotation == 0
    assert tetris_block.shift_in_x == 0
    assert tetris_block.shift_in_y == 0
    assert isinstance(tetris_block.colors, tuple)
    assert isinstance(tetris_block.Figures, tuple)
    
def test_create_figure(tetris_block):
    starting_shift_x = 3
    starting_shift_y = 2
    tetris_block.create_figure(starting_shift_x, starting_shift_y)
    assert tetris_block.shift_in_x == starting_shift_x
    assert tetris_block.shift_in_y == starting_shift_y
    assert 0 <= tetris_block.current_figure_type < len(tetris_block.Figures)
    assert 1 <= tetris_block.current_figure_color < len(tetris_block.colors)
    assert tetris_block.current_rotation == 0
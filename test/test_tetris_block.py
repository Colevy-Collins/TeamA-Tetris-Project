import sys
import os

# Add the parent directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.RandomDelegate import RandomDelegate
from src.TetrisBlock import TetrisBlock

def test_create_figure():
    random = RandomDelegate()
    block = TetrisBlock()
    block.create_figure(1, 2)
    assert block.get_current_figure_type() >= 0
    assert block.get_current_figure_type() < len(block.Figures)
    assert block.get_current_figure_color() >= 1
    assert block.get_current_figure_color() < len(block.colors)
    assert block.get_current_rotation() == 0

def test_shift_in_x():
    block = TetrisBlock()
    block.set_shift_in_x(5)
    assert block.get_shift_in_x() == 5

def test_shift_in_y():
    block = TetrisBlock()
    block.set_shift_in_y(3)
    assert block.get_shift_in_y() == 3

def test_current_rotation():
    block = TetrisBlock()
    block.set_current_rotation(2)
    assert block.get_current_rotation() == 2

def test_get_shape():
    block = TetrisBlock()
    block.create_figure(1, 2)
    current_shape = block.get_shape()
    assert current_shape in block.Figures[block.get_current_figure_type()]

def test_colors():
    block = TetrisBlock()
    colors = block.get_colors()
    assert len(colors) == len(block.colors)


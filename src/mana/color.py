
from enum import Enum


class Color(Enum):
    """Mana colors."""

    WHITE = 1
    BLUE = 2
    BLACK = 3
    RED = 4
    GREEN = 5
    COLORLESS = 6

ALL_COLORS = set(Color)

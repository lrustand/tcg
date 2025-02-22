
from dataclasses import dataclass

from .game import Game


@dataclass
class MagicTheGathering(Game):
    """Magic the Gathering."""
    hand_size: int = 7
    players: int = 2


@dataclass
class Commander(MagicTheGathering):
    """Commander format."""
    players: int = 4

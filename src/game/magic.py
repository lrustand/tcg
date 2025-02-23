"""Definition of the Magic: the Gathering game type, and formats."""

from dataclasses import dataclass
import math

from zone.zones import CommandZone
from .game import GameType, ValueRange


@dataclass
class MagicTheGathering(GameType):
    """Magic the Gathering."""
    life_total = 20
    hand_size = ValueRange(0, 7)
    deck_size = ValueRange(60, math.inf)
    players = ValueRange(2, 2)


@dataclass
class Commander(MagicTheGathering):
    """Commander format."""
    life_total = 40
    deck_size = ValueRange(100, 100)
    players = ValueRange(2, 6)

    def __post_init__(self) -> None:
        self.zones += CommandZone


@dataclass
class Standard(MagicTheGathering):
    """Standard format."""

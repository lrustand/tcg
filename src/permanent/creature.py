
from dataclasses import dataclass

from .permanent import Permanent


@dataclass
class Creature(Permanent):
    """Creature."""

    power: int = 0
    toughness: int = 0
    attacking: bool = False
    blocking: bool = False
    summoning_sick: bool = False

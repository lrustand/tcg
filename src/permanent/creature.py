
from dataclasses import dataclass

from .permanent import Permanent


@dataclass
class Creature(Permanent):
    """Creature."""

    power: int = 0
    toughness: int = 0

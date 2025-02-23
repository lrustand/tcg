
from dataclasses import dataclass

from .creature import Creature
from card.legendary import Legendary


@dataclass
class Commander(Spell, Permanent):
    """Commander."""

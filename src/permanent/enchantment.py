
from dataclasses import dataclass

from .permanent import Permanent


@dataclass
class Enchantment(Permanent):
    """Enchantment."""


@dataclass
class Room(Enchantment):
    """Room enchantment."""

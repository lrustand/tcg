
from dataclasses import dataclass

from mana.color import Color
from.effect import Effect


@dataclass
class AddMana(Effect):
    """Add an amount of mana."""
    mana: dict[Color, int] = {}

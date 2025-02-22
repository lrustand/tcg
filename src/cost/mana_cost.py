
from dataclasses import dataclass

from mana.color import Color, ALL_COLORS
from .cost import Cost


@dataclass
class ManaCost(Cost):
    """Mana cost."""

    # The colors that can be used to pay this cost
    colors: set[Color] = ALL_COLORS

    @property
    def color_identity(self) -> set[Color]:
        """Calculate color identity."""
        return set(self.colors)

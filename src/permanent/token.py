
from mana.color import Color
from .permanent import Permanent


class Token(Permanent):
    """Token."""

    # Explicitly specified colors (create a blue and white detective token...)
    colors: set[Color]

    @property
    def color_identity(self) -> set[Color]:
        """Override color_identity."""
        super.color_identity.update(self.colors)

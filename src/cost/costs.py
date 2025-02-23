
from dataclasses import dataclass
from typing import Any

from action.action import Action
from mana.color import Color, ALL_COLORS
from .cost import Cost


@dataclass
class ManaCost(Cost):
    """Mana cost."""

    # The colors that can be used to pay this cost
    colors: set[Color] = Any

    @property
    def color_identity(self) -> set[Color]:
        """Calculate color identity."""
        return set(self.colors)


@dataclass
class ActionCost(Cost):
    """Cost that requires a game action to be performed."""

    action: Action  # The action that is required


@dataclass
class TapCost(Cost):
    """Tap card as part of cost."""

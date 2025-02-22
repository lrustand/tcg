
from dataclasses import dataclass

from .action import Action


@dataclass
class Draw(Action):
    """Draw card(s)."""

    cards: int  # Number of cards to draw

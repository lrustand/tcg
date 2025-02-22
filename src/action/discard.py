
from dataclasses import dataclass

from .action import Action


@dataclass
class Discard(Action):
    """Discard card(s)."""

    cards: int  # Number of cards to discard

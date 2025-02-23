
from dataclasses import dataclass, field
import random

from card.card import Card


@dataclass
class Zone:
    """Base class for all types of zones."""

    cards: list[Card] = field(default_factory=list)

    def select_card(self) -> Card:
        """Let player select a card in a zone."""
        card: Card = random.choice(self.cards)
        return card


@dataclass
class PlayerOwnedZone(Zone):
    """Zone owned by a player."""

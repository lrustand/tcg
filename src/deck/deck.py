
from dataclasses import dataclass, field
from typing import Type

from card.card import Card
from game.game import GameType
from game import magic


@dataclass
class Deck:
    """A deck of cards."""

    game: GameType = None
    cards: list[Card] | set[Card] = field(default_factory=list)

    def validate(self) -> bool:
        """Validate the deck."""

        # Right amount of cards
        if len(self.cards) != self.game.deck_size:
            return False

        # All cards are legal
        for card in self.cards:
            if self.game not in card.legality:
                return False

        return True


@dataclass
class CommanderDeck(Deck):
    """A commander deck."""
    game: GameType = magic.Commander
    cards: set[Type[Card]] = field(default_factory=set)

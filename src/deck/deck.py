
from dataclasses import dataclass

from card.card import Card
from game.game import Game
from game import magic


@dataclass
class Deck:
    """A deck of cards."""

    game: Game = None
    cards: list[Card] | set[Card] = []

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
    game: magic.Commander
    cards: set[Card] = set()

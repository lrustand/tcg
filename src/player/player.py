
from dataclasses import dataclass, field
import math
import random

from card.card import Card
from deck.deck import Deck
from permanent.permanent import Permanent
from zone import zones


@dataclass
class Player:
    """A player of the game."""
    life: int = math.inf
    deck: Deck = field(default_factory=Deck)
    library: zones.Library = field(default_factory=zones.Library)
    graveyard: zones.Graveyard = field(default_factory=zones.Graveyard)
    hand: zones.Hand = field(default_factory=zones.Hand)
    permanents: list[Permanent] = field(default_factory=list)

    def __post_init__(self) -> None:
        """Initialize library from deck."""
        self.library.cards=self.deck.cards.copy()
        random.shuffle(self.library.cards)

    def draw(self) -> None:
        """Draw a card from the top of the library and put it into the hand."""
        card: Card = self.library.cards.pop()
        self.hand.cards.append(card)

    def shuffle(self) -> None:
        """Shuffle the library."""
        random.shuffle(self.library.cards)

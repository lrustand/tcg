
from dataclasses import dataclass
from typing import Type

from card.card import Card
from permanent.token import Token
from zone import zones
from zone.zone import Zone
from .action import Action


@dataclass
class ZoneTransfer(Action):
    """Transfer card/permanent to another zone."""

    card: Card | None = None
    target_zone: Type[Zone] | Zone = None

    def resolve(self) -> None:
        card_class: Type[Card] = self.card.card_class

        from_zone = self.card.zone
        from_zone.remove(self.card)

        # Create a new instance of the card
        card = card_class()
        zones.get_zone(self.target_zone).append(card)


@dataclass
class Search(Action):
    """Search for card(s)."""

    # How many of each card type to find
    what: dict[Type[Card], int]
    from_zone: Zone
    target_zone: Zone

    def resolve(self) -> None:
        """Select the card(s), and transfer it to the target zone."""
        card: Card = self.from_zone.select_card()
        ZoneTransfer(performer=self.performer,
                     card=card,
                     target_zone=self.target_zone).resolve()
        super().resolve()


@dataclass
class CreateToken(Action):
    """Create token(s)."""

    amount: int = 1
    type: Type[Token]

    def resolve(self) -> None:
        """Create the tokens."""
        for _ in range(self.amount):
            token = self.type()
            self.performer.permanents.append(token)
        super().resolve()


@dataclass
class Destroy(Action):
    """Destroy permanent(s)."""


@dataclass
class Shuffle(Action):
    """Shuffle."""


@dataclass
class Sacrifice(Action):
    """Sacrifice permanent(s)."""


@dataclass
class Discard(ZoneTransfer):
    """Discard card(s)."""

    def __post_init__(self) -> None:
        self.from_zone = self.performer.hand
        self.target_zone = zones.Graveyard


@dataclass
class Draw(ZoneTransfer):
    """Draw card(s)."""

    def resolve(self) -> None:
        card: Card = self.performer.library.cards.pop()
        self.performer.hand.cards.append(card)

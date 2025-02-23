
from __future__ import annotations

from dataclasses import dataclass
from typing import Type
import urllib.parse

from game.game import Game
from player.player import Player
from .rarity import Rarity


@dataclass
class Card:
    """Base class for all cards."""
    name: str = None
    text: str = None
    flavor: str = None
    price: int = None
    rarity: Rarity = None
    legality: set[Game] = None
    owner: Player = None

    @property
    def url(self) -> str:
        """URL to the card info in Scryfall."""
        return f"https://scryfall.com/search?q={urllib.parse.quote_plus(self.name)}"

    @property
    def card_class(self) -> Type[Card]:
        """Get a reference to the original card class of the card."""
        return self.__class__


from dataclasses import dataclass
import urllib.parse

from game.game import Game
from .rarity import Rarity


@dataclass
class Card:
    """Base class for all cards."""
    name: str = None
    text: str = None
    flavor: str = None
    price: int = None
    rarity: Rarity = None
    legendary: bool = False
    legality: set[Game] = None

    @property
    def url(self) -> str:
        """URL to the card info in Scryfall."""
        return f"https://scryfall.com/search?q={urllib.parse.quote_plus(self.name)}"

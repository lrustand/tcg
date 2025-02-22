
from dataclasses import dataclass

from .card_type import CardType


@dataclass
class Selector:
    """Card selector class.

    Contains criteria for matching cards.
    """

    card_types: set[CardType] = set()
    classes: set[type] = set()

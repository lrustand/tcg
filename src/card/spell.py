
from dataclasses import dataclass
from typing import Union

from cost.cost import Cost
from .card import Card


@dataclass
class Spell(Card):
    """Base class for all spells."""

    cost: Union[Cost, list[Cost]] = None

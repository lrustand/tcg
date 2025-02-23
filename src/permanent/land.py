
from dataclasses import dataclass

from card.card import Card
from .permanent import Permanent
from .ability.abilities import ManaAbility
from .ability.ability import Ability


@dataclass
class Land(Card, Permanent):
    """A land."""


@dataclass
class BasicLand(Land):
    """Basic land."""

    def __init__(self, color: Color) -> None:
        self.abilities: list[ManaAbility] = ManaAbility(color)


@dataclass
class Plains(Land):
    """Plains."""


@dataclass
class Island(Land):
    """Island."""


@dataclass
class Swamp(Land):
    """Swamp."""


@dataclass
class Mountain(Land):
    """Mountain."""


@dataclass
class Forest(Land):
    """Forest."""


from dataclasses import dataclass

from cost.cost import Cost
from cost import costs
from mana.color import Color
from effect import effects
from effect.effect import Effect
from .ability import ActivatedAbility, KeywordAbility


@dataclass
class ManaAbility(ActivatedAbility):
    """Mana ability."""

    amount: dict[Color, int]
    cost: Cost = costs.TapCost()

    def __post_init__(self) -> None:
        self.effect: Effect = effects.AddMana(self.amount)


@dataclass
class Flying(KeywordAbility):
    """Flying ability."""


@dataclass
class Trample(KeywordAbility):
    """Trample ability."""


@dataclass
class Deathtouch(KeywordAbility):
    """Deathtouch ability."""


@dataclass
class Reach(KeywordAbility):
    """Reach ability."""


@dataclass
class Flash(KeywordAbility):
    """Flash ability."""


@dataclass
class Vigilance(KeywordAbility):
    """Vigilance ability."""


@dataclass
class Haste(KeywordAbility):
    """Haste ability."""


@dataclass
class Menace(KeywordAbility):
    """Menace ability."""


@dataclass
class Intimidate(KeywordAbility):
    """Intimidate ability."""


@dataclass
class Defender(KeywordAbility):
    """Defender ability."""


@dataclass
class FirstStrike(KeywordAbility):
    """First strike ability."""


@dataclass
class DoubleStrike(KeywordAbility):
    """Double strike ability."""

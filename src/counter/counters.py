
from dataclasses import dataclass

from permanent.ability.ability import KeywordAbility
from .counter import Counter


@dataclass
class PoisonCounter(Counter):
    """Poison counter."""
    poison: int


@dataclass
class CommanderDamage(Counter):
    """Commander damage."""
    commander: Commander
    damage: int


@dataclass
class PowerToughnessCounter(Counter):
    """Plus or minus power and toughness counter."""
    power: int
    toughness: int


@dataclass
class AbilityCounter(Counter):
    """Counter that adds an ability."""
    ability: KeywordAbility

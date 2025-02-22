
from dataclasses import dataclass

from .counter import Counter
from card.ability.ability import Ability


@dataclass
class AbilityCounter(Counter):
    """Counter that adds an ability."""
    ability: Ability

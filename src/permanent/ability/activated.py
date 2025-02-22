
from dataclasses import dataclass

from cost.cost import Cost
from effect.effect import Effect

from .ability import Ability


@dataclass
class ActivatedAbility(Ability):
    """An activated ability."""

    cost: Cost
    effect: Effect

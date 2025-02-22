
from dataclasses import dataclass

from action.action import Action
from effect.effect import Effect

from .ability import Ability


@dataclass
class TriggeredAbility(Ability):
    """A triggered ability."""

    triggers: list[Action]
    effect: Effect

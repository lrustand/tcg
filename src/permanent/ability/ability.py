"""Ability class and general subtypes of abilities."""

from dataclasses import dataclass, field
from typing import Type

from action.action import Action
from cost import costs
from cost.cost import Cost
from effect.effect import Effect
from phase.phase import Phase
from turn.turn import ALL_PHASES
from zone.zone import Zone
from zone.zones import Battlefield


@dataclass
class Ability:
    """Base class for all types of abilities."""

    # Zones where the ability can be activated/triggered/in effect
    active_zones: set[Type[Zone]] = field(default_factory=lambda : set([Battlefield]))
    active_phases: set[Type[Phase]] = field(default_factory=lambda : set(ALL_PHASES))
    effects: list[Effect] = field(default_factory=list)


@dataclass
class KeywordAbility(Ability):
    """Keyword ability."""


@dataclass
class ActivatedAbility(Ability):
    """Activated ability."""

    cost: list[Cost]

    @property
    def repeatable(self) -> bool:
        """Try to decide if the ability can be repeated multiple times."""
        for c in self.cost:
            if isinstance(c, costs.TapCost):
                return False
        return True

@dataclass
class StaticAbility(Ability):
    """Static ability."""


@dataclass
class TriggeredAbility(Ability):
    """Triggered ability."""
    trigger: Action | Effect

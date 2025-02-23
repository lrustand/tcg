
from dataclasses import dataclass, field
from typing import Type

from phase.phase import Phase
from phase import phases

ALL_PHASES: list[Type[Phase]] = [
        phases.BeginningPhase,
        phases.MainPhase,
        phases.CombatPhase,
        phases.MainPhase,
        phases.EndingPhase
    ]


@dataclass
class Turn:
    """A game turn."""

    @staticmethod
    def __init_phases__() -> list[Phase]:
        """Initialize turn phases."""
        return [phase() for phase in ALL_PHASES]

    phases: list[Phase] = field(default_factory=__init_phases__)

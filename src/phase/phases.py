
from dataclasses import dataclass, field

from .phase import Phase
from .step import Step


@dataclass
class BeginningPhase(Phase):
    """The beginning phase."""

    @staticmethod
    def __init_steps__() -> list[Step]:
        """Initialize phase steps."""

        @dataclass
        class Untap(Step):
            """Untap step."""

        @dataclass
        class Upkeep(Step):
            """Upkeep step."""

        @dataclass
        class Draw(Step):
            """Draw step."""

        return [
            Untap,
            Upkeep,
            Draw
        ]

    steps: list[Step] = field(default_factory=__init_steps__)

    def __post_init__(self) -> None:
        """Instantiate all steps."""
        self.steps = [s() for s in self.steps]


@dataclass
class MainPhase(Phase):
    """Main phase."""

    @staticmethod
    def __init_steps__() -> list[Step]:
        """Initialize phase steps."""

        @dataclass
        class MainPhaseStep(Step):
            """Main phase."""

        return [
            MainPhaseStep
        ]

    steps: list[Step] = field(default_factory=__init_steps__)

    def __post_init__(self) -> None:
        """Instantiate all steps."""
        self.steps = [s() for s in self.steps]


@dataclass
class CombatPhase(Phase):
    """Combat phase."""

    @staticmethod
    def __init_steps__() -> list[Step]:
        """Initialize phase steps."""

        @dataclass
        class BeginningOfCombat(Step):
            """Begininning of combat step."""

        @dataclass
        class DeclareAttackers(Step):
            """Declare attackers step."""

        @dataclass
        class DeclareBlockers(Step):
            """Declare blockers step."""

        @dataclass
        class CombatDamage(Step):
            """Combat damage step."""

        @dataclass
        class EndOfCombat(Step):
            """End of combat step."""

        return [
            BeginningOfCombat,
            DeclareAttackers,
            DeclareBlockers,
            CombatDamage,
            EndOfCombat
        ]

    steps: list[Step] = field(default_factory=__init_steps__)

    def __post_init__(self) -> None:
        """Instantiate all steps."""
        self.steps = [s() for s in self.steps]


@dataclass
class EndingPhase(Phase):
    """Ending phase."""

    @staticmethod
    def __init_steps__() -> list[Step]:
        """Initialize phase steps."""

        @dataclass
        class EndStep(Step):
            """End step."""

        @dataclass
        class CleanupStep(Step):
            """Cleanup step."""

        return [
            EndStep,
            CleanupStep
        ]

    steps: list[Step] = field(default_factory=__init_steps__)

    def __post_init__(self) -> None:
        """Instantiate all steps."""
        self.steps = [s() for s in self.steps]

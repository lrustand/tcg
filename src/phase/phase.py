
from dataclasses import dataclass, field

from .step import Step


@dataclass
class Phase:
    """Base class for game phases."""

    steps: list[Step] = field(default_factory=list)

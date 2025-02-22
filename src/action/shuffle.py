
from dataclasses import dataclass

from .action import Action


@dataclass
class Shuffle(Action):
    """Shuffle."""

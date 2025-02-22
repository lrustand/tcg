
from dataclasses import dataclass

from .action import Action


@dataclass
class Sacrifice(Action):
    """Sacrifice permanent(s)."""

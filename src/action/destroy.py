
from dataclasses import dataclass

from .action import Action


@dataclass
class Destroy(Action):
    """Destroy permanent(s)."""

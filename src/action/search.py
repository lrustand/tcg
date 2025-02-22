
from dataclasses import dataclass

from .action import Action


@dataclass
class Search(Action):
    """Search for card(s)."""

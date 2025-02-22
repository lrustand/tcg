
from dataclasses import dataclass

from .spell import Spell


@dataclass
class Instant(Spell):
    """Instant."""

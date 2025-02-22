
from dataclasses import dataclass

from .zone import Zone


@dataclass
class Battlefield(Zone):
    """The battlefield."""

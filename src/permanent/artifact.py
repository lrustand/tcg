
from dataclasses import dataclass

from .permanent import Permanent


@dataclass
class Artifact(Permanent):
    """Artifact."""

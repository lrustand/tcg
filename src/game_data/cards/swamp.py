
from dataclasses import dataclass

from permanent.land import BasicLand, Swamp


@dataclass
class BasicSwamp(BasicLand, Swamp):
    """Basic swamp."""

swamp = BasicSwamp()

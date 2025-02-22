
from dataclasses import dataclass

from permanent.land import BasicLand, Mountain


@dataclass
class BasicMountain(BasicLand, Mountain):
    """Basic mountain."""

mountain = BasicMountain()

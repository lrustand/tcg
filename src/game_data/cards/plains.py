
from dataclasses import dataclass

from permanent.land import BasicLand, Plains


@dataclass
class BasicPlains(BasicLand, Plains):
    """Basic plains."""

plains = BasicPlains()

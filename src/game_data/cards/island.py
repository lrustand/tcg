
from dataclasses import dataclass

from permanent.land import BasicLand, Island


@dataclass
class BasicIsland(BasicLand, Island):
    """Basic island."""

island = BasicIsland()

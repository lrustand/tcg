
from dataclasses import dataclass

from permanent.land import BasicLand, Forest


@dataclass
class BasicForest(BasicLand, Forest):
    """Basic forest."""

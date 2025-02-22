
from dataclasses import dataclass

from .counter import Counter


@dataclass
class PowerToughnessCounter(Counter):
    """Plus or minus power and toughness counter."""
    power: int
    toughness: int

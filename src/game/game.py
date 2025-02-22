
from dataclasses import dataclass

from phase.phase import Phase
from zone.zone import Zone


@dataclass
class Game:
    """A game."""
    hand_size: int = 0
    deck_size: int = 0
    card_duplicates: int = 1
    zones: list[Zone] = []
    games_phases: list[Phase] = []
    players: int = 0

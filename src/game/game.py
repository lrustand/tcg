
from dataclasses import dataclass, field

from phase.phase import Phase
from player.player import Player
from zone.zone import Zone


@dataclass
class ValueRange:
    """Class defining a valid value range."""
    min: int = None
    max: int = None

    def __post_init__(self) -> None:
        if self.min is None:
            self.min = 0
            self.max = 0
        elif self.max is None:
            self.max = self.min
            self.min = 0


@dataclass
class GameType:
    """A game type."""
    life_total: int = 0
    hand_size: ValueRange = ValueRange()
    deck_size: ValueRange = ValueRange()
    card_duplicates: ValueRange = ValueRange()
    players: ValueRange = ValueRange()
    zones: list[Zone] = field(default_factory=list)
    phases: list[Phase] = field(default_factory=list)


@dataclass
class Game:
    """A game."""

    game_type: GameType
    players: list[Player]

    def start(self) -> None:
        """Start the game."""

        for p in self.players:
            p.life = self.game_type.life_total

        for p in self.players:
            p.draw(self.game_type.hand_size.max)

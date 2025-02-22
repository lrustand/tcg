
from dataclasses import dataclass

from player.player import Player


@dataclass
class Action:
    """Base class for all game actions."""

    # The player that performs the action
    player: Player

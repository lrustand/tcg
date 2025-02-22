
from dataclasses import dataclass

from card.card import Card
import cost
from counter.counter import Counter
from mana.color import Color
from permanent.ability.ability import Ability
from player.player import Player
from zone.zone import Zone


@dataclass
class Permanent(Card):
    """Base class for all permanents."""

    owner: Player = None
    controller: Player = None
    zone: Zone = None
    tapped: bool = False
    counters: list[Counter] = []
    abilities: list[Ability] = []

    @property
    def color_identity(self) -> set[Color]:
        """Calculate color identity."""
        colors: set[Color] = set()

        # Colors from ability costs
        for a in self.abilities:
            if hasattr(a, "cost"):
                if isinstance(a.cost, cost.mana_cost.ManaCost):
                    colors_in_cost = set(a.cost.specific.keys())
                    colors.update(colors_in_cost)

        # Colors from casting cost
        if hasattr(self, "cost"):
            if isinstance(self.cost, cost.mana_cost.ManaCost):
                colors_in_cost = set(self.cost.specific.keys())
                colors.update(colors_in_cost)

        # TODO: Handle devoid, colored tokens, effects that change color of other permanents, etc.
        return colors

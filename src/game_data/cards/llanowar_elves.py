
from card.spell import Spell
from cost.costs import ManaCost
from mana.color import Color
from permanent.ability.abilities import ManaAbility
from permanent.creature import Creature


class LlanowarElves(Spell, Creature):
    """Llanowar Elves."""
    def __init__(self) -> None:
        Spell.__init__(self)
        Creature.__init__(self)
        self.name = "Llanowar Elves"
        self.cost = ManaCost(Color.GREEN)
        self.abilities = [ManaAbility]

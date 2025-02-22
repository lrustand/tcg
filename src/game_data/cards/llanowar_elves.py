
from mana.color import Color
from card.spell import Spell
from cost.mana_cost import ManaCost
from permanent.creature import Creature


#llanowar_elves = Creature(name="Llanowar Elves",
#                          cost=ManaCost(specific={Color.GREEN: 1}),


class LlanowarElves(Spell, Creature):
    """Llanowar Elves."""
    def __init__(self) -> None:
        Spell.__init__(self)
        Creature.__init__(self)
        self.name = "Llanowar Elves"


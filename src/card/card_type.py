"""Helper module, re-exporting all card types."""

from enum import Enum

from permanent.artifact import Artifact
from permanent.battle import Battle
from permanent.creature import Creature
from permanent.enchantment import Enchantment
from permanent.land import Land
from permanent.planeswalker import Planeswalker

from .instant import Instant
from .sorcery import Sorcery


class CardType(Enum):
    ARTIFACT = Artifact
    BATTLE = Battle
    CREATURE = Creature
    ENCHANTMENT = Enchantment
    INSTANT = Instant
    LAND = Land
    SORCERY = Sorcery
    PLANESWALKER = Planeswalker
    ANY = None

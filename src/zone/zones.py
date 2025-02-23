
from dataclasses import dataclass
from typing import Type

from .zone import Zone, PlayerOwnedZone


@dataclass
class Battlefield(Zone):
    """The battlefield."""


@dataclass
class Exile(Zone):
    """Exile."""


@dataclass
class Graveyard(PlayerOwnedZone):
    """Graveyard."""


@dataclass
class Hand(PlayerOwnedZone):
    """Hand."""


@dataclass
class Library(PlayerOwnedZone):
    """Library."""


@dataclass
class CommandZone(Zone):
    """Command zone."""


@dataclass
class Stack(Zone):
    """Stack."""


def get_zone(zone: Type[Zone]):
    if isinstance(zone, Type[PlayerOwnedZone]):
        pass

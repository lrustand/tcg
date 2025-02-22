
from dataclasses import dataclass

from zone.zone import Zone
from zone.battlefield import Battlefield


@dataclass
class Ability:
    """Base class for all types of abilities."""

    # Zones where the ability can be activated/triggered/static
    valid_zones: list[Zone] = [Battlefield]


from dataclasses import dataclass

from card.card import Card
from zone.zone import Zone
from .action import Action


@dataclass
class ZoneTransfer(Action):
    """Transfer card/permanent to another zone."""

    card: Card
    target_zone: Zone

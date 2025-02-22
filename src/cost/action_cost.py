
from dataclasses import dataclass

from action.action import Action
from .cost import Cost


@dataclass
class ActionCost(Cost):
    """Cost that requires a game action to be performed."""

    action: Action  # The action that is required

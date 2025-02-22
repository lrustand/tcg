
from dataclasses import dataclass

from permanent.token import Token
from .action import Action


@dataclass
class CreateToken(Action):
    """Create token(s)."""

    amount: int = 1
    token: Token


from dataclasses import dataclass

from .resource import Resource


@dataclass
class Life(Resource):
    """Life points."""

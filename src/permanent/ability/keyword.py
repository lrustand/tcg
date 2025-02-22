
from dataclasses import dataclass

from .ability import Ability


@dataclass
class KeywordAbility(Ability):
    """Keyword abilities."""


@dataclass
class Flying(KeywordAbility):
    """Flying."""


@dataclass
class Deathtouch(KeywordAbility):
    """Deathtouch."""


@dataclass
class Trample(KeywordAbility):
    """Trample."""


@dataclass
class Reach(KeywordAbility):
    """Reach."""


@dataclass
class Menace(KeywordAbility):
    """Menace."""


@dataclass
class Fear(KeywordAbility):
    """Fear."""


@dataclass
class Intimidate(KeywordAbility):
    """Intimidate."""


@dataclass
class Flash(KeywordAbility):
    """Flash."""


@dataclass
class Defender(KeywordAbility):
    """Defender."""

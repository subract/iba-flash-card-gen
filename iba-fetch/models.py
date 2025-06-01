from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Cocktail:
    name: str
    category: Optional[str] = None
    url: Optional[str] = None
    ingredients: List[str] = field(default_factory=list)
    method: List[str] = field(default_factory=list)
    garnish: Optional[str] = None
    video: Optional[str] = None

    def __str__(self):
        return f"{self.name} ({self.category}) - {self.url}"

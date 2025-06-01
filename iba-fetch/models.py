from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Cocktail:
    name: str
    category: Optional[str] = None
    url: Optional[str] = None
    ingredients: List[str] = field(default_factory=list)
    steps: List[str] = field(default_factory=list)
    garnish: Optional[str] = None
    video: Optional[str] = None

    def get_ingredients(self):
        if self.ingredients == []:
            return None
        return "- " + "\n- ".join(self.ingredients)

    def get_steps(self):
        if self.steps == []:
            return None
        return "- " + "\n- ".join(self.steps)

    def __str__(self):
        return f"{self.name} ({self.category})\n{self.get_ingredients()}\nSteps:\n{self.get_steps()}\n"

from .models import Cocktail

import string
from typing import List


def writeCocktails(cocktails: List[Cocktail], path: string):
    with open(path, "w", encoding="utf-8") as f:
        f.write("#separator:semicolon\n")
        f.write("#html:true\n")

        for cocktail in cocktails:
            f.write(f"{cocktail.get_card()}\n")

    f.close()

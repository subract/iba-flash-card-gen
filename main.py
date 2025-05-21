# import urllib2
from dataclasses import dataclass, field
from typing import List, Optional
from bs4 import BeautifulSoup

import IPython;


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

def main():
    page_number = 1
    iba_url = f"https://iba-world.com/cocktails/all-cocktails/page/${page_number}/"

    # For development, load a local example page instead of fetching it every time
    with open("example/page1.html") as page1:
        soup = BeautifulSoup(page1, 'html.parser')

    # page = urllib2.urlopen(iba_url)
    # soup = BeautifulSoup(page, 'html.parser')

    print(soup.title.string)

    cocktails = []

    cocktail_elems = soup(class_='cocktail')
    for cocktail_elem in cocktail_elems:
        # IPython.embed()

        name = cocktail_elem.h2.string
        cocktail = Cocktail(name)

        cocktail.category = cocktail_elem.find(class_="cocktail-category").get_text(strip=True)
        
        # For some reason, the text isn't in title case, despite being rendered
        # so on the web page using text-transform: capitalize
        # Let's make it title case ourselves
        cocktail.category = cocktail.category.title()

        cocktail.url = cocktail_elem.a.get('href')
        print(cocktail)


if __name__ == "__main__": main()

    # <div class="cocktail cocktail-203">
    #   <a href="https://iba-world.com/iba-cocktail/casino/">
    #     <picture>
    #       <img decoding="async" src="https://iba-world.com/wp-content/uploads/2024/07/iba-cocktail-the-unforgettables-casino-6694910882cd6.webp" alt=""/>
    #     </picture>
    #     <div class="cocktail-content">
    #       <h2>Casino</h2>
    #       <div class="content">
    #         <div class="cocktail-category"><i class="fa-solid fa-tag fa-flip-horizontal  fa-fw"></i> The unforgettables</div>
    #         <div class="cocktail-views"><i class="fa-regular fa-eye fa-fw"></i> 39.9K views</div>
    #       </div>
    #     </div>
    #   </a>
    # </div>
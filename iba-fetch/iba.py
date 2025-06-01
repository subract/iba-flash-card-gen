from .models import Cocktail

from bs4 import BeautifulSoup

import os

import IPython
import requests


def __get_cocktails_from_page(url):
    cocktails = []

    env = os.getenv("ENV", "production").lower()
    if env == "development":
        # For development, load a local example page instead of fetching it every time
        with open("example/page1.html") as page1:
            soup = BeautifulSoup(page1, "html.parser")
    else:
        page = requests.get(url, allow_redirects=True).content
        soup = BeautifulSoup(page, "html.parser")

    cocktail_divs = soup(class_="cocktail")

    for cocktail_div in cocktail_divs:
        name = cocktail_div.h2.string
        cocktail = Cocktail(name)

        cocktail.category = cocktail_div.find(class_="cocktail-category").get_text(
            strip=True
        )
        # For some reason, the text isn't in title case, despite being rendered
        # so on the web page using text-transform: capitalize
        cocktail.category = cocktail.category.title()
        cocktail.url = cocktail_div.a.get("href")
        cocktails.append(cocktail)
    return cocktails


def get_all_cocktails():
    page_number = 1
    iba_url = f"https://iba-world.com/cocktails/all-cocktails/page/{page_number}/"

    return __get_cocktails_from_page(iba_url)

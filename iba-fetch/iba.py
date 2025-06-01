import string
from .models import Cocktail

from bs4 import BeautifulSoup

import os

import IPython
import requests


def __get_cocktails_from_page(url: string):
    print(f"Fetching {url}")
    cocktails = []
    resp = requests.get(url, allow_redirects=True)
    if resp.status_code != 200:
        return None

    soup = BeautifulSoup(resp.content, "html.parser")

    cocktail_divs = soup(class_="cocktail")
    if cocktail_divs == []:
        return None

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


def __get_cocktail_details(cocktail: Cocktail):
    print(f"Fetching {cocktail.url}")
    resp = requests.get(cocktail.url, allow_redirects=True)
    soup = BeautifulSoup(resp.content, "html.parser")

    # Get ingredients
    ingredient_header = soup.find("h4", string="Ingredients")
    ingredient_list = ingredient_header.find_next("ul")
    for ingredient in ingredient_list.find_all("li"):
        cocktail.ingredients.append(ingredient.get_text(strip=True))

    # Get methods (steps to make)
    method_header = soup.find("h4", string="Method")
    method_list = method_header.find_next("div", class_="elementor-shortcode")
    for step in method_list.find_all("p"):
        cocktail.steps.append(step.get_text(strip=True))

    # Get garnish
    garnish_header = soup.find("h4", string="Garnish")
    cocktail.garnish = garnish_header.find_next("p").get_text(strip=True)

    return cocktail


def get_all_cocktails():
    page_number = 1
    iba_url = f"https://iba-world.com/cocktails/all-cocktails/page/{page_number}/"

    # Get only first cocktail from first page in dev
    env = os.getenv("ENV", "production").lower()
    if env == "development":
        cocktails = __get_cocktails_from_page(iba_url)
        cocktails[0] = __get_cocktail_details(cocktails[0])
        return cocktails

    cocktails = __get_cocktails_from_page(iba_url)
    while True:
        page_number += 1
        iba_url = f"https://iba-world.com/cocktails/all-cocktails/page/{page_number}/"
        page_cocktails = __get_cocktails_from_page(iba_url)
        if page_cocktails is None:
            break
        cocktails += page_cocktails

    for cocktail in cocktails:
        cocktail = __get_cocktail_details(cocktail)

    return cocktails

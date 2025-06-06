import os

from doctest import debug

from .iba import get_all_cocktails
from .output import writeCocktails

if __name__ == "__main__":
    env = os.getenv("ENV", "production").lower()
    if env == "development":
        from IPython.core.debugger import set_trace
        import sys

        def ipython_excepthook(exc_type, exc_value, exc_tb):
            import traceback
            import IPython

            traceback.print_exception(exc_type, exc_value, exc_tb)
            IPython.embed()

        sys.excepthook = ipython_excepthook

    cocktails = get_all_cocktails()
    writeCocktails(cocktails, "cocktails.txt")

    if env == "development":
        for cocktial in cocktails:
            print(cocktial)

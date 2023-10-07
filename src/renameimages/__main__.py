import os, sys

from os.path import dirname, join, abspath

sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from renameimages.rename import rename

def main():
    try:
        rename()
    except ValueError as ve:
        return str(ve)

if __name__ == "__main__":
    sys.exit(main())
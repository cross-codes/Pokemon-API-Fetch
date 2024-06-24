# main.py

import sys
from requests import get
from ansi_colors import bcolors
from func.details import print_details
from func.image import download_image

URL = "https://pokeapi.co/api/v2/pokemon/"


def main():
    pokemon_name = sys.argv[1]

    # Obtain JSON data
    api_response = get(URL + pokemon_name)

    if api_response:
        # Print details
        print_details(api_response.json(), pokemon_name)
        # Generate image
        download_image(api_response.json())
        print(f"{bcolors.OKGREEN}\nImage downloaded{bcolors.ENDC}")
    else:
        print(f"{bcolors.FAIL}Pokemon not found{bcolors.ENDC}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"{bcolors.FAIL}Incorrect arguments supplied{bcolors.ENDC}")
        sys.exit(1)
    else:
        main()
        sys.exit(0)

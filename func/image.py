# image.py

from urllib import request


def download_image(pokemon_data):
    image_url = pokemon_data["sprites"]["other"]["official-artwork"]["front_default"]
    request.urlretrieve(image_url, "sprite.png")

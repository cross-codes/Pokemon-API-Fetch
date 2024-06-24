# details.py

from ansi_colors import bcolors


def print_details(pokemon_data, pokemon_name):
    dex_number = pokemon_data["id"]
    types = []

    for x in range(0, len(pokemon_data["types"]), 1):
        types.append(pokemon_data["types"][x]["type"]["name"].upper())

    abilities = []

    for y in range(0, len(pokemon_data["abilities"]), 1):
        abilities.append(pokemon_data["abilities"][y]["ability"]["name"].capitalize())

    height = pokemon_data["height"] / 10
    weight = pokemon_data["weight"] / 10

    stats_array = pokemon_data["stats"]
    hp = stats_array[0]["base_stat"]
    attack = stats_array[1]["base_stat"]
    defense = stats_array[2]["base_stat"]
    special_attack = stats_array[3]["base_stat"]
    special_defense = stats_array[4]["base_stat"]
    speed = stats_array[5]["base_stat"]

    print(
        f"{bcolors.BOLD}Name:{bcolors.ENDC}",
        pokemon_name.capitalize(),
        f"{bcolors.BOLD}\nNational Number:{bcolors.ENDC}",
        dex_number,
    )

    print(f"{bcolors.BOLD}Type: {bcolors.ENDC}", end="")

    for z in range(0, len(types), 1):
        escape_code = getattr(bcolors, types[z])
        print(f"{bcolors.BOLD}{escape_code}{types[z]}{bcolors.ENDC}", end=" ")
    print(f"{bcolors.BOLD}\nAbilities: {bcolors.ENDC}", end="")

    for w in range(0, len(abilities), 1):
        if w == len(abilities) - 1:
            print(f"{abilities[w]}", end=" ")
        else:
            print(f"{abilities[w]}", end=", ")

    print(
        f"{bcolors.BOLD}\nHeight:{bcolors.ENDC}",
        height,
        "m",
        f"{bcolors.BOLD}\nWeight:{bcolors.ENDC}",
        weight,
        "kg",
    )

    print(f"{bcolors.BOLD}\nBase stats:{bcolors.ENDC}")

    print(
        f"{bcolors.BOLD}HP:{bcolors.ENDC}",
        hp,
        f"{bcolors.BOLD}\nAttack:{bcolors.ENDC}",
        attack,
        f"{bcolors.BOLD}\nDefense:{bcolors.ENDC}",
        defense,
        f"{bcolors.BOLD}\nSpecial Attack:{bcolors.ENDC}",
        special_attack,
        f"{bcolors.BOLD}\nSpecial Defense:{bcolors.ENDC}",
        special_defense,
        f"{bcolors.BOLD}\nSpeed:{bcolors.ENDC}",
        speed,
        f"{bcolors.BOLD}\nTotal:{bcolors.ENDC}",
        hp + attack + defense + special_attack + special_defense + speed,
    )

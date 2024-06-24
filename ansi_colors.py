# ansi_colors.py

from colorist import BgColor


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

    # Pokémon types with background colors and white text
    NORMAL = BgColor.WHITE  # White on Grey
    FIRE = BgColor.RED  # White on Red
    WATER = BgColor.BLUE  # White on Blue
    ELECTRIC = BgColor.YELLOW  # White on Yellow
    GRASS = BgColor.GREEN  # White on Green
    ICE = BgColor.CYAN  # White on Cyan
    FIGHTING = BgColor.RED  # White on Magenta
    POISON = "\033[97m\033[45m"  # White on Purple
    GROUND = "\033[97m\033[43m"  # White on Yellow
    FLYING = "\033[97m\033[47m"  # White on Light Grey
    PSYCHIC = "\033[97m\033[45m"  # White on Magenta
    BUG = BgColor.GREEN  # White on Green
    ROCK = BgColor.BLACK  # White on Dark Grey
    GHOST = "\033[97m\033[45m"  # White on Purple
    DRAGON = "\033[97m\033[44m"  # White on Dark Blue
    DARK = BgColor.BLACK  # White on Black
    STEEL = BgColor.WHITE  # White on Light Grey
    FAIRY = "\033[97m\033[105m"  # White on Light Magenta

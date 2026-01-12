import msvcrt

# ============================
# TERMINAL COLORS
# ============================

RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"

# ============================
# ASCII FONT (5x5)
# ============================

FONT = {
    "A": [" *** ", "*   *", "*****", "*   *", "*   *"],
    "B": ["**** ", "*   *", "**** ", "*   *", "**** "],
    "C": [" *** ", "*   *", "*    ", "*   *", " *** "],
    "D": ["**** ", "*   *", "*   *", "*   *", "**** "],
    "E": ["*****", "*    ", "***  ", "*    ", "*****"],
    "F": ["*****", "*    ", "***  ", "*    ", "*    "],
    "G": [" *** ", "*    ", "* ***", "*   *", " *** "],
    "H": ["*   *", "*   *", "*****", "*   *", "*   *"],
    "I": [" *** ", "  *  ", "  *  ", "  *  ", " *** "],
    "J": ["  ***", "   * ", "   * ", "*  * ", " **  "],
    "K": ["*   *", "*  * ", "***  ", "*  * ", "*   *"],
    "L": ["*    ", "*    ", "*    ", "*    ", "*****"],
    "M": ["*   *", "** **", "* * *", "*   *", "*   *"],
    "N": ["*   *", "**  *", "* * *", "*  **", "*   *"],
    "O": [" *** ", "*   *", "*   *", "*   *", " *** "],
    "P": ["**** ", "*   *", "**** ", "*    ", "*    "],
    "Q": [" *** ", "*   *", "*   *", "*  **", " ****"],
    "R": ["**** ", "*   *", "**** ", "*  * ", "*   *"],
    "S": [" ****", "*    ", " *** ", "    *", "**** "],
    "T": ["*****", "  *  ", "  *  ", "  *  ", "  *  "],
    "U": ["*   *", "*   *", "*   *", "*   *", " *** "],
    "V": ["*   *", "*   *", "*   *", " * * ", "  *  "],
    "W": ["*   *", "*   *", "* * *", "** **", "*   *"],
    "X": ["*   *", " * * ", "  *  ", " * * ", "*   *"],
    "Y": ["*   *", " * * ", "  *  ", "  *  ", "  *  "],
    "Z": ["*****", "   * ", "  *  ", " *   ", "*****"],

    "0": [" *** ", "*  **", "* * *", "**  *", " *** "],
    "1": ["  *  ", " **  ", "  *  ", "  *  ", " *** "],
    "2": [" *** ", "*   *", "   * ", "  *  ", "*****"],
    "3": ["**** ", "    *", " *** ", "    *", "**** "],
    "4": ["*   *", "*   *", "*****", "    *", "    *"],
    "5": ["*****", "*    ", "**** ", "    *", "**** "],
    "6": [" *** ", "*    ", "**** ", "*   *", " *** "],
    "7": ["*****", "   * ", "  *  ", " *   ", "*    "],
    "8": [" *** ", "*   *", " *** ", "*   *", " *** "],
    "9": [" *** ", "*   *", " ****", "    *", " *** "],

    " ": ["     "] * 5,
    ".": ["     ", "     ", "     ", " **  ", " **  "],
    "-": ["     ", "     ", " *** ", "     ", "     "],
    "_": ["     ", "     ", "     ", "     ", "*****"]
}

# ============================
# ASCII LOGOS
# ============================

LOGOS = {
    "HEART": [
        " **   ** ",
        "*********",
        " ********",
        "  ****** ",
        "    **   "
    ],
    "SMILE": [
        "         ",
        "*  *  *  ",
        "         ",
        "*      * ",
        "  ****   "
    ]
}

# ============================
# GLOBAL STATE
# ============================

FONT_SCALE = 1
LAST_OUTPUT = ""

# ============================
# UTILITY FUNCTIONS
# ============================

def wait():
    print(YELLOW + "\nPress any key to continue..." + RESET)
    msvcrt.getch()


def scale_block(block, scale):
    if scale == 1:
        return block

    enlarged = []
    for row in block:
        expanded = "".join(char * scale for char in row)
        for _ in range(scale):
            enlarged.append(expanded)
    return enlarged


def build_ascii(text):
    global FONT_SCALE

    filtered = ""
    for ch in text:
        if ch in FONT:
            filtered += ch
        elif ch.upper() in FONT:
            filtered += ch.upper()
        else:
            filtered += " "

    lines = [""] * (5 * FONT_SCALE)

    for ch in filtered:
        block = scale_block(FONT.get(ch, FONT[" "]), FONT_SCALE)
        for i in range(len(block)):
            lines[i] += block[i] + "  "

    return "\n".join(lines)


def save_output(content):
    if not content.strip():
        print(RED + "Nothing to save." + RESET)
        return

    with open("ascii_output.txt", "w", encoding="utf-8") as f:
        f.write(content)

    print(GREEN + "Saved to ascii_output.txt" + RESET)


# ============================
# MENU ACTIONS
# ============================

def single_character():
    global LAST_OUTPUT
    ch = input("Enter one character: ")
    if len(ch) != 1:
        print(RED + "Only one character allowed." + RESET)
        return

    art = build_ascii(ch)
    print(CYAN + art + RESET)
    LAST_OUTPUT = art


def word_mode():
    global LAST_OUTPUT
    text = input("Enter text (max 15 chars): ")
    if len(text) > 15:
        print(RED + "Text too long." + RESET)
        return

    art = build_ascii(text)
    print(CYAN + art + RESET)
    LAST_OUTPUT = art


def numbers_only():
    global LAST_OUTPUT
    text = input("Enter numbers only: ")
    if not text.isdigit():
        print(RED + "Invalid input." + RESET)
        return

    art = build_ascii(text)
    print(CYAN + art + RESET)
    LAST_OUTPUT = art


def logo_mode():
    global LAST_OUTPUT
    print("Available logos:", ", ".join(LOGOS.keys()))
    name = input("Enter logo name: ").upper()

    if name not in LOGOS:
        print(RED + "Logo not found." + RESET)
        return

    art = "\n".join(scale_block(LOGOS[name], FONT_SCALE))
    print(CYAN + art + RESET)
    LAST_OUTPUT = art


def change_size():
    global FONT_SCALE
    print("1. Small\n2. Medium\n3. Large")
    choice = input("Choose size: ")

    FONT_SCALE = {"1": 1, "2": 2, "3": 3}.get(choice, FONT_SCALE)
    print(GREEN + f"Font size set to {FONT_SCALE}x" + RESET)


# ============================
# MAIN MENU LOOP
# ============================

def main():
    while True:
        print("\n" + YELLOW + "ASCII ART GENERATOR" + RESET)
        print("1. Single Character")
        print("2. Word / Sentence")
        print("3. Numbers Only")
        print("4. ASCII Logos")
        print("5. Change Font Size")
        print("6. Save Last Output")
        print("7. Exit")

        key = msvcrt.getch().decode()

        if key == "1":
            single_character()
        elif key == "2":
            word_mode()
        elif key == "3":
            numbers_only()
        elif key == "4":
            logo_mode()
        elif key == "5":
            change_size()
        elif key == "6":
            save_output(LAST_OUTPUT)
        elif key == "7":
            print(GREEN + "Goodbye!" + RESET)
            break
        else:
            print(RED + "Invalid option." + RESET)

        wait()


if __name__ == "__main__":
    main()


import os
import msvcrt as key
from colorama import init, Fore

init()

small = {
    "a": ["     "," *** ","*  * ","**** ","*  * "],
    "b": ["*    ","*    ","**** ","*   *","**** "],
    "c": ["     "," *** ","*    ","*    "," *** "],
    "d": ["    *","    *"," ****","*   *"," ****"],
    "e": ["     "," *** ","* ** ","*    "," *** "],
    "f": ["  ** "," *   ","***  "," *   "," *   "],
    "g": ["     "," *** ","*   *"," ****","    *"],
    "h": ["*    ","*    ","**** ","*   *","*   *"],
    "i": ["  *  ","     "," **  ","  *  "," *** "],
    "j": ["   * ","     ","   * ","*  * "," **  "],
    "k": ["*    ","*  * ","***  ","*  * ","*   *"],
    "l": [" *   "," *   "," *   "," *   "," *** "],
    "m": ["     ","** * ","* * *","* * *","*   *"],
    "n": ["     ","***  ","*  * ","*  * ","*  * "],
    "o": ["     "," *** ","*   *","*   *"," *** "],
    "p": ["     ","**** ","*   *","**** ","*    "],
    "q": ["     "," *** ","*   *"," *** ","    *"],
    "r": ["     ","* ** ","**   ","*    ","*    "],
    "s": ["     "," *** "," *   ","   * "," *** "],
    "t": ["  *  "," *** ","  *  ","  *  ","  *  "],
    "u": ["     ","*   *","*   *","*   *"," *** "],
    "v": ["     ","*   *","*   *"," * * ","  *  "],
    "w": ["     ","*   *","* * *","* * *"," * * "],
    "x": ["     ","*   *"," *** "," *** ","*   *"],
    "y": ["     ","*   *","*   *"," ****","    *"],
    "z": ["     ","**** ","  *  "," *   ","**** "],
    "@": [" *** ","* * *"," *** ","*    "," *** "],
    "#": [" * * ","*****"," * * ","*****"," * * "],
    "$": [" *** ","* *  "," *** ","  * *"," *** "],
    "&": [" **  ","*  * "," **  ","*  * "," ** *"],
    " ": ["     ","     ","     ","     ","     "]
}

big = [
    " ***  ****   ***  ****  ***** *****  ***  *   * ***** ***** *   * *     *   * *   *  ***  ****   ***  ****   **** ***** *   * *   * *   * *   * *   * *****        ***                     ***  ***   ****  ****  *   * *****  ***  *****  ***  ***** ",
    "*   * *   * *   * *   * *     *     *     *   *   *      *  *  *  *     ** ** **  * *   * *   * *   * *   * *       *   *   * *   * *   *  * *   * *     *        * ***                   *   *   *       *     * *   * *     *         * *   * *   * ",
    "*   * ****  *     *   * ***   ****  *  ** *****   *      *  ***   *     * * * * * * *   * ****  *   * ****  *****   *   *   * *   * * * *   *     *     *         * * *       *****       *   *   *       *   **  ***** ****  ****      *  ***  ***** ",
    "***** *   * *   * *   * *     *     *   * *   *   *   *  *  *  *  *     *   * *  ** *   * *     *   * *  *      *   *   *   *  * *  ** **  * *    *    *          * * *              ***  *   *   *   ***       *     *     * *   *     * *   *     * ",
    "*   * ****   ***  ****  ***** *      ***  *   * *****  ***  *   * ***** *   * *   *  ***  *      ***  *   * ****    *   *****   *   *   * *   *   *   *****        ***  *****        ***   ***  ***** ***** ****      * ****   ***      *  ***      * "
]

def select_color():
    os.system("cls")
    print("1.Red 2.Green 3.Yellow 4.Blue 5.Magenta 6.Cyan 7.White")
    return {
        "1": Fore.RED, "2": Fore.GREEN, "3": Fore.YELLOW,
        "4": Fore.BLUE, "5": Fore.MAGENTA, "6": Fore.CYAN,
        "7": Fore.WHITE
    }.get(key.getch().decode(), Fore.CYAN)

active_color = Fore.CYAN

def show_small(text):
    os.system("cls")
    for row in range(5):
        for ch in text:
            print(active_color + small[ch][row] + "  ", end="")
        print()

def show_big(text):
    os.system("cls")
    for line in big:
        for ch in text:
            if ch.isdigit():
                pos = (ord(ch) - 17) * 6
            else:
                pos = (ord(ch) - 65) * 6
            for i in range(pos, pos + 6):
                print(active_color + line[i], end="")
        print()

def start_menu():
    global active_color
    while True:
        os.system("cls")
        print("\nASCII ART PROJECT")
        print("1. Small Letter")
        print("2. Capital Letter")
        print("3. Small Word")
        print("4. Capital Word")
        print("5. Numbers")
        print("6. Special Characters")
        print("7. Exit")

        choice = key.getch().decode()
        active_color = select_color()

        if choice == "1":
            val = input("Enter small letter: ")
            if len(val) == 1 and val in small:
                show_small(val)

        elif choice == "2":
            val = input("Enter capital letter: ").upper()
            if len(val) == 1 and val.isalpha():
                show_big(val)

        elif choice == "3":
            word = input("Enter small word: ")
            if all(ch in small for ch in word):
                show_small(word)

        elif choice == "4":
            word = input("Enter capital word: ").upper()
            if word.replace(" ", "").isalpha():
                show_big(word)

        elif choice == "5":
            num = input("Enter numbers: ")
            if num.isdigit():
                show_big(num)

        elif choice == "6":
            sym = input("Enter special characters (@#$&): ")
            if all(ch in small for ch in sym):
                show_small(sym)

        elif choice == "7":
            break

        input("\nPress Enter to continue...")

start_menu()

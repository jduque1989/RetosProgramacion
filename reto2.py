# /*
#  * Escribe un programa que reciba un texto y transforme lenguaje natural a
#  * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
#  *  se caracteriza por sustituir caracteres alfanuméricos.
#  * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
#  *   con el alfabeto y los números en "leet".
#  *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
#  */

# Creating a list of common leet speak substitutions for each letter from A to Z

leet_speak_dict = {
    "A": "4",
    "B": "8",
    "C": "(",
    "D": "|)",
    "E": "3",
    "F": "|=",
    "G": "9",
    "H": "#",
    "I": "1",
    "J": "_|",
    "K": "|<",
    "L": "|_",
    "M": "/\\/",
    "N": "|\\|",
    "O": "0",
    "P": "|D",
    "Q": "(,)",
    "R": "|2",
    "S": "$",
    "T": "7",
    "U": "|_|",
    "V": "\\/",
    "W": "\\/\\/",
    "X": "><",
    "Y": "`/'",
    "Z": "2",
    "a": "4",
    "b": "8",
    "c": "(",
    "d": "|)",
    "e": "3",
    "f": "|=",
    "g": "9",
    "h": "#",
    "i": "1",
    "j": "_|",
    "k": "|<",
    "l": "|_",
    "m": "/\\/",
    "n": "|\\|",
    "o": "0",
    "p": "|D",
    "q": "(,)",
    "r": "|2",
    "s": "$",
    "t": "7",
    "u": "|_|",
    "v": "\\/",
    "w": "\\/\\/",
    "x": "><",
    "y": "`/'",
    "z": "2",
    " ": " ",
}

message = "Esto es un mensaje de prueba donde se escribe de manera"


def convert_to_leet_speak(message):
    crypt = []
    for char in message:
        crypt.append(leet_speak_dict[char])
    return "".join(crypt)


leet_message = convert_to_leet_speak(message)
print(leet_message)

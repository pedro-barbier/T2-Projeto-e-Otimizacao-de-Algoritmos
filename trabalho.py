import sys

def msg_counter(msg: str) -> int:
    morse = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "'": ".----.",
    "!": "-.-.--",
    "/": "-..-.",
    "(": "-.--.",
    ")": "-.--.-",
    "&": ".-...",
    ":": "---...",
    ";": "-.-.-.",
    "=": "-...-",
    "+": ".-.-.",
    "-": "-....-",
    "_": "..--.-",
    '"': ".-..-.",
    "$": "...-..-",
    "@": ".--.-."
    }

    codes = set(morse.values())
    lens  = sorted({len(v) for v in codes})

    def decode_count(s: str) -> int:
        def ways(i: int) -> int:
            if i == len(s):
                return 1
            total = 0
            for L in lens:
                if i + L <= len(s) and s[i:i+L] in codes:
                    total += ways(i + L)
            return total
        return ways(0)

    total = 1
    for token in msg.split():
        total *= decode_count(token)
    return total

def main():
    if len(sys.argv) != 2:
        print("Entrada inválida.")
        sys.exit(1)
        
    msg = sys.argv[1]
    print(f"Número de mensagens válidas no código provido: {msg_counter(msg)}")

if __name__ == "__main__":
    main()

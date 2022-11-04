

def get_braille_chars(emboss_char='O', flat_char=' '):
    e = f'{emboss_char}'
    f = f'{flat_char}'
    return {
        'a': f"{e}{f}_{f}{f}_{f}{f}",

        'b': f"{e}{f}_{e}{f}_{f}{f}",

        'c': f"{e}{e}_{f}{f}_{f}{f}",

        'd': f"{e}{e}_{f}{e}_{f}{f}",

        'e': f"{e}{f}_{f}{e}_{f}{f}",

        'f': f"{e}{e}_{e}{f}_{f}{f}",

        'g': f"{e}{e}_{e}{e}_{f}{f}",

        'h': f"{e}{f}_{e}{e}_{f}{f}",

        'i': f"{f}{e}_{e}{f}_{f}{f}",

        'j': f"{f}{e}_{e}{e}_{f}{f}",

        'k': f"{e}{f}_{f}{f}_{e}{f}",

        'l': f"{e}{f}_{e}{f}_{e}{f}",

        'm': f"{e}{e}_{f}{f}_{e}{f}",

        'n': f"{e}{e}_{f}{e}_{e}{f}",

        'o': f"{e}{f}_{f}{e}_{e}{f}",

        'p': f"{e}{e}_{e}{f}_{e}{f}",

        'q': f"{e}{e}_{e}{e}_{e}{f}",

        'r': f"{e}{f}_{e}{e}_{e}{f}",

        's': f"{f}{e}_{e}{f}_{e}{f}",

        't': f"{f}{e}_{e}{e}_{e}{f}",

        'u': f"{e}{f}_{f}{f}_{e}{e}",

        'v': f"{e}{f}_{e}{f}_{e}{e}",

        'w': f"{f}{e}_{e}{e}_{f}{e}",

        'x': f"{e}{e}_{f}{f}_{e}{e}",

        'y': f"{e}{e}_{f}{e}_{e}{e}",

        'z': f"{e}{f}_{f}{e}_{e}{e}",

        '!': f"{f}{f}_{e}{e}_{e}{f}",

        'cap': f"{f}{f}_{f}{f}_{f}{e}",

        'num': f"{f}{e}_{f}{e}_{e}{e}",

        ' ': f"{f}{f}_{f}{f}_{f}{f}",

        '.': f"{f}{f}_{f}{f}_{f}{f}",

        ',': f"{f}{f}_{f}{f}_{f}{f}",

        "'": f"{f}{f}_{f}{f}_{f}{f}",

        '0': f"{f}{f}_{f}{f}_{f}{f}",

        '1': f"{f}{f}_{f}{f}_{f}{f}",

        '2': f"{f}{f}_{f}{f}_{f}{f}",

        '3': f"{f}{f}_{f}{f}_{f}{f}",

        '4': f"{f}{f}_{f}{f}_{f}{f}",

        '5': f"{f}{f}_{f}{f}_{f}{f}",

        '6': f"{f}{f}_{f}{f}_{f}{f}",

        '7': f"{f}{f}_{f}{f}_{f}{f}",

        '8': f"{f}{f}_{f}{f}_{f}{f}",

        '9': f"{f}{f}_{f}{f}_{f}{f}",
    }


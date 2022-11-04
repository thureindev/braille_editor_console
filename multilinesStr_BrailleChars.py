

def get_braille_chars(emboss_char):
    e = f'{emboss_char}'
    f = '.'
    return {
        'a': f"""
{e}{f}
{f}{f}
{f}{f}""",
        'b': f"""
{e}{f}
{e}{f}
{f}{f}""",
        'c': f"""
{e}{e}
{f}{f}
{f}{f}""",
        'd': f"""
{e}{e}
{f}{e}
{f}{f}""",
        'e': f"""
{e}{f}
{f}{e}
{f}{f}""",
        'f': f"""
{e}{e}
{e}{f}
{f}{f}""",
        'g': f"""
{e}{e}
{e}{e}
{f}{f}""",
        'h': f"""
{e}{f}
{e}{e}
{f}{f}""",
        'i': f"""
{f}{e}
{e}{f}
{f}{f}""",
        'j': f"""
{f}{e}
{e}{e}
{f}{f}""",
        'k': f"""
{e}{f}
{f}{f}
{e}{f}""",
        'l': f"""
{e}{f}
{e}{f}
{e}{f}""",
        'm': f"""
{e}{e}
{f}{f}
{e}{f}""",
        'n': f"""
{e}{e}
{f}{e}
{e}{f}""",
        'o': f"""
{e}{f}
{f}{e}
{e}{f}""",
        'p': f"""
{e}{e}
{e}{f}
{e}{f}""",
        'q': f"""
{e}{e}
{e}{e}
{e}{f}""",
        'r': f"""
{e}{f}
{e}{e}
{e}{f}""",
        's': f"""
{f}{e}
{e}{f}
{e}{f}""",
        't': f"""
{f}{e}
{e}{e}
{e}{f}""",
        'u': f"""
{e}{f}
{f}{f}
{e}{e}""",
        'v': f"""
{e}{f}
{e}{f}
{e}{e}""",
        'w': f"""
{f}{e}
{e}{e}
{f}{e}""",
        'x': f"""
{e}{e}
{f}{f}
{e}{e}""",
        'y': f"""
{e}{e}
{f}{e}
{e}{e}""",
        'z': f"""
{e}{f}
{f}{e}
{e}{e}""",
        '!': f"""
{f}{f}
{e}{e}
{e}{f}""",
        'cap': f"""
{f}{f}
{f}{f}
{f}{e}""",
        'num': f"""
{f}{e}
{f}{e}
{e}{e}"""
    }


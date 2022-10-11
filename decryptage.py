def decryptage_substitution(texte):
    """Décryptage par substitution"""
    # Dictionnaire de correspondance
    correspondance = {"a": "e", "b": "s", "c": "t", "d": "a", "e": "o", "f": "h", "g": "n", "h": "r", "i": "i", "j": "d", "k": "l", "l": "u", "m": "m", "n": "c", "o": "p", "p": "v", "q": "f", "r": "g", "s": "b", "t": "j", "u": "q", "v": "k", "w": "w", "x": "x", "y": "y", "z": "z"}
    # Décryptage
    texte_decrypte = ""
    for lettre in texte:
        if lettre in correspondance:
            texte_decrypte += correspondance[lettre]
        else:
            texte_decrypte += lettre
    return texte_decrypte

print(decryptage_substitution("Huyzu Izxk u'hoovihvy eht h wzopvo. Vk hkkdph. Tzu Ahc phojdhvy pvudvy ivuly. Vk ezdtth du eozgzuw tzdevo, t'httvy whut tzu kvy, t'heedxhuy tdo tzu ezkzrqzu. Vk eovy du ozphu, vk k'zdiovy, vk kdy; phvt vk u'x thvtvtthvy jd'du vpmozlkvz rzugdt, vk mdyhvy h yzdy vutyhuy tdo du pzy wzuy vk vluzohvy kh tvluvgvrhyvzu. Vk hmhuwzuuh tzu ozphu tdo tzu kvy. Vk hkkh h tzu khihmz; vk pzdvkkh du lhuy jd'vk ehtth tdo tzu gozuy, tdo tzu rzd."))
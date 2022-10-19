LONGEUR_ALPHABET = 26
PREMIERE_INDEX = 97
DERNIER_INDEX = 122
AVG_ICS = {
    "fr": 0.06,
    "en": 0.0385
}
LETTERS_FREQUENCIES = {
    "fr": {
        'a': 8.4, 'b': 1.06, 'c': 3.03, 'd': 4.18, 'e': 17.26, 'f': 1.12, 'g': 1.27, 'h': 0.92, 'i': 7.34, 'j': 0.31, 'k': 0.05, 'l': 6.01, 'm': 2.96,
        'n': 7.13, 'o': 5.26, 'p': 3.01, 'q': 0.99, 'r': 6.55, 's': 8.08, 't': 7.07, 'u': 5.74, 'v': 1.32, 'w': 0.04, 'x': 0.45, 'y': 0.30, 'z': 0.12
    },

    "en": {
        'a': 8.2, 'b': 1.5, 'c': 2.8, 'd': 4.3, 'e': 12.7, 'f': 2.2, 'g': 2.0, 'h': 6.1, 'i': 7.0, 'j': 0.2, 'k': 0.8, 'l': 4.0, 'm': 2.4,
        'n': 6.7, 'o': 7.5, 'p': 1.9, 'q': 0.1, 'r': 6.0, 's': 6.3, 't': 9.1, 'u': 2.8, 'v': 1.0, 'w': 2.3, 'x': 0.1, 'y': 2.0, 'z': 0.1
    }
}

def caesar(text:str, key:int) -> str:
    result = ""

    for c in text.lower():
        if c.isalpha():
            result += chr((ord(c) + key % (LONGEUR_ALPHABET) - PREMIERE_INDEX) % (LONGEUR_ALPHABET) + PREMIERE_INDEX)
        else:
            result += c

    return result

def convert_to_correct_text(text:str) -> str:
    return "".join([c for c in text if c.isalpha()]).lower()

def get_occurence_des_dicts(text:str) -> "dict[int, int]":
    occurences = dict()

    for c in text:
        ascii_char = ord(c)
        if ascii_char in occurences:
            occurences[ascii_char] += 1
        else:
            occurences[ascii_char] = 1
    
    return occurences

def get_indice_de_coicidence(text:str) -> int:
    occurences = get_occurence_des_dicts(text)
    ic = 0.0
    text_len = len(text)

    for i in occurences:
        ic += occurences[i] * (occurences[i] - 1)
    
    return ic / (text_len * (text_len - 1))

def get_longueur_cle(text:str, lang:str) -> int or None:
    res = (None, None)

    for i in range(1, 20):
        sub_ic = abs(get_indice_de_coicidence(text[0::i]) - AVG_ICS[lang])
        if res[0] is None or (res[1] > sub_ic and res[0] % i != 0):
            res = (i, sub_ic)
    
    return res[0]

def trouver_cle_vigenere(text:str, lang:str) -> str:
    res = ""

    if lang in LETTERS_FREQUENCIES:
        max_frequency_lang = ord(min(LETTERS_FREQUENCIES[lang], key=LETTERS_FREQUENCIES[lang].get))
        text = convert_to_correct_text(text)
        key_length = get_longueur_cle(text, lang)

        for i in range(key_length):
            frequencies = get_occurence_des_dicts(text[i::key_length])
            max_frequency_text = max(frequencies, key=frequencies.get)

            res += chr(PREMIERE_INDEX + max_frequency_text - max_frequency_lang)

    return res

def vigenere(text:str, key:"list[int]") -> str:
    res = ""
    key_len = len(key)
    key_indice = 0

    for l in text.lower():
        if l.isalpha():
            res += caesar(l, PREMIERE_INDEX + key[key_indice])
            key_indice = (key_indice + 1) % key_len
        else:
            res += l
    
    return res

def encode_vigenere(text:str, key:str) -> str:
    return vigenere(text, [ord(n) for n in key])

def decode_vigenere(text:str, lang:str) -> str:
    return vigenere(text, [-ord(n) for n in trouver_cle_vigenere(text, lang)])

def bezout(a,b):
    ua, va, ub, vb = 1, 0, 0, 1
    while a !=0:
        q, r = divmod(b,a) # q <= b//a et r <= b%a
        m,n = ub -ua*q, vb -va*q
        b, a, ub, vb, ua, va = a, r, ua, va, m, n
    return b, ub, vb

def premier_entre_eux(a, b):
    return bezout(a, b)[0] == 1

def inverse(a, mod):
    if premier_entre_eux(a, mod):
        for i in range(1, mod):
            if a * i % mod == 1:
                return i
            elif a * (-i) % mod == 1:
                return -i
    return None
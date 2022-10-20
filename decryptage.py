from math import *

ALPHABET = { 'A':0 , 'B':1 , 'C':2 , 'D':3 , 'E':4 , 'F':5 , 'G':6 , 'H':7 , 'I':8 , 'J':9 , 'K':10 , 'L':11 , 'M':12 , 'N':13 , 'O':14 , 'P':15 , 'Q':16 , 'R':17 , 'S':18 , 'T':19 , 'U':20 , 'V':21 , 'W':22 , 'X':23 , 'Y':24 , 'Z':25 }


LONGEUR_ALPHABET = 26
PREMIERE_INDEX = 97
DERNIER_INDEX = 122
AVG_ICS = {
    "fr": 0.06,
    "en": 0.0385
}
FREQUENCES_LETTRES = {
    "fr": {
        'a': 8.4, 'b': 1.06, 'c': 3.03, 'd': 4.18, 'e': 17.26, 'f': 1.12, 'g': 1.27, 'h': 0.92, 'i': 7.34, 'j': 0.31, 'k': 0.05, 'l': 6.01, 'm': 2.96,
        'n': 7.13, 'o': 5.26, 'p': 3.01, 'q': 0.99, 'r': 6.55, 's': 8.08, 't': 7.07, 'u': 5.74, 'v': 1.32, 'w': 0.04, 'x': 0.45, 'y': 0.30, 'z': 0.12
    },

    "en": {
        'a': 8.2, 'b': 1.5, 'c': 2.8, 'd': 4.3, 'e': 12.7, 'f': 2.2, 'g': 2.0, 'h': 6.1, 'i': 7.0, 'j': 0.2, 'k': 0.8, 'l': 4.0, 'm': 2.4,
        'n': 6.7, 'o': 7.5, 'p': 1.9, 'q': 0.1, 'r': 6.0, 's': 6.3, 't': 9.1, 'u': 2.8, 'v': 1.0, 'w': 2.3, 'x': 0.1, 'y': 2.0, 'z': 0.1
    }
}

def caesar(text:str, cle:int) -> str:
    result = ""

    for lettre in text.lower():
        if lettre.isalpha():
            result += chr((ord(lettre) + cle % (LONGEUR_ALPHABET) - PREMIERE_INDEX) % (LONGEUR_ALPHABET) + PREMIERE_INDEX)
        else:
            result += lettre

    return result

def convertir_en_texte(text:str) -> str:
    return "".join([c for c in text if c.isalpha()]).lower()

def get_occurence_des_dicts(text:str) -> "dict[int, int]":
    occurences = dict()

    for lettre in text:
        ascii_char = ord(lettre)
        if ascii_char in occurences:
            occurences[ascii_char] += 1
        else:
            occurences[ascii_char] = 1
    
    return occurences

def get_indice_de_coicidence(text:str) -> int:
    occurences = get_occurence_des_dicts(text)
    indice_coincidence = 0.0
    text_len = len(text)

    for lettre in occurences:
        indice_coincidence += occurences[lettre] * (occurences[lettre] - 1)
    
    return indice_coincidence / (text_len * (text_len - 1))

def get_longueur_cle(text:str, lang:str) -> int or None:
    res = (None, None)

    for i in range(1, 20):
        sub_ic = abs(get_indice_de_coicidence(text[0::i]) - AVG_ICS[lang])
        if res[0] is None or (res[1] > sub_ic and res[0] % i != 0):
            res = (i, sub_ic)
    
    return res[0]

def trouver_cle_vigenere(text:str, lang:str) -> str:
    res = ""

    if lang in FREQUENCES_LETTRES:
        max_frequence_lang = ord(min(FREQUENCES_LETTRES[lang], cle=FREQUENCES_LETTRES[lang].get))
        text = convertir_en_texte(text)
        longueur_cle = get_longueur_cle(text, lang)

        for i in range(longueur_cle):
            frequences = get_occurence_des_dicts(text[i::longueur_cle])
            max_frequence_texte = max(frequences, cle=frequences.get)

            res += chr(PREMIERE_INDEX + max_frequence_texte - max_frequence_lang)

    return res

def vigenere(text:str, cle:"list[int]") -> str:
    res = ""
    cle_len = len(cle)
    cle_indice = 0

    for l in text.lower():
        if l.isalpha():
            res += caesar(l, PREMIERE_INDEX + cle[cle_indice])
            cle_indice = (cle_indice + 1) % cle_len
        else:
            res += l
    
    return res

def decode_vigenere(text:str, lang:str) -> str:
    return vigenere(text, [-ord(n) for n in trouver_cle_vigenere(text, lang)])


def euclidian_diff(text:str, lang:str) -> float:
    text_convertit = convertir_en_texte(text, lang)
    occurences = get_occurence_des_dicts(text_convertit)
    sum = 0
    for elem in occurences:
        sum += pow(FREQUENCES_LETTRES['fr'][chr(elem)] - (occurences[elem] * 100 / len(text_convertit)), 2)

    return sqrt(sum)

def est_une_lettre(lettre:str, lang:str):
    return lettre in FREQUENCES_LETTRES[lang]

def convertir_en_texte(text:str, lang:str) -> str:
    return "".join([c for c in text if est_une_lettre(c, lang)]).lower()

def bezout(a,b):
    ua, va, ub, vb = 1, 0, 0, 1
    while a !=0:
        q, r = divmod(b,a) # q <= b//a et r <= b%a
        m,n = ub-ua*q, vb-va*q
        b, a, ub, vb, ua, va = a, r, ua, va, m, n
    return b, ub, vb

def nombre(a, b):
    return bezout(a, b)[0] == 1

def inverse(a, mod):
    if nombre(a, mod):
        for chiffre in range(1, mod):
            if a * chiffre % mod == 1:
                return chiffre
            elif a * (-chiffre) % mod == 1:
                return -chiffre
    return None

def decode_affine(texte:str, lang:str) -> None or "tuple[str, tuple[int, int]]":
    res = None

    if lang in FREQUENCES_LETTRES:
        for i in range(26):
            inv = inverse(i, LONGEUR_ALPHABET)
            if inv is not None:
                for j in range(26):
                    texte_res = ""
                    for c in texte.lower():
                        v = ord(c)
                        if est_une_lettre(c, lang):
                            texte_res += chr(((v - PREMIERE_INDEX - j) * inv + LONGEUR_ALPHABET) % LONGEUR_ALPHABET + PREMIERE_INDEX)
                        else:
                            texte_res += c

                    diff = euclidian_diff(texte_res, lang)

                    if res is None or res[1] > diff:
                        res = (texte_res, diff, i, j)

    return None if res is None else (res[0])

# print ("AFFINE :") 
# print(decode_affine("Huyzu Izxk u'hoovihvy eht h wzopvo. Vk hkkdph. Tzu Ahc phojdhvy pvudvy ivuly. Vk ezdtth du eozgzuw tzdevo, t'httvy whut tzu kvy, t'heedxhuy tdo tzu ezkzrqzu. Vk eovy du ozphu, vk k'zdiovy, vk kdy; phvt vk u'x thvtvtthvy jd'du vpmozlkvz rzugdt, vk mdyhvy h yzdy vutyhuy tdo du pzy wzuy vk vluzohvy kh tvluvgvrhyvzu. Vk hmhuwzuuh tzu ozphu tdo tzu kvy. Vk hkkh h tzu khihmz; vk pzdvkkh du lhuy jd'vk ehtth tdo tzu gozuy, tdo tzu rzd.", "fr"))
print(trouver_cle_vigenere("Dwi gsftn seebvzx ezjg jzzo. Zp ldvzx npvlh. Tt jlzcqo jsy dvjmdbvj, wnzpke wi ilme. Qg wetavzx owpo. Yy jmlme qiumdbdege ujexlqo uy qipssfzb. Lr nimzpwwi, gpfa gfycl ll'yy ogrw, atpj wzcmu uf'ci ksnade, twcn gvznjeh bc'pe fzcmusy, vje pzqi, jsyvv kvzqn tsfxn. Uy niirp Didex-Ximkmy, ci tplxjkmd xgrmybdw wtoirplqo lr npvceyl llm ainjetb.", "fr"))

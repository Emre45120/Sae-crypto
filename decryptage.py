from ctypes.wintypes import LONG
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

def decode_cesar(texte:str, decalage:int) -> str:
    """ Décode un texte chiffré avec le chiffrement de César

    Args:
        texte (str): Le texte à décoder
        decalage (int): Le décalage à appliquer

    Returns:
        str: Le texte décodé
    """    
    resultat = ""
    for lettre in texte :
        new = ord(lettre) + decalage
         
        if 65 <= ord(lettre) <= 90 :    
            if new > 90 :               
                new -= 26
            resultat += chr(new)        
        elif 97 <= ord(lettre) <= 122 : 
            if new > 122 :              
                new -= 26
            resultat += chr(new)        
        else :
            resultat += lettre   
    return resultat



def trouver_decalage(texteChiffre:str) -> int:
    """ Permet de trouver le décalage utilisé pour chiffrer un texte

    Args:
        texteChiffre (str): Le texte chiffré à analyser

    Returns:
        int: Le décalage utilisé
    """    
    max = None
    valeurEuclid = 0
    decalage = None
    for d in range(1,26):
        texte = decode_cesar(texteChiffre, d)
        valeurEuclid = euclidian_diff(texte,'fr')
        if max is None or valeurEuclid < max:
            max = valeurEuclid
            decalage = d
    return decalage


def caesar(text:str, cle:int) -> str:
    """ Chiffre un texte avec le chiffrement de César

    Args:
        text (str): Le texte à chiffrer
        cle (int): La clé à utiliser

    Returns:
        str: Le texte chiffré
    """    
    result = ""

    for lettre in text.lower():
        if lettre.isalpha():
            result += chr((ord(lettre) + cle % (LONGEUR_ALPHABET) - PREMIERE_INDEX) % (LONGEUR_ALPHABET) + PREMIERE_INDEX)
        else:
            result += lettre

    return result



def convertir_en_texte(text:str) -> str:
    """ Convertit un texte en minuscule et enlève les caractères spéciaux

    Args:
        text (str): Le texte à convertir

    Returns:
        str: Le texte converti
    """    
    return "".join([c for c in text if c.isalpha()]).lower()

def get_occurence_des_dicts(text:str) -> "dict[int, int]":
    """ Retourne un dictionnaire contenant le nombre d'occurence de chaque lettre

    Args:
        text (str): Le texte à analyser

    Returns:
        dict[int, int]: Le dictionnaire contenant le nombre d'occurence de chaque lettre
    """    
    occurences = dict()

    for lettre in text:
        ascii_char = ord(lettre)
        if ascii_char in occurences:
            occurences[ascii_char] += 1
        else:
            occurences[ascii_char] = 1
    
    for elem in occurences:
        (occurences[elem] * 100 / len(text))
    return occurences

def get_indice_de_coicidence(text:str) -> int:
    """ Retourne l'indice de coïncidence d'un texte

    Args:
        text (str): Le texte à analyser

    Returns:
        int: L'indice de coïncidence du texte
    """    
    occurences = get_occurence_des_dicts(text)
    indice_coincidence = 0.0
    text_len = len(text)

    for lettre in occurences:
        indice_coincidence += occurences[lettre] * (occurences[lettre] - 1)
    
    return indice_coincidence / (text_len * (text_len - 1))

def get_longueur_cle(text:str, lang:str) -> int or None:
    """ Retourne la longueur de la clé utilisée pour chiffrer un texte

    Args:
        text (str): Le texte à analyser
        lang (str): La langue du texte

    Returns:
        int or None: La longueur de la clé utilisée ou None si la longueur n'a pas pu être trouvée
    """    
    res = (None, None)

    for i in range(1, 20):
        sub_ic = abs(get_indice_de_coicidence(text[0::i]) - AVG_ICS[lang])
        if res[0] is None or (res[1] > sub_ic and res[0] % i != 0):
            res = (i, sub_ic)
    
    return res[0]

def trouver_cle_vigenere(text:str, lang:str) -> str:
    """ Retourne la clé utilisée pour chiffrer un texte avec le chiffrement de Vigenère

    Args:
        text (str): Le texte à analyser
        lang (str): La langue du texte

    Returns:
        str: La clé utilisée
    """    
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
    """ Chiffre un texte avec le chiffrement de Vigenère

    Args:
        text (str): Le texte à chiffrer
        cle (list[int]): La clé à utiliser

    Returns:
        str: Le texte chiffré
    """    
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
    """ Déchiffre un texte avec le chiffrement de Vigenère

    Args:
        text (str): Le texte à déchiffrer
        lang (str): La langue du texte

    Returns:
        str: Le texte déchiffré
    """    
    return vigenere(text, [-ord(n) for n in trouver_cle_vigenere(text, lang)])


def euclidian_diff(text:str, lang:str) -> float:
    """ Retourne la différence entre l'indice de coïncidence du texte et la moyenne de l'indice de coïncidence de la langue

    Args:
        text (str): Le texte à analyser
        lang (str): La langue du texte

    Returns:
        float: La différence entre l'indice de coïncidence du texte et la moyenne de l'indice de coïncidence de la langue
    """    
    text_convertit = convertir_en_texte(text, lang)
    occurences = get_occurence_des_dicts(text_convertit)
    sum = 0
    for elem in occurences:
        sum += pow(FREQUENCES_LETTRES['fr'][chr(elem)] - (occurences[elem] * 100 / len(text_convertit)), 2)

    return sqrt(sum)

def est_une_lettre(lettre:str, lang:str) -> bool:
    """ Retourne si une lettre est une lettre de la langue

    Args:
        lettre (str): La lettre à analyser
        lang (str): La langue du texte

    Returns:
        bool: Retourne True si la lettre est une lettre de la langue, False sinon
    """    
    return lettre in FREQUENCES_LETTRES[lang]

def convertir_en_texte(text:str, lang:str) -> str:
    """ Retourne le texte sans les caractères spéciaux

    Args:
        text (str): Le texte à analyser
        lang (str): La langue du texte

    Returns:
        str: Le texte sans les caractères spéciaux
    """    
    return "".join([c for c in text if est_une_lettre(c, lang)]).lower()

def bezout(a:float, b:float) -> tuple:
    """ Retourne le PGCD de a et b ainsi que les coefficients de Bézout

    Args:
        a (_type_): Le premier nombre
        b (_type_): Le deuxième nombre

    Returns:
        tuple: Le PGCD de a et b ainsi que les coefficients de Bézout
    """    
    ua, va, ub, vb = 1, 0, 0, 1
    while a !=0:
        q, r = divmod(b,a) # q <= b//a et r <= b%a
        m,n = ub-ua*q, vb-va*q
        b, a, ub, vb, ua, va = a, r, ua, va, m, n
    return b, ub, vb

def nombre(a:float, b:float) -> bool:
    """ Teste a et b pour savoir si ils sont premiers entre eux ou non avec Bezout 

    Args:
        a (float): Le premier nombre
        b (float): Le deuxième nombre

    Returns:
        bool: True si a et b sont premiers entre eux, False sinon
    """      
    return bezout(a, b)[0] == 1

def separe_texte(text:str) -> "list[str]":
    """ Retourne une liste de texte séparé par des espaces

    Args:
        text (str): Le texte à analyser

    Returns:
        list[str]: Une liste de texte séparé par des espaces
    """    
    sub_texts = list()

    for i in range(0, len(text), 2):
        sub_texts.append(text[i:i+2])
    
    return sub_texts

def inverse(a:int, mod:int) -> int or None:
    """ Retourne l'inverse de a modulo mod

    Args:
        a (int): Le nombre dont on veut l'inverse
        mod (int): Le modulo

    Returns:
        int or None: L'inverse de a modulo mod ou None si a et mod ne sont pas premiers entre eux
    """    
    if nombre(a, mod):
        for chiffre in range(1, mod):
            if a * chiffre % mod == 1:
                return chiffre
            elif a * (-chiffre) % mod == 1:
                return -chiffre
    return None

def decode_affine(texte:str, lang:str) -> None or "tuple[str, tuple[int, int]]":
    """ Déchiffre un texte avec le chiffrement affine

    Returns:
        str: Le texte déchiffré ou None si le texte ne peut pas être déchiffré
    """    
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

def decode_hill(text:str, lang:str) -> None or "tuple[tuple[int, int, int, int]]":
    """ Déchiffre un texte avec le chiffrement de Hill

    Returns:
        str: Le texte déchiffré ou None si le texte ne peut pas être déchiffré
    """    
    res = None
    correct_text = convertir_en_texte(text, lang)

    sub_texts = separe_texte(correct_text, 2)
        
    if len(correct_text) % 2 != 0:
        sub_texts[-1] += "a"

    if lang in FREQUENCES_LETTRES:
         for a in range(1, 26):
            for b in range(1, 26):
                for c in range(1, 26):
                    for d in range(1, 26):
                        det_inv = inverse((a * d - b * c), LONGEUR_ALPHABET)
                        if det_inv is not None:
                            text_res = ""
                            inv = (det_inv * d, det_inv * b * -1, det_inv * c * -1, det_inv * a)

                            for sub in sub_texts:
                                elem = (ord(sub[0]) - PREMIERE_INDEX, ord(sub[1]) - PREMIERE_INDEX)
                                text_res += chr((elem[0] * inv[0] + elem[1] * inv[1]) % LONGEUR_ALPHABET + PREMIERE_INDEX) + chr((elem[0] * inv[2] + elem[1] * inv[3]) % LONGEUR_ALPHABET + PREMIERE_INDEX)

                            diff = get_indice_de_coicidence(text_res)

                            if res is None or res[1] < diff:
                                res = (text_res, diff, (a, b, c, d))
                            
    return None if res is None else (res[0:-1], res[2])



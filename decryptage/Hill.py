from constante import *
from fonctions_general import *

class Hill :

    def __init__(self) -> None:
        raise Exception('Non instanciable !')

    @staticmethod
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

    @staticmethod
    def nombre(a:float, b:float) -> bool:
        """ Teste a et b pour savoir si ils sont premiers entre eux ou non avec Bezout 

        Args:
            a (float): Le premier nombre
            b (float): Le deuxième nombre

        Returns:
            bool: True si a et b sont premiers entre eux, False sinon
        """      
        return Hill.bezout(a, b)[0] == 1
 
    @staticmethod
    def inverse(a:int, mod:int) -> int or None:
        """ Retourne l'inverse de a modulo mod

        Args:
            a (int): Le nombre dont on veut l'inverse
            mod (int): Le modulo

        Returns:
            int or None: L'inverse de a modulo mod ou None si a et mod ne sont pas premiers entre eux
        """    
        if Hill.nombre(a, mod):
            for chiffre in range(1, mod):
                if a * chiffre % mod == 1:
                    return chiffre
                elif a * (-chiffre) % mod == 1:
                    return -chiffre
        return None

    @staticmethod
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

    @staticmethod
    def get_indice_de_coicidence(text:str) -> int:
        """ Retourne l'indice de coïncidence d'un texte

        Args:
            text (str): Le texte à analyser

        Returns:
            int: L'indice de coïncidence du texte
        """    
        occurences = Hill.get_occurence_des_dicts(text)
        indice_coincidence = 0.0
        text_len = len(text)

        for lettre in occurences:
            indice_coincidence += occurences[lettre] * (occurences[lettre] - 1)
        
        return indice_coincidence / (text_len * (text_len - 1))


    @staticmethod 
    def est_une_lettre(lettre:str, lang:str) -> bool:
        """ Retourne si une lettre est une lettre de la langue

        Args:
            lettre (str): La lettre à analyser
            lang (str): La langue du texte

        Returns:
            bool: Retourne True si la lettre est une lettre de la langue, False sinon
        """    
        return lettre in FREQUENCES_LETTRES[lang] 

    @staticmethod
    def convertir_en_texte(text:str, lang:str) -> str:
        """ Retourne le texte sans les caractères spéciaux

        Args:
            text (str): Le texte à analyser
            lang (str): La langue du texte

        Returns:
            str: Le texte sans les caractères spéciaux
        """    
        return "".join([c for c in text.lower() if Hill.est_une_lettre(c, lang)])

    @staticmethod
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
        
    @staticmethod
    def decode_hill(text:str, lang:str) -> None or "tuple[tuple[int, int, int, int]]":
        """ Déchiffre un texte avec le chiffrement de Hill

        Returns:
            str: Le texte déchiffré ou None si le texte ne peut pas être déchiffré
        """    
        res = None
        correct_text = Hill.convertir_en_texte(text, lang)
        PREMIERE_INDEX = 97

        sub_texts = Hill.separe_texte(correct_text)
            
        if len(correct_text) % 2 != 0:
            sub_texts[-1] += "a"

        if lang in FREQUENCES_LETTRES:
            for a in range(1, 26):
                for b in range(1, 26):
                    for c in range(1, 26):
                        for d in range(1, 26):
                            det_inv = Hill.inverse((a * d - b * c), LONGUEUR_ALPHABET)
                            if det_inv is not None:
                                text_res = ""
                                inv = (det_inv * d, det_inv * b * -1, det_inv * c * -1, det_inv * a)

                                for sub in sub_texts:
                                    elem = (ord(sub[0]) - PREMIERE_INDEX, ord(sub[1]) - PREMIERE_INDEX)
                                    text_res += chr((elem[0] * inv[0] + elem[1] * inv[1]) % LONGUEUR_ALPHABET + PREMIERE_INDEX) + chr((elem[0] * inv[2] + elem[1] * inv[3]) % LONGUEUR_ALPHABET + PREMIERE_INDEX)

                                diff = Hill.get_indice_de_coicidence(text_res)


                                if res is None or res[1] < diff:
                                    res = (text_res, diff, (a, b, c, d))
                                
        return None if res is None else (res[0:-1], res[2])




from constante import *
from fonctions_general import *

class Affine :

    def __init__(self) -> None:
        raise Exception('Non instanciable !')

    @staticmethod
    def est_une_lettre(lettre:str) -> bool:
        """ Retourne si une lettre est une lettre de la langue

        Args:
            lettre (str): La lettre à analyser
            lang (str): La langue du texte

        Returns:
            bool: Retourne True si la lettre est une lettre de la langue, False sinon
        """    
        return lettre in FREQUENCE_LETTRE_FR

    @staticmethod
    def bezout(a,b):
        """
        Il calcule le pgcd de deux nombres, ainsi que les coefficients de l'identité de Bézout
        
        :param a: un nombre 
        :param b: un nombre 
        :return: Le pgcd, le coefficient de a et le coefficient de b
        """
        pgcd = a
        coef_u = 1
        coef_v = 0
        u = 0
        v = 1
        while b != 0: # on applique l'algorithme d'Euclide étendu
            q = pgcd // b 
            r = pgcd % b 
            pgcd = b  
            b = r 
            tmp = coef_u 
            coef_u = u 
            u = tmp - q * u 
            tmp = coef_v 
            coef_v = v 
            v = tmp - q * v 
        return pgcd, coef_u, coef_v 

    @staticmethod
    def inverse(a, mod):
        if Affine.bezout(a, mod)[0] == 1:
            for chiffre in range(1, mod):
                if a * chiffre % mod == 1:
                    return chiffre
                elif a * (-chiffre) % mod == 1:
                    return -chiffre
        return None

    @staticmethod
    def decode_affine(text:str) -> None or "tuple[str, tuple[int, int]]":
        """ Déchiffre un texte avec le chiffrement affine

        Returns:
            str: Le texte déchiffré ou None si le texte ne peut pas être déchiffré
        """    
        texte = Fct_gen.traiter_texte(text)
        res = None
        for i in range(26):
            inv = Affine.inverse(i, LONGUEUR_ALPHABET)
            if inv is not None:
                for j in range(26):
                    texte_res = ""
                    for c in texte:
                        v = ALPHA[c]
                        if Affine.est_une_lettre(c):
                            texte_res += ALPHABET[((v - ALPHA['A'] - j) * inv + LONGUEUR_ALPHABET) % LONGUEUR_ALPHABET + ALPHA['A']]
                        else:
                            texte_res += c

                    diff = Fct_gen.euclidian_diff(texte_res)

                    if res is None or res[1] > diff:
                        res = (texte_res, diff, i, j)

        return None if res is None else (res[0])



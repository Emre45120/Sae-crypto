
from constante import *
from fonctions_general import Fct_gen

class Cesar :

    def __init__(self) -> None:
        raise Exception('Non instanciable !')

    @staticmethod
    def chiffrement_cesar(text:str, cle:int) -> str:
        """ Chiffre un texte avec le chiffrement de César

        Args:
            text (str): Le texte à chiffrer
            cle (int): La clé à utiliser

        Returns:
            str: Le texte chiffré
        """  
        texte = Fct_gen.traiter_texte(text)
        result = ""
        for lettre in texte:
            if lettre.isalpha():
                result += ALPHABET[(ALPHA[lettre] + cle % (LONGUEUR_ALPHABET) - ALPHA['A']) % (LONGUEUR_ALPHABET) + ALPHA['A']]
            else:
                result += lettre

        return result

    @staticmethod
    def decode_cesar(text:str, decalage:int) -> str:
        """ Décode un texte chiffré avec le chiffrement de César

        Args:
            texte (str): Le texte à décoder
            decalage (int): Le décalage à appliquer

        Returns:
            str: Le texte décodé
        """    
        texte = Fct_gen.traiter_texte(text)
        resultat = ""
        for lettre in texte :
            new = ALPHA[lettre] + decalage
            if ALPHA['A'] <= ALPHA[lettre] <= ALPHA['Z'] :    
                if new > ALPHA['Z'] :               
                    new -= 26
                resultat += ALPHABET[new]               
            else :
                resultat += lettre   
        return resultat

    @staticmethod
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
            texte = Cesar.decode_cesar(texteChiffre, d)
            valeurEuclid = Fct_gen.euclidian_diff(texte,'fr')
            if max is None or valeurEuclid < max:
                max = valeurEuclid
                decalage = d
        return decalage
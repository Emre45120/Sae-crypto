from math import sqrt
from constante import *

class Fct_gen:

    def __init__(self) -> None:
        raise Exception('Non instanciable !')
    
    @staticmethod
    def traiter_texte(texte):
            """
            Il supprime tous les signes de ponctuation et les accents du message et le convertit en majuscules
            
            :param texte : le texte à déchiffrer
            :return: Le message est renvoyé en majuscules et sans ponctuation.
            """
            texte_traiter = "".join([caractere for caractere in texte if caractere.isalpha()]) # Supprime les signes de ponctuation
            return texte_traiter.upper()

    @staticmethod
    def dico_freq(texte):
            """
            Il prend un texte en entrée et renvoie un dictionnaire contenant la fréquence de chaque lettre
            :param texte: le texte à analyser
            :return: Un dictionnaire contenant la fréquence de chaque lettre.
            """
            dico = dict()
            for carac in texte:
                if carac in dico:
                    dico[carac] += 1
                else:
                    dico[carac] = 1
            return dico

    @staticmethod
    def euclidian_diff(text:str) -> float:
        """ Retourne la différence entre l'indice de coïncidence du texte et la moyenne de l'indice de coïncidence de la langue

        Args:
            text (str): Le texte à analyser
            lang (str): La langue du texte

        Returns:
            float: La différence entre l'indice de coïncidence du texte et la moyenne de l'indice de coïncidence de la langue
        """    
        texte = Fct_gen.traiter_texte(text)
        occurences = Fct_gen.dico_freq(texte)
        sum = 0
        for elem in occurences:
            sum += pow(FREQUENCE_LETTRE_FR[ALPHABET[ALPHA[elem]]] - (occurences[elem] * 100 / len(texte)), 2)
        return sqrt(sum)

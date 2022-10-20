from cesar import Cesar
from constante import *

class Vigenere:
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
    def indice_coincidence(message):
        """
        Il compte le nombre d'occurrences de chaque lettre dans le message, puis calcule l'indice de
        coïncidence
        
        :param message: le message à analyser
        :return: L'indice de coïncidence du message.
        """
        num = 0
        texte = Vigenere.traiter_texte(message)
        dico = Vigenere.dico_freq(texte)
        for i in range(26):
            if len(texte) > 1 :
                # Si la lettre est présente dans le texte au moins 2 fois
                if ALPHABET[i] in dico.keys() and dico[ALPHABET[i]] > 1 : 
                    # Application de la formule calculant l'indice de coïncidence
                    num += dico[ALPHABET[i]]*(dico[ALPHABET[i]]-1)/((len(texte)*(len(texte)-1))) 
                    round(num,7)
        return num
   
    @staticmethod
    def recherche_longueur_cle_vigenere(message):
        """
        Il prend un message en entrée et renvoie la longueur de la clé utilisée pour le chiffrer
        
        :param message: le message à déchiffrer
        :return: La longueur de la clé.
        """
        texte = Vigenere.traiter_texte(message)
        seuil = 0.065 
        sous_chaine = ""
        cpt = 1
        for i in texte :
            for j in range(0,len(texte),cpt) : # On parcourt le texte par pas de cpt
                sous_chaine += texte[j] # Construction de la sous chaine
            if Vigenere.indice_coincidence(sous_chaine) >= seuil : # Si l'indice de coïncidence est supérieur au seuil
                return cpt
            cpt += 1
            sous_chaine = "" 

    @staticmethod
    def sous_chaine(message,longueur_cle):
        """
        Il prend un message et la longueur de la clé en entrée et renvoie une liste de sous-chaines
        correspondant à la longueur de la clé
        
        :param message: le message à déchiffrer
        :param longueur_cle: la longueur de la clé
        :return: Une liste de sous-chaines.
        """
        texte = Vigenere.traiter_texte(message)
        sous_chaine = []
        for i in range(longueur_cle) :
            sous_chaine.append(texte[i::longueur_cle]) 
        return sous_chaine 

    @staticmethod
    def trouver_clef(message):
        """
        Il prend un message en entrée et renvoie la clé utilisée pour le chiffrer
        
        :param message: le message à déchiffrer
        :return: La clé.
        """
        texte = Vigenere.traiter_texte(message)
        longueur_cle = Vigenere.recherche_longueur_cle_vigenere(texte)
        fragment = Vigenere.sous_chaine(texte,longueur_cle) # On récupère les sous-chaines
        clef = ""
        for i in range(longueur_cle) :
            portion = fragment[i] # On récupère la sous-chaine indice i
            indice_lettre = 0 - Cesar.decalage(portion) # On calcule le décalage
            clef += ALPHABET[indice_lettre] # On ajoute la lettre correspondante à la clé
        return clef

    @staticmethod
    def decoder_vigenere(message,clef):
        """
        Il prend un message et une clé en entrée et renvoie le message déchiffré
        
        :param message: le message à déchiffrer
        :param clef: la clé
        :return: Le message déchiffré.
        """
        res = ""
        ind_l_message = 0
        ind_l_cle = 0
        texte = Vigenere.traiter_texte(message)
        while ind_l_message < len(texte):
            ind_carac_decode = (ALPHA[texte[ind_l_message]]-ALPHA[clef[ind_l_cle]])%26 # On calcule l'indice de la lettre décodée
            res += ALPHABET[ind_carac_decode] 
            ind_l_message+=1
            ind_l_cle+=1
            if ind_l_cle == len(clef): # Si on a parcouru toute la clé
                ind_l_cle = 0 # On recommence à la première lettre
        return res

MESSAGE = "Dwi gsftn seebvzx ezjg jzzo. Zp ldvzx npvlh. Tt jlzcqo jsy dvjmdbvj, wnzpke wi ilme. Qg wetavzx owpo. Yy jmlme qiumdbdege ujexlqo uy qipssfzb. Lr nimzpwwi, gpfa gfycl ll'yy ogrw, atpj wzcmu uf'ci ksnade, twcn gvznjeh bc'pe fzcmusy, vje pzqi, jsyvv kvzqn tsfxn. Uy niirp Didex-Ximkmy, ci tplxjkmd xgrmybdw wtoirplqo lr npvceyl llm ainjetb."


print(Vigenere.decoder_vigenere(MESSAGE,Vigenere.trouver_clef(MESSAGE)))




from decryptage import *


def decryptage_ceasar(texte: str) -> str:
    """Fonction qui permet de décrypter un texte crypté avec le codage de César

    Args:
        texte (str): Texte à décrypter

    Returns:
        str: Texte décrypté
    """    
    decalage = trouver_decalage(texte)
    return decode_cesar(texte, decalage)

def decryptage_vigenere(texte: str) -> str:
    """ Fonction qui permet de décrypter un texte crypté avec le codage de Vigenère

    Args:
        texte (str): Texte à décrypter

    Returns:
        str: Texte décrypté
    """    
    return decode_vigenere(texte, "fr")

def decryptage_affine(texte: str) -> str:
    """Fonction qui permet de décrypter un texte crypté avec le codage affine

    Args:
        texte (str): Texte à décrypter

    Returns:
        str: Texte décrypté
    """    
    return decode_affine(texte,'fr')

def decryptage_hill(texte : str) -> str:
    """Fonction qui permet de décrypter un texte crypté avec le codage de Hill

    Args:
        texte (str): Texte à décrypter

    Returns:
        str: Texte décrypté
    """    
    return decode_hill(texte,'fr')

def decrypter():
    """Fonction principale qui permet de décrypter un texte en détéctant le cryptage utilisé
    """    
    running = True
    while running:
        codageUtilise = None
        texte=input("Entrez votre code à décrypter :   ")
        print("Décryptage en cours...")
        texteCesar = decryptage_ceasar(texte)
        texteVigenere = "Dwi gsftn seebvzx ezjg jzzo. Zp ldvzx npvlh. Tt jlzcqo jsy dvjmdbvj, wnzpke wi ilme. Qg wetavzx owpo. Yy jmlme qiumdbdege ujexlqo uy qipssfzb. Lr nimzpwwi, gpfa gfycl ll'yy ogrw, atpj wzcmu uf'ci ksnade, twcn gvznjeh bc'pe fzcmusy, vje pzqi, jsyvv kvzqn tsfxn. Uy niirp Didex-Ximkmy, ci tplxjkmd xgrmybdw wtoirplqo lr npvceyl llm ainjetb."
        texteAffine = decryptage_affine(texte)
        # texteHill = test_avec_hill(texte)
        # texteSubstitution = test_avec_substitution(texte)
        codageUtilise=texte_le_plus_francais(texteCesar,texteVigenere,texteAffine)#,texteHill,texteSubstitution) 
        if codageUtilise == "César":
            print("Le code a été crypté avec le codage de César")
            print("Le texte décodé est : ",texteCesar)
            running = False
        elif codageUtilise == "Vigenere":
            print("Le code a été crypté avec le codage de Vigenère")
            print("Le texte décodé est : ",texteVigenere)
            running = False
        elif codageUtilise == "Affine":
            print("Le code a été crypté avec le codage Affine")
            print("Le texte décodé est : ",texteAffine)
            running = False
        # elif codageUtilise == "Hill":
        #     print("Le code a été crypté avec le codage de Hill")
        #     print("Le texte décodé est : ",texteHill)
        # elif codageUtilise == "Substitution":
        #     print("Le code a été crypté avec le codage de Substitution")
        #     print("Le texte décodé est : ",texteSubstitution)
        else :
            print("Le code n'a pas pu être décrypté car le cryptage utilisé n'est pas reconnu")
            running = False
            

def texte_le_plus_francais(texteCesar : str,texteVigenere : str,texteAffine : str) -> str: #,texteHill : str,texteSubstitution : str)
    """ Fonction qui permet de détecter le cryptage utilisé en regardant lequel des textes décodés est le plus français

    Args:
        texteCesar (str): Texte décodé avec le codage de César
        texteVigenere (str): Texte décodé avec le codage de Vigenère
        texteAffine (str): Texte décodé avec le codage affine

    Returns:
        str: Cryptage utilisé
    """    
    valeursCryptage = None
    valeur_cesar = euclidian_diff(texteCesar,'fr') 
    valeur_vigenere = euclidian_diff(texteVigenere,'fr')
    valeurAffine = euclidian_diff(texteAffine,'fr')
    # valeurHill = euclidian_diff(texteHill,'fr')
    # valeurSubstitution = euclidian_diff(texteSubstitution,'fr')
    if valeursCryptage == None or texteCesar < valeursCryptage:
        valeursCryptage = valeur_cesar
        cryptage = "Cesar"
    if valeur_vigenere < valeursCryptage:
        valeursCryptage = valeur_vigenere
        cryptage = "Vigenere"
    if valeurAffine < valeursCryptage:
        valeursCryptage = valeurAffine
        cryptage = "Affine"
    # if valeurHill < valeursCryptage:
        # valeursCryptage = valeurHill
        # cryptage = "Hill"
    # if valeurSubstitution < valeursCryptage:
        # valeursCryptage = valeurSubstitution
        # cryptage = "Substitution"
    return cryptage
   
    
if __name__ == "__main__":
    decrypter()

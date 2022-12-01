from cesar import Cesar
from vigenere import Vigenere
from affine import Affine
from Hill import Hill
from fonctions_general import Fct_gen


def decode_cesar(texte: str) -> str:
    """Fonction qui permet de décrypter un texte crypté avec le codage de César

    Args:
        texte (str): Texte à décrypter

    Returns:
        str: Texte décrypté
    """    
    decalage = Cesar.trouver_decalage(texte)
    return Cesar.decode_cesar(texte, decalage)

def decryptage_vigenere(texte: str) -> str:
    """ Fonction qui permet de décrypter un texte crypté avec le codage de Vigenère

    Args:
        texte (str): Texte à décrypter

    Returns:
        str: Texte décrypté
    """
    cle = Vigenere.trouver_clef(texte)    
    return Vigenere.decoder_vigenere(texte,cle)

def decryptage_affine(texte: str) -> str:
    """Fonction qui permet de décrypter un texte crypté avec le codage affine

    Args:
        texte (str): Texte à décrypter

    Returns:
        str: Texte décrypté
    """    
    return Affine.decode_affine(texte)

def decryptage_hill(texte : str) -> str:
    """Fonction qui permet de décrypter un texte crypté avec le codage de Hill

    Args:
        texte (str): Texte à décrypter

    Returns:
        str: Texte décrypté
    """    
    return Hill.decode_hill(texte)


def decrypter():
    """Fonction principale qui permet de décrypter un texte en détéctant le cryptage utilisé
    """    
    running = True
    while running:
        codageUtilise = None
        texte= input("Entrez le code à décrypter : ")
        print("Décryptage en cours...")
        texteCesar = decode_cesar(texte)
        texteVigenere = decryptage_vigenere(texte)
        texteAffine = decryptage_affine(texte)
        texteHill = decryptage_hill(texte)
        #texteSubstitution = test_avec_substitution(texte)
        codageUtilise=texte_le_plus_francais(texteCesar,texteVigenere,texteAffine,texteHill[0][0])#,texteSubstitution) 
        if codageUtilise == "Cesar":
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
        elif codageUtilise == "Hill":
            print("Le code a été crypté avec le codage de Hill")
            print("Le texte décodé est : ",texteHill)
            running = False
        # elif codageUtilise == "Substitution":
        #     print("Le code a été crypté avec le codage de Substitution")
        #     print("Le texte décodé est : ",texteSubstitution)
        else :
            print("Le code n'a pas pu être décrypté car le cryptage utilisé n'est pas reconnu")
            running = False
            

def texte_le_plus_francais(texteCesar : str,texteVigenere : str,texteAffine : str,texteHill : str) -> str: #,texteHill : str,texteSubstitution : str)
    """ Fonction qui permet de détecter le cryptage utilisé en regardant lequel des textes décodés est le plus français

    Args:
        texteCesar (str): Texte décodé avec le codage de César
        texteVigenere (str): Texte décodé avec le codage de Vigenère
        texteAffine (str): Texte décodé avec le codage affine

    Returns:
        str: Cryptage utilisé
    """    
    valeursCryptage = None
    valeur_cesar = Fct_gen.euclidian_diff(texteCesar) 
    valeur_vigenere = Fct_gen.euclidian_diff(texteVigenere)
    valeurAffine = Fct_gen.euclidian_diff(texteAffine)
    valeurHill = Fct_gen.euclidian_diff(texteHill)
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
    if valeurHill < valeursCryptage:
        valeursCryptage = valeurHill
        cryptage = "Hill"
    # if valeurSubstitution < valeursCryptage:
        # valeursCryptage = valeurSubstitution
        # cryptage = "Substitution"
    return cryptage
   
    
if __name__ == "__main__":
    decrypter()

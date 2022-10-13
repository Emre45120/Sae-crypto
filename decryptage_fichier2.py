from interval import interval


def traiter_message(message):
    """
    Il supprime tous les signes de ponctuation et les accents du message et le convertit en majuscules
    
    :param message: le message à chiffrer
    :return: Le message est renvoyé en majuscules et sans ponctuation.
    """
    
    res = None
    for caractere_special in "éèàùâêîôûëïü":
        message = message.replace(caractere_special, "")
    for ponctuation in ".,;:!?-'":
        message = message.replace(ponctuation, "")
    for espace in " ":
        message = message.replace(espace, "")
    res = message.upper()
        
    return res


def indice_coincidence(message):
    """
    Il compte le nombre d'occurrences de chaque lettre dans le message, puis calcule l'indice de
    coïncidence
    
    :param message: le message à analyser
    :return: L'indice de coïncidence du message.
    """
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dico = {}
    num = 0
    texte = traiter_message(message)
    for lettre in texte :
        if lettre in dico.keys() :
            dico[lettre]+=1
        else :
            dico[lettre] = 1
    for i in range(26):
        if len(texte) > 1 :
            if alphabet[i] in dico.keys() and dico[alphabet[i]] > 1 :
                num += dico[alphabet[i]]*(dico[alphabet[i]]-1)/((len(texte)*(len(texte)-1)))
                round(num,7)
    return num

def longueur_cle(message):
    texte = traiter_message(message)
    seuil = 0.065
    sous_chaine = ""
    cpt = 1
    for i in texte :
        for j in range(0,len(texte),cpt) :
            sous_chaine += texte[j]
        if indice_coincidence(sous_chaine) >= seuil :
            return cpt
        cpt += 1
        sous_chaine = ""


message ="UMHRTAMGCILTZOEYLMVNPAPZWTVAFVXIOZGTMIUIMINVNPAPZWAWHGMPZHRMDRVZQPTDEJZZHRXTYPVHZVXAIXMNLMDZZTSYDZIXTMYRRDTDEJZZHRXTYPVIERVZQPKV"

print(longueur_cle(message))
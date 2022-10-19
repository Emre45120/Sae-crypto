def analyse_frequence_lettre(texte):
    """Analyse la fréquence des lettres dans un texte.
    Retourne un dictionnaire contenant les lettres en clé et leur fréquence en valeur.
    """
    dico = {}
    for lettre in texte:
        if lettre in dico:
            dico[lettre] += 1
        else:
            dico[lettre] = 1
    return dico

def analyse_bigrammes(texte):
    """Analyse les bigrammes dans un texte.
    Retourne un dictionnaire contenant les bigrammes en clé et leur fréquence en valeur.
    """
    dico = {}
    for i in range(len(texte) - 1):
        bigramme = texte[i:i + 2]
        if bigramme in dico:
            dico[bigramme] += 1
        else:
            dico[bigramme] = 1
    return dico

def indice_coincidence(texte):
    """Calcule l'indice de coïncidence d'un texte.
    Retourne un nombre flottant.
    """
    dico = analyse_frequence_lettre(texte)
    somme = 0
    for lettre in dico:
        somme += dico[lettre] * (dico[lettre] - 1)
    return somme / (len(texte) * (len(texte) - 1))
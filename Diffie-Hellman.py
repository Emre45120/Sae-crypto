# Nous avons d'étudier le fonctionnement de l'algorithme de Diffie-Hellman

# 1) Détaillez et expliquez un de ces deux protocoles et explicitez en particulier son lien avec le problème du logarithme discret.

# Le principe de Diffie-Hellman est de permettre à deux communicants d'échanger de manière sécurisée. 
# Pour cela, il faut que les deux communicants aient un secret commun, c'est-à-dire un nombre premier p et g commun à ces deux communicants.
# Ces deux communicants vont ensuite chacun choisir une cle privée aléatoire D et H
# Le premier communicant va calculer A = g^S mod p
# il va ensuite l'envoyer au deuxième communicant,qui va calculer B = g^S mod p
# Le 2eme communicant va envoyer son résultat au 1er communicant
# les deux communicants vont ensuite calculer la même clef K = B^D mod p = A^H mod p, qui ne peut être connue que par les deux communicants car ils faut les deux clefs privées pour la calculer

# 2) Implémentez un programme permettant de simuler le protocole de Diffie-Hellman.

def Diffie_Hellman(p : int, g : int, S1 : int, S2 : int) -> int:
    """ Cette fonction permet de simuler le protocole de Diffie-Hellman

    Args:
        p (int): un nombre premier commun aux deux communicants
        g (int): un nombre premier commun aux deux communicants
        S1 (int): une clef privée du communicant 1
        S2 (int): une clef privée du communicant 2

    Returns:
        int: retourne la clef commune
    """    
    A = (g**S1) % p # calcul de A
    B = (g**S2) % p # calcul de B
    K1 = (B**S1) % p # calcul de la clef commune
    K2 = (A**S2) % p # calcul de la clef commune
    return K1, K2


# 3) Pour le protocole choisi, explicitez une méthode en “force brute” possible en théorie, 
#    si on intercepte les messages chiffrés en connaissant la taille de la clef, 
#    mais difficilement exploitable en pratique.
#
#    Une méthode en force brute possible est d'à partir de A, p, g et B calculer toutes les valeurs possibles de H pour retrouver B.
#    C'est à dire de tester une par une les valeurs de H jusqu'à trouver g^H mod p = B
#    Cette méthode peut être exploitable lorsque la taille de la clef est petite cependant sur de grands nombre cette méthode est en effet difficilement exploitable
#    car cela prendrait un trop grand temps avant de retrouver la clef mais aussi beaucoup de ressources. 

def brute_force_diffie_helman(p, g, B):
    for i in range(p):
        if B == g**i % p:
            return i




def est_premier(nombre : int) -> bool:
    """Verifie si un nombre est premier

    Args:
        nombre (int): un entier

    Returns:
        boolean: retourne True si le nombre est premier, False sinon
    """    
    for i in range(2,nombre):
        if nombre%i==0: # si le nombre est divisible par un nombre entre 2 et lui meme
            return False
    return True

def affichage() -> None:
    p_est_premier = True
    q_est_premier = True
    diffie = True
    while diffie:
        while p_est_premier:
            p = int(input("Entrez un nombre premier p : "))
            if est_premier(p):
                p_est_premier = False
            else:
                print("Ce nombre n'est pas premier")
        while q_est_premier:
            q = int(input("Entrez un nombre premier q : "))
            if est_premier(q):
                q_est_premier = False
            else:
                print("Ce nombre n'est pas premier")
        D = int(input("Communicant 1,entrez une clef privée D : "))
        H = int(input("Communicant 2,entrez une clef privée H : "))
        print(Diffie_Hellman(p, q, D, H))
        diffie = False

        

if __name__ == "__main__":
    affichage()
    
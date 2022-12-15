import random
import math
import timeit


# le code contient un menu qui vous permet de tester l'algorithme de Diffie Hellman avec des valeurs que vous voulez ou alors ave des valeurs genere aleatoirement.
# le code contient aussi 2 print ( qui sont en commentaire ) qui teste la méthode bruteForce et Baby Step Giant Step avec 2 prints associés qui affichent leur temps de réalisation (sont en commentaires).

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

def q_est_premier(p : int) -> bool:
    """Verifie si q est premier

    Args:
        p (int): un nombre premier

    Returns:
        boolean: retourne True si q est premier, False sinon
    """    
    q = (2*p) + 1
    return est_premier(q)


def brute_force_diffie_helman(p : int, g : int, B : int) -> int:
    """ Cette fonction permet de retrouver la clef privée H à partir de B ( ou A ), p, g

    Args:
        p (int):  un nombre premier commun aux deux communicants
        g (int):  un nombre premier commun inférieur à p aux deux communicants
        B (int):  le résultat de g^H mod p

    Returns:
        int: retourne la clef privée 
    """    
    for i in range(p):
        if B == g**i % p:
            return i


def affichage() -> None:
    p_est_premier = True
    g_est_premier = True
    diffie = True
    nombreP = None
    print("------------------------------------------------------------------------")
    print("| Bienvenue dans le programme de Diffie-Hellman                         |")
    print("------------------------------------------------------------------------")
    print("| 1. Simuler le protocole de Diffie-Hellman avec des chiffres choisis   |")
    print("| 2. Simuler le protocole de Diffie-Hellman avec des chiffres aléatoire |")
    print("------------------------------------------------------------------------")
    choix = input("Que voulez vous faire ? ")
    if choix == "1":
        while diffie: # tant que les deux communicants n'ont pas la meme clef
            while p_est_premier: # tant que p n'est pas premier
                p = int(input("Entrez un nombre premier p : "))
                if est_premier(p):
                    if q_est_premier(p):
                        nombreP = p
                        p_est_premier = False
                    else:
                        print("ce nombre ne valide pas la condition q = 2p + 1 avec q premier")
                else:
                    print("Ce nombre n'est pas premier")
            while g_est_premier: # tant que g n'est pas premier
                g = int(input("Entrez un nombre aléatoire inférieur à p : "))
                if g < nombreP:
                    g_est_premier = False
                else:
                    print("Ce nombre n'est pas inférieur à p")
            D = int(input("Communicant 1,entrez une clef privée D : "))
            H = int(input("Communicant 2,entrez une clef privée H : "))
            print(Diffie_Hellman(p, g, D, H))
            diffie = False
    elif choix == "2":
        while diffie: # tant que les deux communicants n'ont pas la meme clef
            while p_est_premier: # tant que p n'est pas premier
                p = random.randint(2,1000)
                if est_premier(p):
                    if q_est_premier(p):
                        nombreP = p
                        p_est_premier = False
                        print("Votre nombre premier p est : ",p)
                    else:
                        print("ce nombre ne valide pas la condition q = 2p + 1 avec q premier")
                else:
                    print("Ce nombre n'est pas premier")
            while g_est_premier: # tant que g n'est pas premier
                g = random.randint(2,1000)
                if g < nombreP:
                    g_est_premier = False
                    print("Votre nombre g est : ",g)
                else:
                    print("Ce nombre n'est pas inférieur à p")
            D = random.randint(2,1000)
            print("Votre clef privée D est : ",D)
            H = random.randint(2,1000)
            print("Votre clef privée H est : ",H)
            print(Diffie_Hellman(p, g, D, H))
            diffie = False
        

        
def baby_step_giant_step(g : int,h : int,p : int) -> int or None:
    """ methode bsgs sur diffie hellman

    Args:
        g (int): chiffre premier inférieur a p
        h (int): chiffre qui est le res du calcul (g^x mod p)
        p (int): chiffre premier p

    Returns:
        int or None: la clé secrete ou None si pas trouvé
    """    
    n = math.ceil(math.sqrt(p-1))
    dico = {}
    
    for i in range(n):
        dico[pow(g,i,p)]=i
        
    c = pow(g,n*(p - 2),p)
    
    for j in range(n):
        cleProbable = (h * pow(c,j,p)) % p
        if cleProbable in dico:
            return j * n + dico[cleProbable]
    return None

# print(baby_step_giant_step(1187,1147,1223))
# print(brute_force_diffie_helman(1223,1187,1147))

# print(timeit.timeit("baby_step_giant_step(100,171,179)",setup = "from __main__ import baby_step_giant_step ",number=1))
# print(timeit.timeit("brute_force_diffie_helman(179,170,171)",setup = "from __main__ import brute_force_diffie_helman ",number=1))

if __name__ == "__main__":
    affichage()
    
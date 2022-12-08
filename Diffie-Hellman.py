import random
import sys


# Nous avons d'étudier le fonctionnement de l'algorithme de Diffie-Hellman

# 1) Détaillez et expliquez un de ces deux protocoles et explicitez en particulier son lien avec le problème du logarithme discret.

# Le principe de Diffie-Hellman est de permettre à deux communicants d'échanger de manière sécurisée. 
# Pour cela, ils doivent avoir un nombre premier commun p qui doit valider q = 2p + 1 avec q premier.   
#  et g commun à ces deux communicants.    
# Ces deux communicants vont ensuite chacun choisir une cle privée aléatoire D et H respectivement.
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




# 3) Pour le protocole choisi, explicitez une me?thode en "force brute" possible en the?orie, 
#    si on intercepte les messages chiffre?s en connaissant la taille de la clef, 
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


def affichage() -> None:
    p_est_premier = True
    g_est_premier = True
    diffie = True
    nombreP = None
    print("-------------------------------------------------")
    print("| Bienvenue dans le programme de Diffie-Hellman |")
    print("-------------------------------------------------")
    print("1. Simuler le protocole de Diffie-Hellman avec des chiffres choisis")
    print("2. Simuler le protocole de Diffie-Hellman avec des chiffres aléatoire")
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

def convert_to_int(mess : str) -> int:
    """Convertit un message en entier

    Args:
        mess (str): un message

    Returns:
        int: retourne un entier
    """    
    mess =  mess.encode(encoding="utf-8") 
    return int.from_bytes(mess,byteorder=sys.byteorder)
 
def convert_to_str(mess : int) -> str:
    """Convertit un entier en message

    Args:
        mess (int): un entier

    Returns:
        str: retourne un message
    """
    mess = mess.to_bytes(len(str(mess)),byteorder=sys.byteorder)    
    return mess.decode(encoding="utf-8")



def encode_diffie(p : int,message : str,C : int,C2 : int) -> int:
    if est_premier(p):
        if q_est_premier(p):
            message = convert_to_int(message)
            if message > C and C2:
                encodageNiveaux1 = (message**C) % p
                print("Encodage niveau 1 : ",encodageNiveaux1)
                encodageNiveaux2 = (encodageNiveaux1**C2) % p
                print("Encodage niveau 2 : ",encodageNiveaux2)
                return convert_to_str(encodageNiveaux2)
            else:
                print("Votre message M doit être inférieur à C et C2")
        else:
            print("ce nombre ne valide pas la condition q = 2p + 1 avec q premier")
    else:
        print("Ce nombre n'est pas premier")

def decode_diffie(p : int,message : int,C : int,C2 : int) -> int:
    if est_premier(p):
        if q_est_premier(p):
                decodageNiveaux2 = (message**C2) % p
                print("Décodage niveau 2 : ",decodageNiveaux2)
                decodageNiveaux1 = (decodageNiveaux2**C) % p
                print("Décodage niveau 1 : ",decodageNiveaux1)
                message = convert_to_str(decodageNiveaux1)
                print("Message decodé: ",message)
        else:
            print("ce nombre ne valide pas la condition q = 2p + 1 avec q premier")
    else:
        print("Ce nombre n'est pas premier")

def meet_in_the_middle_diffie_helman(p):
    K1 = None
    



        

if __name__ == "__main__":
    affichage()
    
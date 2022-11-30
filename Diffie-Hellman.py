# Nous allons d'étudier le fonctionnement de l'algorithme de Diffie-Hellman

# 1) Détaillez et expliquez un de ces deux protocoles et explicitez en particulier son lien avec le problème du logarithme discret.

# Le principe de Diffie-Hellman est de permettre à deux personnes de communiquer de manière sécurisée. 
# Pour cela, il faut que les deux personnes aient un secret commun, c'est-à-dire un nombre premier p et g commun à ces deux personnes.
# Ces deux personnes vont ensuite chacun choisir une cle privée aléatoire S
# une première personne va calculer A = g^S mod p
# elle va ensuite l'envoyer à la deuxième personne,qui va calculer B = g^S mod p
# la deuxième personne va envoyer son résultat à la première personne
# les deux personnes vont ensuite calculer la même clef K = B^S mod p = A^S mod p, qui ne peut être connue que par les deux personnes car ils faut les deux clefs privées pour la calculer

# 2) Implémentez un programme permettant de simuler le protocole de Diffie-Hellman.

def Diffie_Hellman(p, g, S1, S2):
    A = (g**S1) % p
    B = (g**S2) % p
    K1 = (B**S1) % p
    K2 = (A**S2) % p
    return K1, K2

# 3) Pour le protocole choisi, explicitez une méthode en “force brute” possible en théorie, 
#    si on intercepte les messages chiffrés en connaissant la taille de la clef, 
#    mais difficilement exploitable en pratique.
#
#    Une méthode en force brute possible est d'à partir de A, p, g et B calculer toutes les valeurs possibles de H pour retrouver B.
#    C'est à dire de tester une par une les valeurs de H jusqu'à trouver g^H mod p = B
#    Cette méthode peut être exploitable lorsque la taille de la clef est petite cependant sur de grands nombre cette méthode est en effet difficilement exploitable
#    car cela prendrait un trop grand temps avant de retrouver la clef mais aussi beaucoup de ressources. 

def brute_force_diffie_hellman(p, g, A, B):
    H = 0
    while (g**H) % p != B:
        H += 1
    return H

crypt = Diffie_Hellman(23, 4, 13, 10)
#print(crypt)
print(brute_force_diffie_hellman(23, 4, crypt[0], crypt[1]))



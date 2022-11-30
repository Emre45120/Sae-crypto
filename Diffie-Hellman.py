# Nous avons d'étudier le fonctionnement de l'algorithme de Diffie-Hellman

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

print(Diffie_Hellman(23, 4, 13, 10))

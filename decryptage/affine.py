from decryptage.constante import *
from decryptage.vigenere import Vigenere


def inverse_modulo(a, b):
    for i in range(1, b):
        if (a * i) % b == 1:
            return i
    return None

# def decode_affine(message):
#     texte = Vigenere.traiter_texte(message)
#     res = None
#     for i in range(26):
#         inverse = inverse_modulo(i, LONGUEUR_ALPHABET)
#         if inverse is not None:
#             for j in range(LONGUEUR_ALPHABET):
#                 texte_res = ""
#                 for carac in texte:




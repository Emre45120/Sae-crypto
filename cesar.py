from email import message
import math 
import string

class Cesar:
    alphabet = string.ascii_uppercase
    alpha = {'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5, 'G' : 6, 'H' : 7, 'I' : 8, 'J' : 9, 'K' : 10, 'L' : 11, 'M' : 12, 'N' : 13, 'O' : 14, 'P' : 15, 'Q' : 16, 'R' : 17, 'S' : 18, 'T' : 19, 'U' : 20, 'V' : 21, 'W' : 22, 'X' : 23, 'Y' : 24, 'Z' : 25}
    fr_freq = {'A' : 8.4 , 'B' : 1.06 , 'C' : 3.03 , 'D' : 4.18 , 'E' : 17.26 , 'F' : 1.12 , 'G' : 1.27 , 'H' : 0.92 , 'I' : 7.34 , 'J' : 0.31 , 'K' : 0.05 , 'L' : 6.01 , 'M' : 2.96 , 'N' : 7.13 , 'O' : 5.26 , 'P' : 3.01 , 'Q' : 0.99 , 'R' : 6.55 , 'S' : 8.08 , 'T' : 7.07 , 'U' : 5.74 , 'V' : 1.32 , 'W' : 0.04 , 'X' : 0.45 , 'Y' : 0.3 , 'Z' : 0.12}

    def __init__(self) -> None:
        raise Exception('Non instanciable !')

    @staticmethod
    def decal(text,d):
        res = ""
        text = text.upper()
        for c in text :
            if c in Cesar.alpha.keys():
                res += Cesar.alphabet[(Cesar.alpha[c] + d) % 26]
            else :
                res += c
        return res

    @staticmethod
    def frequences(text):
        freq = dict()
        for lettre in text.upper():
            if lettre in Cesar.alphabet :
                if lettre in freq:
                    freq[lettre] += 1
                else :
                    freq[lettre] = 1
        for l in Cesar.alphabet :
            if l not in freq :
                freq[l] = 0.0
            else :
                freq[l] = freq[l] / len(text)
        return freq

    @staticmethod
    def lettre_freq_max(text):
        freq = Cesar.frequences(text)
        return max(freq,key=freq.get)

    @staticmethod
    def decode_E(text):
        E = Cesar.lettre_freq_max(text)
        print(E)
        decalage = Cesar.alpha[E] - Cesar.alpha['E']
        return Cesar.decal(text,(26-decalage)%26)
    
    @staticmethod
    def dist_freq_fr(message):
        distance = 0.0
        frq = Cesar.frequences(message)
        for lettre in Cesar.alphabet :
            distance += (frq[lettre] - Cesar.fr_freq[lettre])**2
        return math.sqrt(distance)

    @staticmethod
    def decode(message):
        d_mini = Cesar.dist_freq_fr(message)
        decal_mini = 0
        for d in range(1,26):
            d_curr = Cesar.dist_freq_fr(Cesar.decal(message ,d))
            if d_curr < d_mini :
                decal_mini = d
                d_mini = d_curr
        print(decal_mini)
        return Cesar.decal(message,decal_mini- 26%26)
MESSAGE = "Zc krgfkr u'le ufzxk le rzi drikzrc jli c'fscfex tyrjjzj ul mrjzjkrj.Zc flmizk jfe wizxf dlirc, zc gizk ul crzk wifzu, zc slk le xireu sfc. Zc j'rgrzjrzk. Zc j'rjjzk jli jfe tfjp, zc gizk le aflierc hl'zc gritflilk u'le rzi uzjkirzk. Zc rccldr le tzxrizccf hl'zc wldr aljhl'rl sflk hlfzhl'zc kiflmrk jfe griwld ziizkrek. Zc kfljjr."

print(Cesar.decode(MESSAGE))
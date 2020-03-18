# Concours Centrale-Supélec
# Informatique MP, PC, PSI, TSI
# 2017 (Mission d'exploration martienne)

import math
import numpy as np
import random

import inspect
import matplotlib.pyplot as plt

class bcolors:
    """Définit les couleurs pour l'affichage CMD."""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

lg = inspect.currentframe()

def messageErreur(message="Il n'est pas possible de continuer le script dû à une erreur non définie", ligne="non définie."):
    """Affiche un message d'erreur et arrête le processus. Requiert un message (str) localisant l'erreur (optionnel) et le numéro de ligne (optionnel)."""

    print(bcolors.FAIL + "Erreur: " + str(message) + ", ligne " + str(ligne) + bcolors.ENDC)
    print(bcolors.FAIL + "Fin du processus" + bcolors.ENDC)
    exit()

def générer_PI(n:int, cmax:int):
    """Génére n coordonnée(s) de points d'interêts sur une zone géographique carré de longueur cmax. Contraintes: (n,cmax)>= 0, n<=cmax². retourne une valeur de type np.ndarray."""
    
    if n < 0 or cmax < 0:
        messageErreur('(n, cmax)>=0', lg.f_lineno)
    elif n>cmax**2:
        messageErreur('Erreur: n<=cmax²', lg.f_lineno)
    
    PI = []
    while len(PI) < n:
        x = random.randint(0, cmax)
        y = random.randint(0, cmax)
        if [x, y] not in PI:
            PI.append([x, y])
    return np.array(PI)

def position_robot():
    """Donne les coordonnées du robot. Données fournit par l'utilisateur (input) pour x et y. Contraintes: (x, y) >= 0. Retourne un tuple (x, y)."""
    
    #x = int(input('Position abscisse robot: '))
    #y = int(input('Position ordonnée robot: '))

    x = 15
    y = 73

    if x < 0 or y < 0:
        messageErreur('(x, y) >= 0', lg.f_lineno)

    return (x, y)

def distance(a:float, b:float):
    """Calcule la distance entre deux points a et b. (a, b) tuples. Retourne une longueur float."""

    return ((a[0]-b[0])**2 + (a[1] - b[1])**2)**0.5

def point(PI, PR, i , n):
    """Permet de traiter de manière égale le robot avec les PI."""

    if i < n:
        return PI[i]
    else:
        return PR

def calculer_distance(PI):
    """Calcule la distance entre les PI et la position du robot."""

    PR = np.array(position_robot())
    n = len(PI)
    Dist = np.zeros([n + 1, n + 1])
    
    for i in range(n + 1):
        for j in range(n + 1):
            Dist[i, j] = distance(point(PI, PR, i, n), point(PI, PR, j, n))
            
    return Dist

def longueur_chemin(chemin:list, d):
    """"""
    long = 0

    for k in range(len(chemin) - 1):
        long += d[chemin[k], chemin[k + 1]]
    
    return long

def normaliser(chemin, n):
    valide = []
    for point in chemin:
        if point not in valide:
            valide.append(point)
    for k in range(n):
        if k not in valide:
            valide.append(k)
    return valide

def crée_individu(d):
    """"""

    chemin = list(range(len(d) - 1))
    random.shuffle(chemin)
    long = longueur_chemin(chemin, d)
    
    return [long, chemin]

def crée_population(m:int, d):
    """"""

    L = []
    for k in range(m):
        L.append(crée_individu(d))
    
    return L

def réduire(p:list):
    """"""

    p2 = sorted(p)
    p[:] = p2[:len(p)//2]

def muter_chemin(c:list):
    """"""
    
    i = random.randint(0, len(c) - 1)
    j = random.randint(0, len(c) - 2)

    if j >= i:
        j += 1
    
    c[i], c[j] = c[j], c[i]

def muter_individu(I, d):
    muter_chemin(I[1])
    I[0] = longueur_chemin(I[1], d)

def muter_population(p, proba, d):
    """"""

    for k in range(len(p)):
        if random.random() < proba:
            muter_individu(p[k], d)

def croiser(c1, c2):
    n = len(c1)
    return normaliser(c1[:n//2] + c2[n//2:], n)

def croiser_individus(i1, i2, d):
    c = croiser(i1[1], i2[1])
    return [longueur_chemin(c, d), c]

def nouvelle_génération(p, d):
    n = len(p)
    for k in range(n):
        p.append(croiser_individus(p[k], p[(k + 1)%n], d))

def algo_génétique(PI, m, proba, g):
    d = calculer_distance(PI)
    p = crée_population(m, d)

    for _ in range(g):
        réduire(p)
        nouvelle_génération(p, d)
        muter_population(p, proba, d)

        plt.plot(_, sorted(p)[0][0], linestyle='None', marker='D')
    
    return sorted(p)[0]

###
print(bcolors.HEADER + "Concours Supélec-Centrale - Informatique - 2017" + bcolors.ENDC)
###

print(algo_génétique(générer_PI(100, 100), 10, 0.2, 10000))
 
plt.show()
plt.close()
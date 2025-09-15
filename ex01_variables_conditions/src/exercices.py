from __future__ import annotations
import math

def somme(a: int, b: int) -> int:
    """Retourne la somme de deux entiers."""
    resultat = a + b
    return resultat


def produit(a: int, b: int) -> int:
    """Retourne le produit de deux entiers."""
    resultat = a * b
    return resultat


def est_pair(n: int) -> bool:
    """Vrai si le nombre est pair."""
    if n % 2 == 0:
        return True
    else:
        return False

def est_voyelle(lettre: str) -> bool:
    """Vrai si la lettre est une voyelle."""
    if lettre.lower() in "aeiouy":
        return True
    else:
        return False

def calcul_reduction(prix: float, taux: float) -> float:
    """Retourne le prix après remise (taux en pourcentage)."""
    if prix < 0:
        raise ValueError
    elif prix == 0 or taux > 100:
        return 0.0
    else:
        return prix * (1 - (taux / 100))
     


def est_bissextile(annee: int) -> bool:
    """Vrai si année bissextile (Grégorien).
    Une année est bissextile si elle est divisible par 4.
    Cependant, elle n'est pas bissextile si elle est divisible par 100, sauf si elle est aussi divisible par 400.
    Par exemple :
        - 2000 est bissextile (divisible par 400).
        - 1900 n'est pas bissextile (divisible par 100 mais pas par 400).
        - 2004 est bissextile (divisible par 4 mais pas par 100).
    """
    if annee % 4 != 0 or ( annee % 4 == 0 and annee % 100 == 0 and annee % 400 != 0):
        return False
    else:
        return True

def racine_carree(x: float) -> float:
    """Retourne la racine carrée d'un nombre."""
    if x < 0:
        raise ValueError
    return math.sqrt(x)

def maximum_trois(a: int, b: int, c: int) -> int:
    """Renvoie le maximum de trois valeurs sans utiliser max()."""
    if a > b:
        if a > c:
            return a
        else:
            return b
    elif b > c:
        return b
    return c

def factorielle(n: int) -> int:
    """Retourne la factorielle d'un entier.
    1. Vérifier si n est un nombre négatif :
       - Si oui, lever une exception avec un message d'erreur approprié.
    2. Initialiser une variable résultat à 1.
    3. Pour chaque valeur i de 1 à n inclus :
       - Multiplier le résultat actuel par i.
    4. Retourner le résultat.
    """
    # TODO
    raise NotImplementedError

def convertir_en_binaire(n: int) -> str:
    """Convertit un entier en représentation binaire."""
    # TODO
    raise NotImplementedError


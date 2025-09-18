from __future__ import annotations


def somme_pairs(nums: list[int]) -> int:
    # TODO: Implémentez la fonction pour calculer la somme de tous les nombres pairs de la liste donnée.
    calcul = 0
    for i in nums:
        if i % 2 == 0:
            calcul += i
    return calcul


def compter_occurrences(items: list[int], valeur: int) -> int:
    # TODO: Implémentez la fonction pour compter le nombre d'occurrences de `valeur` dans la liste `items`.
    nb_occurence = 0
    for i in items:
        if i == valeur:
            nb_occurence += 1
    return nb_occurence


def table_multiplication(n: int) -> list[int]:
    # TODO: Implémentez la fonction pour retourner la table de multiplication de `n` (jusqu'à 10 inclus).
    table = []
    for i in range(10):
        table.append((i+1) * n)
    return table


def trouver_maximum(nums: list[int]) -> int:
    # TODO: Implémentez une fonction pour trouver et retourner la valeur maximale dans la liste.
    rang = 0
    taille = len(nums)
    # faire une boucle pour passer chaque position de la liste nums indépendemment de la valeur qui s'y trouve (sauf les 2 dernières)
    while rang < (taille-1):
        # pour chaque position de la liste, comparer la valeur qui s'y trouve à la valeur de la position suivante  
        for i in range(taille-1):
            # si la valeur est supérieure à la valeur de la position suivante
            if nums[i] > nums[i+1]:
                # ajouter cette valeur à la fin de la liste
                nums.append(nums[i])
                # effacer la valeur de la position
                del nums[i]
                # incrémenter "rang" pour passer à la position suivante
                rang += 1
                # pas la peine de passer à la valeur suivante car elle à changer de place
                break
    # finir par comparer la valeur de l'avant dernière position avec celle de la dernière position
    if nums[taille-2] > nums[taille-1]:
        return nums[taille-2]
    else:
        return nums[taille-1]
                



def calculer_moyenne(nums: list[int]) -> float:
    # TODO: Implémentez une fonction pour calculer et retourner la moyenne des valeurs dans la liste.
    addition = 0
    moyenne = 0.0
    taille = len(nums)
    if taille == 0:
        return 0
    else:
        for i in range(taille):
            addition += nums[i]
        moyenne = addition / taille
        return moyenne


def compter_negatifs(nums: list[int]) -> int:
    # TODO: Implémentez une fonction pour compter et retourner le nombre d'entiers négatifs dans la liste.
    taille = len(nums)
    quantiteNbreNegatif = 0
    for i in range(taille):
        if nums[i] < 0:
            quantiteNbreNegatif += 1
    return quantiteNbreNegatif


def compter_mots(phrase: str) -> int:
    # TODO: Implémentez une fonction pour compter le nombre d'occurrences de `mot` dans une liste de chaînes de caractères.
    if phrase == "":
        return 0
    else:
        quantiteMots = 1
        for caractere in phrase:
            if caractere.isspace():
                quantiteMots += 1
        return quantiteMots


def trouver_plus_long(items: list[str]) -> str:
    # TODO: Implémentez une fonction pour trouver et retourner le mot le plus long dans une liste de chaînes de caractères.
    compterCarac = 0
    nbCarac = 0
    motPlusLong = ""
    for i in range(len(items)):
        mot = items[i]
        compterCarac = len(mot)
        if compterCarac > nbCarac:
            nbCarac = compterCarac
            motPlusLong = mot
    return motPlusLong


def convertir_majuscule(items: list[str]) -> list[str]:
    # TODO: Implémentez une fonction pour convertir toutes les chaînes de la liste en majuscules.
    majuscule = items.upper()
    return majuscule    



def compter_mots_commencant_par(phrase: str, lettre: str) -> int:
    # TODO: Implémentez une fonction pour compter les mots commençant par une lettre donnée.
    nbMots = 0
    liste = phrase.split()
    for mot in liste:
        if mot[0] == lettre:
            nbMots += 1
    return nbMots


def trouver_mot_finissant_par(phrase: str, suffixe: str) -> list[str]:
    # TODO: Implémentez une fonction pour trouver tous les mots qui se terminent par un suffixe donné dans la liste.
    listeMots = phrase.split()
    motsAvecSuffixe = [mot for mot in listeMots if mot.endswith(suffixe)]
    return motsAvecSuffixe


def compter_caracteres(s: str, char: str) -> int:
    # TODO: Implémentez une fonction pour compter le nombre d'occurences du caractère char et retourner le nombre total.
    occurence = 0
    # for i in range(len(s)):
    #    if s[i] == char:
    for i in s:
        if i == char:            
            occurence += 1
    return occurence


def inverser_chaine(s: str) -> str:
    # TODO: Implémentez une fonction pour inverser et retourner la chaîne de caractères donnée.
    taille = len(s)
    inverser_chaine = ""
    for i in range(taille-1, -1, -1):
        print(i, " ", s[i])
        inverser_chaine += s[i]
    return inverser_chaine
 


def trouver_occurrences_chaine(s: str, c: str) -> int:
    # TODO: Implémentez une fonction pour compter les occurrences d'un caractère donné dans une chaîne.
    occurence = 0
    tailleS = len(s)
    tailleC = len(c)
    # passer les lettres de la chaîne "s" une par une
    for i in range(tailleS):
        # si la lettre est identique à la première lettre de la chaîne "c"
        if s[i] == c[0]:
            # compter cette première lettre identique
            compteur = 1
            # vérifier que les lettres suivantes de "c" sont identiques aux lettres suivantes de "s"
            for j in range(tailleC-1):
                if c[j+1] == s[i+j+1]:
                    # pour chaque lettre identique, compter 1 de plus
                    compteur += 1
                else:
                    # dès que différence apparaît, arrêter la vérification
                    break
            # si toutes les lettres de "c" ont étaient identiques aux lettres de "s", compter une occurence
            if compteur == tailleC:
                occurence += 1
    return occurence

# tuples
def somme_pairs_tuples(nums: tuple[int, ...]) -> int:
    # TODO: Implémentez la fonction pour calculer la somme de tous les nombres pairs dans un tuple donné.
    raise NotImplementedError


def compter_occurrences_tuples(items: tuple[int, ...], valeur: int) -> int:
    # TODO: Implémentez la fonction pour compter le nombre d'occurrences d'une valeur dans un tuple donné.
    raise NotImplementedError


def table_multiplication_tuples(n: int) -> tuple[int, ...]:
    # TODO: Implémentez la fonction pour retourner la table de multiplication (jusqu'à 10 inclus) sous forme de tuple.
    raise NotImplementedError


def trouver_maximum_tuples(nums: tuple[int, ...]) -> int:
    # TODO: Implémentez une fonction pour trouver et retourner le nombre maximum d'un tuple.
    raise NotImplementedError


def calculer_moyenne_tuples(nums: tuple[int, ...]) -> float:
    # TODO: Implémentez une fonction pour calculer et retourner la moyenne des nombres dans un tuple.
    raise NotImplementedError

# sets

def somme_pairs_sets(nums: set[int]) -> int:
    # TODO: Implémentez la fonction pour calculer la somme de tous les nombres pairs dans un set donné.
    raise NotImplementedError

def compter_occurrences_sets(items: set[int], valeur: int) -> int:
    # TODO: Cette fonction vérifiera simplement si `valeur` existe puisque les sets ne permettent pas les doublons.
    raise NotImplementedError


def table_multiplication_sets(n: int) -> set[int]:
    # TODO: Implémentez une fonction pour retourner la table de multiplication (jusqu'à 10 inclus) sous forme de set.
    raise NotImplementedError


def trouver_maximum_sets(nums: set[int]) -> int:
    # TODO: Implémentez une fonction pour trouver et retourner le nombre maximum d'un set.
    raise NotImplementedError


def compter_negatifs_sets(nums: set[int]) -> int:
    # TODO: Implémentez une fonction pour compter et retourner le nombre de nombres négatifs dans un set.
    raise NotImplementedError

# dictionnaires

def ajouter_element(d: dict, cle: str, valeur: any) -> dict:
    # TODO: Implémentez une fonction pour ajouter une clé et sa valeur dans un dictionnaire.
    raise NotImplementedError


def supprimer_element(d: dict, cle: str) -> dict:
    # TODO: Implémentez une fonction pour supprimer une clé et sa valeur d'un dictionnaire.
    raise NotImplementedError


def fusionner_dictionnaires(d1: dict, d2: dict) -> dict:
    # TODO: Implémentez une fonction qui fusionne deux dictionnaires et renvoie le résultat.
    # Les valeurs de `d2` remplaceront celles de `d1` en cas de doublons.
    raise NotImplementedError


def inverser_dictionnaire(d: dict) -> dict:
    # TODO: Implémentez une fonction pour inverser un dictionnaire, échangeant les clés et les valeurs.
    # Note: Si des valeurs duplicatées existent, une erreur ou un comportement spécifique doit être défini.
    raise NotImplementedError


def compter_valeurs(d: dict) -> int:
    # TODO: Implémentez une fonction pour compter combien de paires clé-valeur sont dans le dictionnaire.
    raise NotImplementedError


def trouver_valeur_maximale(d: dict) -> any:
    # TODO: Implémentez une fonction pour trouver et retourner la valeur la plus grande dans un dictionnaire.
    raise NotImplementedError


def trouver_cle_par_valeur(d: dict, valeur: any) -> list[str]:
    # TODO: Implémentez une fonction pour retourner une liste de toutes les clés correspondant à une valeur donnée.
    raise NotImplementedError


def verifier_cle_existe(d: dict, cle: str) -> bool:
    # TODO: Implémentez une fonction qui vérifie si une clé existe dans le dictionnaire.
    raise NotImplementedError


def valeurs_uniques(d: dict) -> set:
    # TODO: Implémentez une fonction qui retourne toutes les valeurs uniques dans un dictionnaire sous forme de set.
    raise NotImplementedError


def mettre_a_jour_valeur(d: dict, cle: str, nouvelle_valeur: any) -> dict:
    # TODO: Implémentez une fonction pour mettre à jour une valeur associée à une clé existante ou en ajouter une nouvelle.
    raise NotImplementedError

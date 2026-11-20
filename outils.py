"""Boîte à outils d'AstraCorp.

Des petites fonctions utilisées par les scripts d'administration de l'équipe.
Elles ont été écrites par un stagiaire, juste avant son départ, sans aucun test.
"""
from pathlib import Path

LIMITE_GROS_FICHIER = 5 * 1024 * 1024   # 5 Mo


def taille_lisible(octets):
    """Renvoie une taille lisible par un humain.

    512 -> "512 o", 1536 -> "1.5 Ko", 3145728 -> "3.0 Mo", 5368709120 -> "5.0 Go"
    En dessous de 1024 octets, on affiche des octets ; à partir de 1024, des Ko, etc.
    """
    if octets <= 1024:
        return f"{octets} o"
    elif octets < 1024 ** 2:
        return f"{octets / 1024:.1f} Ko"
    elif octets < 1024 ** 3:
        return f"{octets / 1024 ** 2:.1f} Mo"
    return f"{octets / 1024 ** 3:.1f} Go"


def categorie(nom_fichier):
    """Renvoie la catégorie d'un fichier d'après son extension, sans tenir compte des majuscules.

    "script.py" -> "python", "NOTES.TXT" -> "texte", "erreurs.log" -> "log",
    "photo.jpg" ou "logo.png" -> "image", tout le reste -> "autre"
    """
    extension = Path(nom_fichier).suffix
    if extension == ".py":
        return "python"
    elif extension in (".txt", ".md"):
        return "texte"
    elif extension == ".log":
        return "log"
    elif extension in (".jpg", ".jpeg", ".png", ".gif"):
        return "image"
    return "autre"


def moyenne(notes):
    """Renvoie la moyenne d'une liste de notes. Lève une ValueError si la liste est vide."""
    if len(notes) == 0:
        raise ValueError("impossible de calculer la moyenne d'une liste vide")
    return sum(notes) / len(notes)


def mention(note):
    """Renvoie la mention correspondant à une note sur 20.

    moins de 10 : "Insuffisant"      de 10 à moins de 12 : "Passable"
    de 12 à moins de 14 : "Assez bien"   de 14 à moins de 16 : "Bien"
    16 et plus : "Très bien"
    Lève une ValueError si la note n'est pas entre 0 et 20.
    """
    if note < 0 or note > 20:
        raise ValueError(f"note impossible : {note}")
    if note < 10:
        return "Insuffisant"
    elif note < 12:
        return "Passable"
    elif note <= 14:
        return "Assez bien"
    elif note < 16:
        return "Bien"
    return "Très bien"


def mot_de_passe_solide(mdp):
    """Renvoie True si le mot de passe respecte la politique d'AstraCorp :
    au moins 12 caractères, au moins une majuscule, une minuscule et un chiffre.
    """
    if len(mdp) < 12:
        return False
    a_majuscule = any(c.isupper() for c in mdp)
    a_minuscule = any(c.islower() for c in mdp)
    a_chiffre = any(c.isdigit() for c in mdp)
    return a_majuscule and a_minuscule and a_chiffre


def nom_de_machine(texte):
    """Transforme un texte en nom de machine valide : minuscules, sans espaces autour,
    les espaces intérieurs remplacés par des tirets.

    "  Serveur Paris 01 " -> "serveur-paris-01"
    """
    return "-".join(texte.strip().lower().split())


def compter_mots(texte):
    """Compte les mots d'un texte, sans tenir compte des majuscules ni de la ponctuation.

    "Le chat. Le chien !" -> {"le": 2, "chat": 1, "chien": 1}
    """
    compte = {}
    for mot in texte.lower().split():
        mot = mot.strip(".,;:!?")
        if mot:
            compte[mot] = compte.get(mot, 0) + 1
    return compte


def analyser_dossier(dossier):
    """Parcourt un dossier et ses sous-dossiers, et renvoie des statistiques :
    le nombre de fichiers, leur taille totale en octets, le nombre de fichiers
    par catégorie, et la liste des noms des fichiers de plus de 5 Mo.
    Le dossier .git est ignoré.
    """
    stats = {"total": 0, "taille": 0, "categories": {}, "gros": []}
    for f in sorted(Path(dossier).rglob("*")):
        if not f.is_file() or ".git" in f.parts:
            continue
        taille = f.stat().st_size
        cat = categorie(f.name)
        stats["total"] += 1
        stats["taille"] += taille
        stats["categories"][cat] = stats["categories"].get(cat, 0) + 1
        if taille > LIMITE_GROS_FICHIER:
            stats["gros"].append(f.name)
    return stats

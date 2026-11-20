"""Affiche un rapport sur le contenu d'un dossier.

Usage : python rapport.py <dossier>
"""
import sys

from outils import analyser_dossier, taille_lisible


def main():
    if len(sys.argv) != 2:
        print("Usage : python rapport.py <dossier>")
        sys.exit(1)
    stats = analyser_dossier(sys.argv[1])
    print(f"Rapport du dossier {sys.argv[1]}")
    print(f"{stats['total']} fichiers, {taille_lisible(stats['taille'])} au total")
    for cat, nombre in sorted(stats["categories"].items()):
        print(f"  {cat} : {nombre}")
    if stats["gros"]:
        print("Fichiers volumineux : " + ", ".join(stats["gros"]))


if __name__ == "__main__":
    main()

"""Un exemple de fichier de tests, pour démarrer.

Lancez-le avec : pytest -v
Puis écrivez vos propres tests dans test_outils.py.
"""
import pytest

from outils import moyenne


def test_moyenne_de_deux_notes():
    assert moyenne([10, 20]) == 15


def test_moyenne_liste_vide():
    with pytest.raises(ValueError):
        moyenne([])

import pytest

from outils import taille_lisible

@pytest.mark.parametrize("octets, attendu", [
    (512, "512 o"),
    (1536, "1.5 Ko"),
    (3 * 1024 ** 2, "3.0 Mo"),
])
def test_taille_lisible(octets, attendu):
    assert taille_lisible(octets) == attendu
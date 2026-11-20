from outils import nom_de_machine

def test_nom_de_machine():
    assert nom_de_machine(" Serveur Paris 01 ") == "serveur-paris-01"
    assert nom_de_machine("web") == "web"
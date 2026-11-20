from outils import analyser_dossier

def test_analyser_dossier(tmp_path):
    (tmp_path / "a.py").write_text("print('a')")
    (tmp_path / "notes.txt").write_text("x" * 100)

    stats = analyser_dossier(tmp_path)
    
    assert stats["total"] == 2
    assert stats["taille"] == 110
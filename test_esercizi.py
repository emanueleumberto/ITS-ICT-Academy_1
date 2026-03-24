import pytest
import esercizi

# Contare le occorrenze di un elemento (Ricorsione)
# Scrivi test per:
# ✔ valore presente più volte
# ✔ valore assente
# ✔ lista vuota
# ✔ lista con un solo elemento

def test_valore_presente():
    assert esercizi.conta_elemento([1, 2, 2, 3, 2], 2) == 3
    
def test_valore_assente():
    assert esercizi.conta_elemento([1, 2, 2, 3, 2], 8) == 0
    
def test_lista_vuota():
    assert esercizi.conta_elemento([], 5) == 0
    
def test_lista_un_elemento():
    assert esercizi.conta_elemento([3], 5) == 0
    assert esercizi.conta_elemento([5], 5) == 1
import pytest

# from myFuncForTest import somma
# from myFuncForTest import is_even
import myFuncForTest

def test_somma():
    # assert somma(2,3) == 5
    assert myFuncForTest.somma(2,3) == 5
    
def test_is_even_true():
    # assert is_even(4) is True
    assert myFuncForTest.is_even(4) is True
    
def test_is_even_false():
    # assert is_even(5) is False
    assert myFuncForTest.is_even(5) is False

# pytest permette di teste eccezioni ed errori   
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        myFuncForTest.divide(10,0)
        
@pytest.mark.parametrize("a,b,expected", [
    (1,2,3),
    (2,3,5),
    (10,5,15)
])
def test_somma_params(a, b, expected):
    assert myFuncForTest.somma(a, b) == expected

@pytest.fixture
def sample_data():
    return [1,2,3,4,5]

def test_somma_lista(sample_data):
    assert myFuncForTest.somma_lista(sample_data) == 15
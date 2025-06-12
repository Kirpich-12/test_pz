from code_1 import sqrt as equalize
import pytest

def test_pos_int_dif():
    assert equalize(1,2) == 5.1962
def test_neg_int_num():
    assert equalize(2, -1) == 0.3333
def test_pos_int_sim():
    with pytest.raises(ZeroDivisionError):
        assert equalize(2,2) == 'Не дели блет на 0'
def test_pos_float_num():
    assert equalize(0.2, 0.1) == 1.6432
def test_neg_root():
    assert equalize(1, -2) == 'Компл область'
def test_er_inp():
    assert equalize('sdass', '0')
    assert equalize('', '0')





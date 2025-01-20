# Fonction test du résultat de 2 + 4
def test_calc_addition():
    output = 1 + 4
    assert output == 5 


# Fonction test du résultat de 2 - 4
def test_calc_subtraction():
    output = 2 - 4
    assert output == -2


# Fonction test du résultat de 2 * 4
def test_calc_multiply():
    output = 2 * 4
    assert output == 8


# Fonction test si la résultat renvoie 'hello'
def test_coucou():
    output = 'hello'
    assert output == 'hello'

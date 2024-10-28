from Project1 import median, average, prop_above

def test_median():
    assert median([1,2,3,4,5,6]) == 3.5
    assert median([1.0,2.0,3.0,4.0,5.0,6.0,7.0]) == 4.0

def test_average():
    assert average([1,2,3,4,5,6]) == 3.5
    assert average([1,2,3,4,5,6,7]) == 4

def test_prop_above():
    assert prop_above([1,2,3,4,5,6]) == 0.5
    assert prop_above([1,2,3,4,5,6,7]) == 3/7


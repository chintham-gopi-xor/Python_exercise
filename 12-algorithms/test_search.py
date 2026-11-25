from exercise1 import linear_search, binary_search


def test_linear_search_found():
    index, comp = linear_search(150)

    assert index == 75
    assert comp == 75


def test_binary_search_found():
    index, comp = binary_search(150)

    assert index == 75
    assert comp >= 0


def test_linear_search_not_found():
    index, comp = linear_search(151)

    assert index == -1
    assert comp == 100


def test_binary_search_not_found():
    index, comp = binary_search(151)

    assert index == -1
    assert comp >= 0


def test_linear_search_first_element():
    index, comp = linear_search(0)

    assert index == 0
    assert comp == 0


def test_binary_search_first_element():
    index, comp = binary_search(0)

    assert index == 0


def test_linear_search_last_element():
    index, comp = linear_search(198)

    assert index == 99


def test_binary_search_last_element():
    index, comp = binary_search(198)

    assert index == 99
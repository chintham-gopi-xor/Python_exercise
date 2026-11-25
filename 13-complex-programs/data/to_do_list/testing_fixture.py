

def test_list_has_three_items(shopping_list):
    assert len(shopping_list) == 3


def test_bread_is_present(shopping_list):
    assert "bread" in shopping_list


def test_chocolate_not_present(shopping_list):
    assert "chocolate" not in shopping_list
import pytest
import sys
sys.path.append('C:/Users/utilisateur/Documents/briefs/UnitTest/module')
import panier as pa


@pytest.fixture()
def panier():
    panier = pa.Panier()
    return panier


def test_add_item_passes_where_item_is_string(panier):
    panier.add_item('a', 1, 1)
    assert len(panier.articles) == 1
    assert panier.articles[0]['item'] == 'a'


def test_add_item_fails_where_item_is_not_string(panier):
    with pytest.raises(Exception):
        panier.add_item(1, 1, 1)

def test_add_item_passes_where_nbr_items_and_price_are_numeric(panier):
    panier.add_item('a', 1, 1)
    assert len(panier.articles) == 1
    assert isinstance(panier.articles[0]['nbr_item'], int)
    assert isinstance(panier.articles[0]['price'], float)

def test_add_item_passes_where_nbr_item_is_numeric(panier):
    panier.add_item("a", 1, 1)
    assert len(panier.articles) == 1
    assert panier.articles[0]['nbr_item'] == 1


def test_add_item_fails_where_nbr_item_is_not_numeric(panier):
    with pytest.raises(Exception):
        panier.add_item("a", "b", 1)


def test_add_item_fails_where_nbr_item_is_negative(panier):
    with pytest.raises(Exception):
        panier.add_item("a", -1, 1)


def test_add_item_passes_where_price_is_numeric(panier):
    panier.add_item("a", 1, 1)
    assert len(panier.articles) == 1
    assert panier.articles[0]['price'] == 1


def test_add_item_fails_where_price_is_not_numeric(panier):
    with pytest.raises(Exception):
        panier.add_item("a", 1, "c")


def test_add_item_fails_where_nbr_item_is_negative(panier):
    with pytest.raises(Exception):
        panier.add_item("a", 1, -1)



def test_add_item_passes_add_nbr_item_to_id_item_already_exists(panier):
    panier.add_item("a", 1, 1)
    panier.add_item("b", 1, 1)
    panier.add_item("a", 1, 1)
    nbr_item_a = panier.articles[0]['nbr_item']
    nbr_item_b = panier.articles[1]['nbr_item']
    assert nbr_item_a == 2
    assert nbr_item_b == 1


def test_calculate_total_passes_where_items_exists(panier):
    panier.add_item("a", 1, 10)
    panier.add_item("b", 2, 20)
    panier.add_item("a", 2, 10)
    total = sum(p['price'] * p['nbr_item'] for p in panier.articles)
    assert total == 70


def test_calculate_total_passes_where_no_items_exists(panier):
    total = sum(p['price'] * p['nbr_item'] for p in panier.articles)
    assert total == 0


def test_display_items_return_empty_where_no_items_exists(panier):
    assert len(panier.articles) == 0


def test_display_items_return_a_list_where_items_exists(panier):
    panier.add_item("a", 1, 10)
    panier.add_item("b", 2, 20)
    assert len(panier.articles) != 0


def test_remove_item_passes_where_item_exists(panier):
    panier.add_item("a", 1, 10)
    panier.add_item("b", 2, 20)
    assert len(panier.articles) == 2
    assert panier.articles[0]['item'] == 'a'
    assert panier.articles[1]['item'] == 'b'
    panier.remove_item('a')
    assert len(panier.articles) == 1
    assert panier.articles[0]['item'] == 'b'


def test_remove_item_passes_where_item_not_exists(panier):
    panier.add_item("a", 1, 10)
    panier.add_item("b", 2, 20)
    assert len(panier.articles) == 2
    panier.remove_item('c')
    assert len(panier.articles) == 2


def test_update_quantity_passes_where_item_exists_and_quantity_valid(panier):
    panier.add_item("a", 1, 10)
    assert panier.articles[0]['nbr_item'] == 1
    panier.update_quantity('a', 2) 
    assert panier.articles[0]['nbr_item'] == 2


def test_update_quantity_where_item_exists_and_quantity_not_valid(panier):
    panier.add_item("a", 1, 10)
    assert panier.articles[0]['nbr_item'] == 1
    with pytest.raises(Exception):
        panier.update_quantity('a', 'b')
    

def test_update_quantity_failed_where_quantity_is_negative(panier):
    panier.add_item("a", 1, 10)
    assert panier.articles[0]['nbr_item'] == 1
    with pytest.raises(Exception):
        panier.update_quantity('a', -1)


def test_update_quantity_remove_item_where_quantity_is_0(panier):
    panier.add_item("a", 1, 10)
    assert len(panier.articles) == 1
    panier.update_quantity('a', 0)
    assert len(panier.articles) == 0
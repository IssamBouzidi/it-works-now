import pytest
import json
from flask import request, jsonify
import sys
sys.path.append('C:/Users/utilisateur/Documents/briefs/UnitTest/module')
import panier as pa


@pytest.fixture()
def panier():
    panier = pa.Panier()
    panier.add_item('Phone', 3, 200)
    return panier


def test_index(app, client):
    res = client.get('/')
    assert res.status_code == 200
    expected = {'hello': 'world'}
    assert expected == json.loads(res.get_data(as_text=True))


def test_get_list_articles(app, client, panier, articles):
    url = "/api/articles"
    response = client.get(
        url,
        content_type='application/json'
    )
    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert len(data['result']) == 3
    assert data['result'][0] == articles[0]
    assert data['result'][1] == articles[1]
    assert data['result'][2] == articles[2]


def test_add_new_article(app, client):
    url = "/api/articles"
    new_item = {'item':'HiFi', 'nbr_item': 3, 'price': 400.0}
    response = client.post(
        url,
        data=json.dumps(new_item),
        content_type='application/json'
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert len(data['result']) == 4
    assert new_item in data['result']


def test_get_item(app, client, articles):
    url = "/api/articles/Laptop"
    response = client.get(
        url,
        data='Laptop',
        content_type='application/json'
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert len(data['result']) == 1
    assert data['result'][0]['item'] == 'Laptop'
    assert data['result'][0]['nbr_item'] == 2
    assert data['result'][0]['price'] == 1200.0


def test_modify_item_quantity(app, client, articles):
    url = "/api/articles"
    response = client.put(
        url,
        data=json.dumps({'item':articles[1]['item'], 'nbr_item': 4}),
        content_type='application/json'
    )

    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert len(data['result']) == 1
    assert data['result'][0]['item'] == articles[1]['item']
    assert articles[1]['nbr_item'] == 2
    assert data['result'][0]['nbr_item'] == 4
    assert data['result'][0]['price'] == articles[1]['price']


def test_remove_item(app, client, articles):
    url = "/api/articles"
    response = client.delete(
        url,
        data=json.dumps({'item':articles[1]['item']}),
        content_type='application/json'
    )
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert len(data['result']) == 2
    assert articles[1] not in data['result']
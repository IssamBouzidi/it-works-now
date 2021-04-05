import pytest
import sys
sys.path.append('C:/Users/utilisateur/Documents/briefs/UnitTest')

from app import app as flask_app
from module.panier import Panier


@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture()
def panier():
    panier = Panier()
    return panier


@pytest.fixture()
def articles():
    panier = Panier()
    panier.add_item('Phone', 3, 200)
    panier.add_item('Laptop', 2, 1200)
    panier.add_item('TV', 3, 400)
    return panier.articles
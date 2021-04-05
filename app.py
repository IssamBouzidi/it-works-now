from flask import Flask, jsonify, request
from module.panier import Panier

panier = Panier()

app = Flask(__name__)
articles = {}

@app.route('/')
def index():
    return jsonify({'hello': 'world'})


@app.route('/api/articles', methods=['GET', 'POST', 'PUT', 'DELETE'])
def list_articles():
    """a route that manage articles
        Display a list,
        Add a new item
        Modify quantity
        Remove an itemm
    Returns:
        List: List of articles
    """
    articles = initialize_articles()
    if request.method == 'GET':
        return jsonify(result=articles)

    if request.method == 'POST':
        data = request.get_json() 
        item = data['item']
        nbr_item = data['nbr_item']
        price = data['price']
        panier.add_item(item, nbr_item, price)
        return jsonify(result=panier.articles)
        
    if request.method == 'PUT':
        data = request.get_json() 
        item = data['item']
        quantity = data['nbr_item']
        item_updated = panier.update_quantity(item, quantity)
        return jsonify(status="True", result=panier.display_item(item))

    if request.method == 'DELETE':
        data = request.get_json() 
        item = data['item']
        new_list = panier.remove_item(item)
        return jsonify(result=new_list)


@app.route('/api/articles/<item>', methods=['GET'])
def display_item(item):
    """A method to return an item
    Args:
        item (String): Name of an article
    Returns:
        item: item object
    """
    articles = initialize_articles()
    return jsonify(status="True", result=panier.display_item(item))


def initialize_articles():
    """initialize a list of article to be sused for tests
    Returns:
        List: a list of articles
    """
    panier.articles = [
        {'item': 'Phone','nbr_item': 3,'price': 200},
        {'item': 'Laptop','nbr_item': 2,'price': 1200},
        {'item': 'TV','nbr_item': 3,'price': 400},
    ]
    return panier.articles


if __name__ == "__main__":
    articles = initialize_articles()
    app.run(debug=True)
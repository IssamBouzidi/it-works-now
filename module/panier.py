class Panier:
    """Class Panier
        Allow to manage a shopping cart
    """
    def __init__(self):
        self.articles = []

    def add_item(self, item, nbr_of_items, price):
        """a void method to add a new item

        Args:
            item (string): item name
            nbr_of_items (int): number of item to add
            price (float): price for one item

        Raises:
            Exception: Parameter type is not valid!
            Exception: Numbre of items and price can not be negative
        """

        # parameters initialization
        nbr_of_items = nbr_of_items
        price = float(price)
        index = -1

        # testing id item informations type are valid
        if (not isinstance(item, str)
        or not isinstance(nbr_of_items, int) 
        or not isinstance(price, float)):
            raise Exception ('Parameter type is not valid!')
        
        # testing if numnber of item and price are positifs
        if(not nbr_of_items > 0 or not price > 0):
            raise Exception('Numbre of items and price can not be negative')

        # get item if already exist
        index_item = self.__is_item_exists(item)

        # if item dos not exist, add it to list of articles
        if index_item == -1:
            self.articles.append({
                'item': item,
                'nbr_item': nbr_of_items,
                'price': price
            })
        else:
            # if item exists, add only number of items
            self.articles[index_item]['nbr_item'] += nbr_of_items


    def __is_item_exists(self, item):
        """private method to test if an item exists
        Args:
            item (String): name of item
        Returns:
            int: return index of item if it exists, else, return -1
        """
        index = -1
        for index, article in enumerate(self.articles):
            if article['item'] == item:
                return index
        return -1


    def remove_item(self, item):
        """Remove item method
        Args:
            item (Stirng): Name of item
        Returns:
            List: list of articles
        """
        self.articles = [article for article in self.articles if article['item'] != item]
        return self.articles


    def display_items(self):
        return self.articles
    
    def display_item(self, item):
        """Return an item from list of articles
        Args:
            item (String): Name of item
        Returns:
            item object: Item from list of articles if it exists
        """
        selected_item = [article for article in self.articles if article['item'] == item]
        return selected_item

    def calculate_total(self):
        """Method to calculate total of the shopping cart
        Returns:
            int: Sum of the prices of items in shopping cart 
        """
        return sum(p['price'] for p in panier.articles)

    def update_quantity(self, item, new_quantity):
        """Method to modify quantity of an item
        Args:
            item (String): Name of item
            new_quantity (int): New quantity

        Raises:
            Exception: Parameter type is not valid!
            Exception: Quanity must be greater than 0!

        Returns:
            List: list of articles updated
        """

        if not isinstance(new_quantity, int):
            # if the quantity is not a valid type 
            raise Exception ('Parameter type is not valid!')
        elif new_quantity < 0:
            # if the new quantity is negative
            raise Exception ('Quanity must be greater than 0!')
        elif new_quantity == 0:
            # if the new quantity is 0, so remove the article
            self.remove_item(item)
        else:
            # is the quantity is greater than 0, modify the quantity
            for index, article in enumerate(self.articles):
                if article['item']==item:
                    self.articles[index]['nbr_item']=new_quantity

        return self.articles
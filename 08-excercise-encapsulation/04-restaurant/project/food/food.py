from project.product import Product

class Food(Product):
    def __init__(self, name, price, grams):
        self.__grams = grams
        super().__init__(name, price)
        
    @property
    def grams(self):
        return self.__grams
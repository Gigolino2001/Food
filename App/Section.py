from Product import Product
class Section:
    def __init__(self,number, categorie):
        self.__number = number
        self.__categorie = categorie
        self.__product = []
        self.__local = "To be defined"

    def get_number(self):
        return self.__number

    def get_categorie(self):
        return self.__categorie

    def get_local(self):
        return self.__local

    def add_product(self,Product):
        self.__product.append(Product)

    def get_products(self):
        return self.__product
    
    def set_categorie(self, categorie):
        self.__categorie = categorie

    def set_local(self, local):
        self.__local = local

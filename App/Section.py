class Section:
    def __init__(self,number, categorie):
        self.__number = number
        self.__categorie = categorie
        self.__product = []

    def get_number(self):
        return self.__number

    def get_categorie(self):
        return self.__categorie

    def add_product(self,Product):
        self.__product.append(Product)
        
    def get_product(self):
        return self.__food
    
    def set_categorie(self, categorie):
        self.__categorie = categorie

class Section:
    def __init__(self,number):
        self.__number = number
        self.__categorie = None
        self.__food = []

    def get_number(self):
        return self.__number

    def get_categorie(self):
        return self.__categorie
    
    def get_food(self):
        return self.__food
    
    def set_categorie(self, categorie):
        self.__categorie = categorie

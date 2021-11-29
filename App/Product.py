class Product:
    def __init__(self,name,id,cost,section_number):
        self.__name = name
        self.__id = id
        self.__cost = cost
        self.__section_number = section_number
        
    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_section_number(self):
        return self.__section_number
    
    def get_cost(self):
        return self.__cost
    
    def set_cost(self,price):
        if price > 0:
            self.__cost = price
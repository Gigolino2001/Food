class Supermarket:
    def __init__(self):
        self.__sections = []
        self.__money_per_day = 1
        self.__costs_per_day = 2

    def get_money_per_day(self):
        return self.__money_per_day
    
    
    def get_costs_per_day(self):
        return self.__costs_per_day
    
    def get_sections(self):
        return self.__sections
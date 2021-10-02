from Section import Section

SECTION_SIZE = 26
ASCII_NUMBER = 65

class Supermarket:
    
    def __init__(self):
        self.__name = None
        self.__sections = self.create_sections()
        self.__money_per_day = 0
        self.__costs_per_day = 0

    def create_sections(self):
        sections = []
        for x in list(range(SECTION_SIZE)):
            sections.append(Section(x,chr(ASCII_NUMBER + x)))
        return sections

    def add_section(self,name):
        self.__sections.append(Section(len(self.__sections)))
        self.__sections[-1].set_categorie(name)

    def get_sections_by_name(self):
        cpy_sections = sorted(self.__sections, key=lambda x: (x.get_categorie()).casefold())
        return cpy_sections


    def set_name(self,name):
        self.__name = name

    def get_name(self):
        return self.__name

    def get_money_per_day(self):
        return self.__money_per_day
    
    def get_costs_per_day(self):
        return self.__costs_per_day
    
    def get_sections(self):
        return self.__sections

    

from Supermarket import Supermarket
from Section import Section

class Menu:
    
    def __init__(self):
        self.__options = {
        1: 'Create a Supermarket',
        2: 'Show money earned per day',
        3: 'Show costs per day',
        4: 'Show all sections',
        5: 'Name Section',
        6: 'Exit',
    }

    def print_menu(self):
        for key in self.__options.keys():
            print (key, '--', self.__options[key])

    def start(self):
        supermarket = None
        while(True):
            self.print_menu()
            option = ''
            try:
                option = int(input('Enter your choice: '))
            except:
                print('->Wrong input. Please enter a number between 1 and 5')
            if option == 1:
                supermarket = Supermarket()
                print("-> Supermarket created.\n")
            elif option == 2:
                try:
                    print("-> " + str(supermarket.get_money_per_day()) + "\n")
                except:
                    print("-> You have to create a Supermarket before.\n")
            elif option == 3:
                try:
                    print("-> " + str(supermarket.get_costs_per_day()) + "\n")
                except:
                    print("-> You have to create a Supermarket before.\n")
            
            elif option == 4:
                try:
                    for section in supermarket.get_sections():
                        print("-> " + str(section.get_number()) + " - " + str(section.get_categorie()))
                    print()
                except:
                    print("-> You have to create a Supermarket before.\n")
            
            elif option == 5:
                try:
                   sections = supermarket.get_sections() #### Stoped Here ######
                   sections[25].set_categorie("Oi")
                except:
                    print("-> You have to create a Supermarket before.\n")


            elif option == 6:
                print('Thank you for using the app!"')
                exit()
            else:
                print('Wrong input. Please enter a number between 1 and 5')

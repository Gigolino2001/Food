from Supermarket import Supermarket
from Section import Section

class Menu:
    
    def __init__(self):
        self.__options = {
        1: 'Name Supermarket',
        2: 'Show money earned per day',
        3: 'Show costs per day',
        4: 'Show all sections sorted by number',
        5: 'Show all sections by alphabetical order',
        6: 'Name Section',
        7: 'Add Section',
        8: 'Exit'
    }

    def print_menu(self):
        for key in self.__options.keys():
            print (key, '--', self.__options[key])

    def start(self):
        supermarket = Supermarket()
        while(True):
            self.print_menu()
            option = ''
            try:
                option = int(input('Enter your choice: '))
            except:
                print('-> Wrong input. Please enter a number between 1 and 5')
            if option == 1:
                try:
                    name_Supermarket = str(input('Enter the name of the Supermarket: '))
                    supermarket.set_name(name_Supermarket)
                except:
                    print('-> Please enter a valid name.')
            elif option == 2:
                print("-> " + str(supermarket.get_money_per_day()) + "\n")

            elif option == 3:
                print("-> " + str(supermarket.get_costs_per_day()) + "\n")
            
            elif option == 4:
                name = supermarket.get_name()
                if not (isinstance(name, type(None))):
                    print("\n↓ SUPERMARKET " + str(name).upper() + " SECTIONS BY NUMBER ↓")
                    for section in supermarket.get_sections():
                        print("-> " + str(section.get_number()) + " - " + str(section.get_categorie()))
                    print()
                else:
                    print("-> Please enter the supermarket name first.")
            
            elif option == 5:
                name = supermarket.get_name()
                if not (isinstance(name, type(None))):
                    print("\n↓ SUPERMARKET " + str(name).upper() + " SECTIONS BY NAME↓")
                    for section in supermarket.get_sections_by_name():
                        print("-> " + str(section.get_number()) + " - " + str(section.get_categorie()))
                    print()
                else:
                    print("-> Please enter the supermarket name first.")


            elif option == 6:
                sections = supermarket.get_sections()
                try:
                    number_section = int(input('Enter the number of the section between 0 and '+ str(len(sections)-1) + ': '))
                    name_section = str(input('Enter the name of the section: '))
                    name_before = sections[number_section].get_categorie()
                    sections[number_section].set_categorie(name_section)
                    print('-> Changes made: ' + str(name_before) + ' ----> ' + name_section + '\n')
                except:
                   print('-> Please enter valid arguments.')

            elif option == 7:
                try:
                    name_section = str(input('Enter the name of the section: '))
                    supermarket.add_section(name_section)
                    print('-> Section added.')
                except:
                    print('-> Please enter a valid name.')

            
            elif option == 8:
                print('Thank you for using the app!"')
                exit()
            else:
                print('-> Wrong input. Please enter a number between 1 and 7')

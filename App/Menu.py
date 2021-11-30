from Product import Product
from Supermarket import Supermarket

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
        8: 'Add Product',
        9: 'Show Product',
        10: 'Show All Products',
        11: 'Exit'
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
                print('-> Wrong input. Please enter a number between 1 and 9')
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
                    sections = supermarket.get_sections()
                    cpy_sections = sorted(sections, key=lambda x: (x.get_categorie()).casefold())
                    for section in cpy_sections:
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
                    print('-> Please enter a valid argument.')
            elif option == 8:
                try:
                    name_product = str(input('Enter the name of the product: '))
                    id_product = int(input('Enter the product ID: '))
                    cost = int(input('Enter the price: '))
                    name_section = str(input('Enter the section name that stores this product: '))
                    flag_existing_section = 0
                    sections = supermarket.get_sections()
                    for section in sections:
                        if section.get_categorie().lower() == name_section.lower():
                            flag_existing_section = 1
                            product = Product(name_product,id_product,cost,section.get_number())
                            section.add_product(product)
                            print('-> Product added.')
                    if flag_existing_section == 0:
                        print("-> Your section doesn't exist.")
                except:
                    print('-> Please enter a valid arguments.')
            
            elif option == 9:
                name = supermarket.get_name()
                try:       
                    prod_name = str(input("Enter the product name: "))
                    print("\n↓ SUPERMARKET " + str(name).upper() + " SECTIONS BY NUMBER ↓")
                    for section in supermarket.get_sections():
                        print("-> " + str(section.get_number()) + " - " + str(section.get_categorie()))
                    print()
                    prod_categorie = int(input("Select the number of the product categorie: "))
                    sections = supermarket.get_sections()
                except:
                    print('-> Please enter a valid arguments.')
                    continue
                try:
                    flag_existing_section = 0
                    for products in sections[prod_categorie].get_products():
                        if prod_name.lower() == products.get_name().lower():
                            flag_existing_section = 1
                            print("ID: " + str(products.get_id()))
                            print("Name: " + str(products.get_name()))
                            print("Section: "+ str(prod_categorie) + " - " + str(sections[prod_categorie].get_categorie()))
                            print("Cost: " + str(products.get_cost()))
                    if flag_existing_section == 0:
                        print("-> Sorry, but the product doesn't exist in this categorie.")
                except:
                    print('-> Please enter a valid categorie number.')
            elif option == 10:
                name = supermarket.get_name()       
                print("\n↓ SUPERMARKET " + str(name).upper() + " PRODUCTS ↓")
                for section in supermarket.get_sections():
                    for product in section.get_products():
                        print("-> " + str(product.get_id()) + " - " + str(product.get_name()))
                print()
   
            elif option == 11:
                print('Thank you for using the app!"')
                exit()
            else:
                print('-> Wrong input. Please enter a number between 1 and 11')

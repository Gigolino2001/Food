class Menu:
    
    def __init__(self):
        self.options = {
        1: 'Option 1',
        2: 'Option 2',
        3: 'Option 3',
        4: 'Option 4',
        5: 'Exit',
    }

    def print_menu(self):
        for key in self.options.keys():
            print (key, '--', self.options[key])

    def start(self):
        while(True):
            self.print_menu()
            option = ''
            try:
                option = int(input('Enter your choice: '))
            except:
                print('Wrong input. Please enter a number between 1 and 5')
            if option == 1:
                print(1)
            elif option == 2:
                print(2)
            elif option == 3:
                print(3)
            elif option == 4:
                print(4)
            elif option == 5:
                print('Thank you for using the app!"')
                exit()
            else:
                print('Wrong input. Please enter a number between 1 and 5')

if __name__ == '__main__':
    menu = Menu()
    menu.start()
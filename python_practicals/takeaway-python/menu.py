class Menu:
    
    def __init__(self):
        self.list =  {
        "Pizza" : 9,
        "Burger" : 10
    }
    def view(self):
        print("Tonight's Menu: ")
        for key, value in self.list.items():
            print(f"{key}, £{value}")
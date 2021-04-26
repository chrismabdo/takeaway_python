from menu import Menu

class Basket:
    def __init__(self, menu=Menu()):
      self.cart = []
      self.menu = menu
      self.total = 0
    
    def add_item(self, item, quantity):
        if item in self.menu.list:
          self.cart += quantity * [item]
          self.total += (quantity * self.menu.list[item])
        else:
          print("Item not available. Please Choose another item")
    
    def check_total(self):
      return f"Your Total Comes to £{self.total}"
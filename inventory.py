class Inventory:
    
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"{item} has been added to your inventory.")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"{item} has been removed from your inventory.")
        else:
            print(f"{item} is not in your inventory.")

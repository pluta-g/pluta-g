import random

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    
def random_item():

    items = [
        Item("Sword", "A sharp sword, This should help you in your journey"),
        Item("Potion of Healing", "you get the idea"),
        Item("Gold", "ooooooh shiny")
    ]
    return random.choice(items)
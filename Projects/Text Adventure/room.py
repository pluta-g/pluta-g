import random

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.exits = {}

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            return item
        return None

    def add_exit(self, direction, room):
        self.exits[direction] = room

    def get_exits(self):
        return self.exits
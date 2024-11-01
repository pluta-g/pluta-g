from random import randint
from game_save import GameState, save_game, load_game
from inventory import Inventory
from items import Item, random_item
from room import Room

def main():
    pass

if __name__ == '__main__':
    main()



room1 = Room("Cave Enterance", "As you step into the cave entrance you hear an eery noise from up ahead")
room2 = Room("Room 2", "N/A")
room3 = Room("Room 3", "N/A")
room4 = Room("Room 4", "N/A")
room5 = Room("Room 5", "N/A")
room6 = Room("Room 6", "N/A")
room7 = Room("Room 7", "N/A")
room8 = Room("Room 8", "N/A")
room9 = Room("Room 9", "N/A")
room10 = Room("Room 10", "N/A")
room11 = Room("Room 11", "N/A")
room12 = Room("Room 12", "N/A")
room13 = Room("Room 13", "N/A")
room14 = Room("Room 14", "N/A")
room15 = Room("Room 15", "N/A")
room16 = Room("Room 16", "N/A")
room17 = Room("Room 17", "N/A")
room18 = Room("Room 18", "N/A")
room19 = Room("Room 19", "N/A")
room20 = Room("Room 20", "N/A")
room21 = Room("Room 21", "N/A")
room22 = Room("Room 22", "N/A")

for room in [room1, room2, room3, room4, room5, room6, room7, room8, room9, room10, room11, room12, room13, room14, room15, room16, room17, room18, room19, room20, room21, room22]:
  for _ in range(randint(1, 3)):
    room.add_item(random_item())

room1.add_exit('west', room2)
room1.add_exit('east', room3)
room2.add_exit('east', room1)
room3.add_exit('south', room4)
room3.add_exit('west', room1)
room4.add_exit('south', room5)
room4.add_exit('north', room3)
room5.add_exit('west', room6)
room5.add_exit('north', room4)
room6.add_exit('west', room7)
room6.add_exit('east', room5)
room7.add_exit('east', room6)
room7.add_exit('south', room8)
room8.add_exit('north', room7)
room8.add_exit('south', room11)
room8.add_exit('east', room9)
room9.add_exit('west', room8)
room11.add_exit('north', room8)
room11.add_exit('south', room12)
room12.add_exit('north', room11)
room12.add_exit('east', room13)
room13.add_exit('west', room12)
room13.add_exit('east', room14)
room14.add_exit('west', room13)
room14.add_exit('north', room15)
room15.add_exit('south', room14)
room15.add_exit('north', room10)
room16.add_exit('west', room10)
room16.add_exit('east', room17)
room17.add_exit('west', room16)
room17.add_exit('east', room18)
room18.add_exit('west', room17)
room18.add_exit('north', room19)
room19.add_exit('south', room18)
room19.add_exit('north', room20)
room20.add_exit('south', room19)
room20.add_exit('east', room21)
room21.add_exit('east', room22)
room21.add_exit('west', room20)
room22.add_exit('east', room21)

rooms = {
  "room1" : room1,
  "room2" : room2,
  "room3" : room3,
  "room4" : room4,
  "room5" : room5,
  "room6" : room6,
  "room7" : room7,
  "room8" : room8,
  "room9" : room9,
  "room10" : room10,
  "room11" : room11,
  "room12" : room12,
  "room13" : room13,
  "room14" : room14,
  "room15" : room15,
  "room16" : room16,
  "room17" : room17,
  "room18" : room18,
  "room19" : room19,
  "room20" : room20,
  "room21" : room21,
  "room22" : room22,

}

#Base class for all characters
class Character:
  def __init__(self):
    #charaters name
    self.name = ""
    #Current health points
    self.health = 1
    #Maximum health points
    self.health_max = 1

    #Method to preform an attack on an enemy. 
  def do_damage(self, enemy):
    #Calculates damage inflicted based on random integers.
    damage = min(max(randint(0, self.health) - randint(0, enemy.health), 0), enemy.health)
    enemy.health -= damage

    #Message if the attack misses
    if damage == 0:
       print(f"{enemy.name} evades {self.name}'s attack")
    
    #Message if the attack hits.
    else: 
      print (f"{self.name} hurts {enemy.name}!")
    
    #Returns true if the enemy is defeated
    return enemy.health <= 0

#Enemy class inherits from the Character
class Enemy(Character):
  
  def __init__(self, player):

    #Initializes the base Character class
    super().__init__()

    #Sets a default name for the enemy
    self.name = 'a goblin'

    #Randomizes enemy health based on player's health.
    self.health = randint(1, player.health)

#Player class inherits from character.
class Player(Character):
  def __init__(self):
    #initializes the base character class.
    super().__init__()
    #Sets initial state of the player.
    self.state = 'normal'
    #Sets player's initial health
    self.health = 10
    #Sets the player's maximum health.
    self.health_max = 10
    #Ensure Inventory is defined correctly
    self.inventory = Inventory()
    self.name = ""
    self.enemy = None
    self.current_room = ""

  def move(self, direction):
    current_room = rooms[self.current_room]
    if direction in current_room.get_exits():
      new_room = current_room.get_exits()[direction].name
      self.set_current_room(new_room)
      print(f"{self.name} moves {direction} to {new_room.name}.")
    else:
      print(f"There is no exit in that direction: {direction}")

  def show_inventory(self):
    self.inventory.list_items()

  def pickup(self, item_name):
    current_room = rooms[self.current_room]
    item_to_pickup = next((item for item in current_room.items if item.name == item_name), None)
    if item_to_pickup:
      self.inventory.add_item(item_to_pickup)
      current_room.remove_item(item_to_pickup)
    else:
      print(f"{item_name} is not available to pick up in this room")

  def drop(self, item_name):
    self.inventory.remove_item(item_name)

  def set_current_room(self, room_name):
    self.current_room = room_name

    #Player method to quit the game.
  def quit(self):
    print (f"{self.name} has quit the game.")
    
    #sets health to 0, indicating death.
    self.health = 0

    #displays all commands.
  def help(self): 
    print (Commands.keys())

  #Displays player's health status.
  def status(self): 
    print (f"{self.name}'s health: {self.health}/{self.health_max}")
  
  
  def tired(self):
    #Message indicating the player is tired
    print (f"{self.name} feels tired.")
    #Reduces health by 1 but ensures it doesn't drop below 1
    self.health = max(1, self.health - 1)

    #Method for resting
  def rest(self):
    if self.state != 'normal': 
      #Can't rest if in combat.
      print (f"{self.name} can't rest now!") 
      #Enemy attacks if the player cannot rest.
      self.enemy_attacks()
    else:
      #Message indicating the player is resting.
      print (f"{self.name} rests.")
      #Random chance of being interrupted by an enemy.
      if randint(0, 1):
        #Creates a new enemy instance.
        self.enemy = Enemy(self)
        #Message for interruption
        print (f"{self.name} is rudely awakened by {self.enemy.name}!")
        #Changes state to fighting
        self.state = 'fight'
        self.enemy_attacks()

      else:

        if self.health < self.health_max:
          #Restores health if below maximum
          self.health = self.health + 1
        
        #Message if health is at max.
        else: print (f"{self.name} slept too much.") 
        #Decrease health for resting.
        self.health = self.health - 1
  
  #Method for fleeing from a fight.
  def flee(self):
    if self.state != 'fight': 
      
      #Message if not fighting.
      print (f"{self.name} runs in circles for a while.")
      
      #Player get tired from running.
      self.tired()
    else:
      
      #Determines if the player successfully flees based on random rolls.
      if randint(1, self.health + 5) > randint(1, self.enemy.health):
       
       #Successful escape message.
        print (f"{self.name} flees from {self.enemy.name}.")
        
        #No longer has an enemy.
        self.enemy = None
        
        #State reset to normal.
        self.state = 'normal'
      else: 
        
        #Failure message
        print (f"{self.name} couldn't escape from {self.enemy.name}!") 
      
      #Enemy attacks if the player fails to flee
      self.enemy_attacks()
  
  #Method for attacking an enemy.
  def attack(self):
    if self.state != 'fight': 
      
      #Message if not in a fight.
      print (f"{self.name} swats the air, without notable results.")
      
      #Player gets tired from missing the attack.
      self.tired()
    else:
      
      #If the player attacks and potentially defeats an enemy.
      if self.do_damage(self.enemy):
        
        #Victory Message.
        print (f"{self.name} executes {self.enemy.name}!")
        
        #No longer has an enemy.
        self.enemy = None
        
        #Reset state to normal.
        self.state = 'normal'
        
        #Random chance to increase health after victory.
        if randint(0, self.health) < 10:
          self.health = self.health + 1
          self.health_max = self.health_max + 1
          
          #Message indicating health increase.
          print (f"{self.name} feels stronger!")
      else: 
        
        #If the enemy survives, they attack back.
        self.enemy_attacks()
  
  #Method for the enemy's attacks
  def enemy_attacks(self):
    
    #Checks if the enemy's attack defeats the player.
    if self.enemy.do_damage(self): 
      
      #Death message.
      print (f"{self.name} was slaughtered by {self.enemy.name}!!!\nR.I.P.")

  

#Dictionary mapping command names to player methods for easy access.
Commands = {
  'quit': Player.quit,
  'help': Player.help,
  'status': Player.status,
  'rest': Player.rest,
  'flee': Player.flee,
  'attack': Player.attack,
  'inventory': Player.show_inventory,
  'pickup': lambda player, item: player.pickup(item),
  'drop': lambda player, item: player.drop(item),
  'save' : lambda player: save_game(GameState(player.name, []), get_save_filename()),
  'load' : lambda: load_game(get_save_filename()),
  'north' : lambda player: player.move('north'),
  'south' : lambda player: player.move('south'),
  'east' : lambda player: player.move('east'),
  'west' : lambda player: player.move('west')

  }



#Creates a title screen and displays options
def title_screen():
  print("Welcome to PLACEHOLDER NAME")
  print("1. Start a new game")
  print("2. Load a previous game")

  choice = input("\nChoose an option (1 or 2)\n")
  return choice

#If the option to start a new game is selected this starts the game
def start_new_game():
  new_player = Player()
  new_player.name = input("What would you like to name your character \n")
  print(f"{new_player.name} enters a dark cave, searching for adventure.")

  new_player.set_current_room("room1")
  return new_player

#Grabs the players previous save data
def load_game_state():
  filename = get_save_filename()
  game_state = load_game(filename)
  if game_state:
    player = Player()
    player.name = game_state.player_name
    player.health = 10
    print(f"The adventure continues, {player.name}!")
    return player
  
  else:
    print("failed to load the game. Please try again")
    return None
  
def get_save_filename():
  return input("Enter the save filename (e.g., savegame_player.log):")

player = Player()
player.set_current_room("room1")

def describe_current_room(player):
  current_room = rooms[player.current_room]
  print(f"You are in {current_room.name}: {current_room.description}")
  if current_room.items:
    print("You see items litering the floor:")
    for item in current_room.items:
      print(f"- {item.name}: {item.description}")
  else:
    print("The room is empty.")
  print("Exits:", ', '.join(current_room.get_exits()))

while True:
  choice = title_screen()

  if choice == '1':
    #Start a new game
    player = start_new_game()
    break

  elif choice == '2':
    #Load a previous game
    player = load_game_state()
    if player:
      break
      
  else:
    print("Invalid choice, please try again.")

#Main game loop that continues while the players health is greater than 0.
while(player.health > 0):
  describe_current_room(player)
  #Gets user inputs for commands.
  line = input("> ")
  #Splits the input into arguments.
  args = line.split()
  #If there are any arguments provided.
  if len(args) > 0:
    #Flag to check if the command was found.
    commandFound = False
    for c in Commands.keys():
      #Checks if input matches any command prefix.
      if args[0] == c[:len(args[0])]: 
        #Executes the corresponding command method.
        if c in ['pickup', 'drop'] and len(args) > 1:
          Commands[c](player, args[1])
        else:
          Commands[c](player)
        commandFound = True
        break
    if not commandFound:
      #Error message for unrecognized commands.
      print (f"{player.name} doesn't understand the suggestion.")

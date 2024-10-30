def main():
    pass

if __name__ == '__main__':
    main()
from random import randint

from game_save import GameState, save_game, load_game

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
    damage = min(
        max(randint(0, self.health) - randint(0, enemy.health), 0),
        enemy.health)
    
    #Reduces the enemy's health by damage dealt.
    enemy.health = enemy.health - damage

    #Message if the attack misses
    if damage == 0:
       print(f"{enemy.name} evades {self.name}'s attack")
    
    #Message if the attack hits.
    else: print (f"{self.name} hurts {enemy.name}!")
    
    #Returns true if the enemy is defeated
    return enemy.health <= 0

#Enemy class inherits from the Character
class Enemy(Character):
  
  def __init__(self, player):

    #Initializes the base Character class
    Character.__init__(self)

    #Sets a default name for the enemy
    self.name = 'a goblin'

    #Randomizes enemy health based on player's health.
    self.health = randint(1, player.health)

#Player class inherits from character.
class Player(Character):
  def __init__(self):

    #initializes the base character class.
    Character.__init__(self)

    #Sets initial state of the player.
    self.state = 'normal'

    #Sets player's initial health
    self.health = 10

    #Sets the player's maximum health.
    self.health_max = 10

    #Player method to quit the game.
  def quit(self):
    print (f"{self.name} can't find the way back home, and dies of starvation.\nR.I.P.")
    
    #sets health to 0, indicating death.
    self.health = 0

    #displays all commands.
  def help(self): print (Commands.keys())

  #Displays player's health status.
  def status(self): print (f"{self.name}'s health: {self.health}/{self.health_max}")
  
  
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
        
        #Enemy attacks immediately after waking up
        self.enemy_attacks()
      else:
        if self.health < self.health_max:
          
          #Restores health if below maximum
          self.health = self.health + 1
        
        #Message if health is at max.
        else: print (f"{self.name} slept too much.") 
        
        #Decrease health for resting.
        self.health = self.health - 1
  
  #Method for moving forward
  def forward(self):
    if self.state != 'normal':
      
      #Cannot move if fighting
      print (f"{self.name} is too busy right now!")
      
      #Enemy attacks if the player cannot move
      self.enemy_attacks()
    else:
      
      #Message indicating explortation.
      print (f"{self.name} explores a twisty passage.")
      
      #Random chance of encountering an enemy.
      if randint(0, 1):
        self.enemy = Enemy(self)
        
        #Message for enemy encounters.
        print (f"{self.name} encounters {self.enemy.name}!")
        
        #Change state to fighting.
        self.state = 'fight'
      else:
        
        #Random chance of getting tired during exploration.
        if randint(0, 1): self.tired()
  
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
  'forward': Player.forward,
  'flee': Player.flee,
  'attack': Player.attack,
  'save' : lambda player: save_game(GameState(player.name, []), get_save_filename()),
  'load' : lambda: load_game(get_save_filename())
  }




def title_screen():
  print("Welcome to PLACEHOLDER NAME")
  print("1. Start a new game")
  print("2. Load a previous game")

  choice = input("\nChoose an option (1 or 2)\n")
  return choice

def start_new_game():
  new_player = Player()
  new_player.name = input("What would you like to name your character \n")
  print(f"{new_player.name} enters a dark cave, searching for adventure.")
  return new_player

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


player = None

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
        Commands[c](player)
        commandFound = True
        break
    if not commandFound:
      
      #Error message for unrecognized commands.
      print (f"{player.name} doesn't understand the suggestion.")

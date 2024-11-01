import json

#Creates parameters on what to save in the game
class GameState:

  def __init__(self, player_name, inventory):
    self.player_name = player_name
    self.inventory = inventory

  def to_dict(self):
    return {
      'player_name' : self.player_name,
      'inventory' : self.inventory
  }

  @classmethod

  def from_dict(cls, data):
    return cls(data['player_name'], data['inventory'])

#Save game state to a file
def save_game(game_state, filename = 'savegame.log'):
  try:
    with open(filename, 'w') as file:
      json.dump(game_state.to_dict(), file)
    print("Game saved successfully as {filename}")
  except IOError as e:
    print(f"An error occurred while saving the game: {e}")


def load_game(filename = 'savegame.log'):
  try:
    with open(filename) as file:
      data = json.load(file)
      game_state = GameState.from_dict(data)
      print("Game loaded successfully from {filename}.")
      return game_state

  except FileNotFoundError:
    print("No save file found.")
    return None
  
  except json.JSONDecodeError:
    print("Error reading the save file")
    return None

if __name__ == '__main__':
  current_game = GameState("Player1", [])
  save_game(current_game)

#Load the game
  loaded_game = load_game()

  if loaded_game:
    print(f"Loaded Game - Player: {loaded_game.player_name}, Inventory: {loaded_game.inventory}")
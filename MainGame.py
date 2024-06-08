from Live import load_game, welcome
import MemoryGame as game1
import GuessGame as game2
import CurrencyRouletteGame as game3

print(welcome("Lachezar"))
user_preferences = load_game()

game_selected_by_user = user_preferences['gameSelected']
difficulty_selected_by_user = user_preferences['gameDifficulty']

# I know it's not a best practice to use numbers as keys, but works fine in this case
games_mapping = { 1: game1, 2: game2, 3: game3}

game_to_call = games_mapping.get(game_selected_by_user)
print(game_to_call)

if game_to_call:
    game_to_call.play(difficulty_selected_by_user)






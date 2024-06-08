def welcome(name):
    welcome_string = (f'Hello {name} and welcome to the World of Games (WoG).\n'
                      "Here you can find many cool games to play.\n"
                      )
    return welcome_string

def load_game():
    selected_game_number = get_and_return_selected_game_number()
    selected_game_difficulty = get_and_return_selected_game_difficulty()

    user_preferences = {"gameSelected": selected_game_number, "gameDifficulty": selected_game_difficulty}
    return user_preferences


def get_and_return_selected_game_number():
    while True:
        try:
            game_id_to_load = int(input("Please choose a game to play:\n"
                                        "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n"
                                        "2. Guess Game - guess a number and see if you chose like the computer\n"
                                        "3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n"))
            if game_id_to_load not in range(1, 4):
                print("Please enter a number between 1 and 3!")
            else:
                break
        except:
            print("Please enter the selected Game number!")

    return game_id_to_load

def get_and_return_selected_game_difficulty():
    while True:
        try:
            game_difficulty_selected = int(input("Please choose game difficulty from 1 to 5:"))
            if game_difficulty_selected not in range(1, 6):
                print("Please enter a number between 1 and 5!")
            else:
                break
        except:
            print("Please enter the desired game difficulty as a number!")

    return game_difficulty_selected


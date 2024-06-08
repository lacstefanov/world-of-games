import random

from Score import add_score

def generate_number(selected_difficulty):
    random_number_in_difficulty_range = random.randint(1,selected_difficulty)
    return random_number_in_difficulty_range

def get_guess_from_user(selected_difficulty):
    while True:
        try:
            user_guess = int(input(f'Please enter your guess between 1 and {selected_difficulty}'))
            if user_guess not in range(1, selected_difficulty + 1):
                print(f'Please enter a number between 1 and {selected_difficulty}!')
            else:
                break
        except:
            print("Please enter a valied number within the specified range!")

    return user_guess

def compare_results(correct_answer, user_guess):
    user_guess_is_correct = False
    if (user_guess == correct_answer):
        user_guess_is_correct = True
    return user_guess_is_correct

def play(selected_difficulty):
    game_answer = generate_number(selected_difficulty)
    user_guess = get_guess_from_user(selected_difficulty)
    user_has_guessed = compare_results(game_answer, user_guess)

    print ("Correct guess!"), add_score(selected_difficulty) if user_has_guessed else print ("Incorrect guess!")
    return user_has_guessed







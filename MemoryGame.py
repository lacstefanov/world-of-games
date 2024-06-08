import random
import sys
import time

from Score import add_score

def generate_sequence(selected_difficulty):
    random_numbers_list = []
    for number in range(0,selected_difficulty):
        random_number = random.randint(1,101)
        random_numbers_list.append(random_number)

    display_random_numbers_list_for_short(random_numbers_list)

    return random_numbers_list

def display_random_numbers_list_for_short(numbers_list):
    sys.stdout.write(str(numbers_list))
    sys.stdout.flush()
    time.sleep(0.7)
    sys.stdout.write('\r' + ' ' * len(str(numbers_list)) + '\r')
    sys.stdout.flush()

def get_list_from_user(selected_difficulty):

    input_converted_to_list = []
    list_consists_of_numbers_only = True

    while True:
        try:
            user_list = input("Please tell me the numbers sequence, remembered by you, separated by comma!")
            splitted_user_list = user_list.split(",")

            for entry in splitted_user_list:
                if entry.isdigit():
                    input_converted_to_list.append(int(entry))
                else:
                    list_consists_of_numbers_only = False
                    break

            user_input_length = len(input_converted_to_list)

            if user_input_length != selected_difficulty:
                print(f'Please enter {selected_difficulty} numbers, separated by comma only!')
                input_converted_to_list = []
            else:
                break
        except:
            print(f'Please enter {selected_difficulty} numbers, separated by comma only!')

    return input_converted_to_list

def is_list_equal(correct_sequence, user_input):
    lists_are_equal = False
    correct_sequence.sort()
    user_input.sort()

    if user_input == correct_sequence:
        lists_are_equal = True

    print("You guessed the numbers correctly!") if lists_are_equal else print("These are not the correct numbers!")

    return lists_are_equal

def play(selected_difficulty):
    numbers_for_this_game = generate_sequence(selected_difficulty)
    user_guess = get_list_from_user(selected_difficulty)
    user_has_guessed = is_list_equal(numbers_for_this_game, user_guess)
    if user_has_guessed: add_score(selected_difficulty)

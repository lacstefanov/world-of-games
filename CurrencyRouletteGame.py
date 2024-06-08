import requests
import random

from Score import add_score

def get_money_interval(selected_difficulty, amount_in_usd):

    currency_api_url = 'https://api.exchangerate-api.com/v4/latest/USD'

    currency_api_response = requests.get(currency_api_url)
    usd_to_ils = float(currency_api_response.json()['rates']['ILS'])

    amount_converted_to_ils = amount_in_usd * usd_to_ils

    generated_interval = {"lowestValidThreshold": (amount_converted_to_ils - (5 - selected_difficulty)),
                          "highestalidThreshold": amount_converted_to_ils + (5 - selected_difficulty)}

    return generated_interval

def get_guess_from_user(amount_in_usd):
    while True:
        try:
            user_guess = int(input(f'Please enter your guess on how much of ILS is {amount_in_usd}$'))
            break
        except:
            print("Please enter a valied number!")

    return user_guess

def play(selected_difficulty):

    user_guess_is_correct = False
    random_amount_in_usd = random.randint(1, 100)

    correct_answer_interval = get_money_interval(selected_difficulty, random_amount_in_usd)
    user_guess = get_guess_from_user(random_amount_in_usd)

    if user_guess >= correct_answer_interval['lowestValidThreshold'] and user_guess <= correct_answer_interval['highestalidThreshold']:
        user_guess_is_correct = True

    print("You guessed correctly"), add_score(selected_difficulty) if user_guess_is_correct else print("Incorrect answer")






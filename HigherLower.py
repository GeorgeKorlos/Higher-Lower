from art import logo, vs
from game_data import data
import random

# Generate a random account from the game data.
def get_data():
    return random.choice(data)

# Format account data into printable format.
def format_data(acc):
    name = acc['name']
    desc = acc['description']
    country = acc['country']
    return f"{name}, a {desc}, from {country}"

# Check if user is correct.
def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess.lower() == 'a'
    else:
        return guess.lower() == 'b'

def game():
    print(logo)
    score = 0
    game_continue = True
    acc_a = get_data()
    acc_b = get_data()

    while game_continue:
        acc_a = acc_b
        acc_b = get_data()

        while acc_a == acc_b:
            acc_b = get_data()
        
        print(f"Compare A: {format_data(acc_a)}.")
        print(vs)
        print(f"Against B: {format_data(acc_b)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").strip()
        a_followers = acc_a['follower_count']
        b_followers = acc_b['follower_count']
        is_correct = check_answer(guess=guess, a_followers=a_followers, b_followers=b_followers)

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            game_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")

game()

import json
import random

def load_riddles(file):  # load riddles from a json file and returns a list of dictionaries with riddles and their answers
    with open(file, 'r', encoding='utf-8') as f:
        riddles = json.load(f)  # json file allows dynamic content updates without changing code
    return riddles


def pere_fouras_riddles(file='data/PFRiddles.json'):  # simulates the riddle challenge, returns true if correct or false if incorrect
    riddles = load_riddles(file)
    riddle = random.choice(riddles)
    question = riddle['question']
    answer = riddle['answer'].lower()

    print("Pere Fouras Challenge: solve this riddle!")
    print(f"Riddle: {question}")

    attempts = 3
    while attempts > 0:
        user_answer = input(
            "Your answer: ").strip().lower()  # strip removes spaces while lower transforms into lowercase
        if user_answer == answer:
            print("Correct! You've won a key.")
            return True
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Incorrect! You have {attempts} attempts left.")
            else:
                print(f"You've failed! The correct answer was: {answer}.")
    return False

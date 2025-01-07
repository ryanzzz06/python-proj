from utility_functions import (introduction, compose_equipe, challenges_menu, choose_player)
from math_challenges import math_challenge
from chance_challenges import chance_challenge
from logical_challenges import logic_challenge
from pere_fouras_challenge import pere_fouras_riddles
from final_challenge import treasure_room


def game():
    # Welcome and Team Setup
    introduction()
    team = compose_equipe()
    total_keys = 0

    # Collect keys until reaching 3
    while total_keys < 3:
        print("\nKeys collected so far:", total_keys, "/ 3")

        choice = challenges_menu()

        if choice == 1:
            print("\nYou've chosen: Math Challenge")
            result = math_challenge()
        elif choice == 2:
            print("\nYou've chosen: Logic Challenge")
            result = logic_challenge()
        elif choice == 3:
            print("\nYou've chosen: Chance Challenge")
            result = chance_challenge()
        elif choice == 4:
            print("\nYou've chosen: Père Fouras Riddle")
            result = pere_fouras_riddles()
        else:
            print("Invalid selection, try again!")
            continue

        if result:
            player = choose_player(team)
            player['keys_won'] = player.get('keys_won', 0) + 1
            total_keys += 1
            print(f"Great! {player['name']} won a key.")
        else:
            print("Challenge failed. Better luck next time!")

    # Final Treasure Room Challenge
    print("\nFinal Stage: The Treasure Room!")
    success = treasure_room()
    if success:
        print("Victory! You've unlocked the treasure and won the game!")
    else:
        print("Unfortunately, the treasure remains locked. Game over.")

def introduction():
    print("Welcome to the Fort Boyard Simulator!")
    print("Your goal is to collect three keys by completing challenges and unlock the treasure room.")


def compose_equipe():  # Returns a list of dictinaries
    team = []
    while True:
        try:
            num_players = int(input("Enter the number of players (1-3): "))
            if 1 <= num_players <= 3:
                break
            else:
                print("Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Enter a number.")
    for i in range(num_players):
        name = input(f"Enter the name of player {i + 1}: ").strip()
        profession = input(f"Enter the profession of player {i + 1}: ").strip()
        is_leader = input(f"Is player {i + 1} the team leader? (yes/no): ").strip().lower() == 'yes'
        team.append({'name': name, 'profession': profession, 'is_leader': is_leader, 'keys_won': 0})
    if not any(player['is_leader'] for player in team):  # Assign leader if none chosen
        team[0]['is_leader'] = True
    return team


def challenges_menu():  # returns the number of the chosen challenge

    print("Choose a challenge:")
    print("1. Mathematics Challenge")
    print("2. Logic Challenge")
    print("3. Chance Challenge")
    print("4. Pere Fouras' Riddle")

    while True:
        try:
            choice = int(input("Enter your choice (1-4): "))
            if 1 <= choice <= 4:
                return choice
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Enter a number.")


def choose_player(team):
    print("Choose a player for the challenge:")

    for i, player in enumerate(team):
        role = "Leader" if player['is_leader'] else "Member"
        print(f"{i + 1}. {player['name']} ({player['profession']}) - {role}")
    while True:
        choice = int(input("Enter the player's number: ")) - 1
        if 0 <= choice < len(team):
            return team[choice]
        else:
            print("Please select a valid player number.")
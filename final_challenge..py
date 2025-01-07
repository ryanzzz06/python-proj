def treasure_room(file='data/TRClues.json'):  # Run the final treasure room challenge
    with open(file, 'r', encoding='utf-8') as f:  # json with codewords allows a way to add new challenges without altering function
        data = json.load(f)

    year = random.choice(list(data.keys()))
    challenge = random.choice(data[year])
    clues = challenge['clues']
    codeword = challenge['codeword'].lower()

    print("Final Challenge: Unlock the treasure room!")

    for i in range(3):
        print(f"Clue {i + 1}: {clues[i]}")
        user_answer = input("Enter the codeword: ").strip().lower()
        if user_answer == codeword:
            print("Congratulations! You've unlocked the treasure room!")
            return True
        elif i < 2:
            print("Incorrect! Here's another clue.")
        else:
            print(f"You've failed! The correct codeword was: {codeword}.")
    return False

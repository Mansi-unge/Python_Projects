# -------------------------------
# SNAKE WATER GUN GAME
# -------------------------------

# Step 1: Import the random module
# This module allows the computer to make random (unpredictable) choices.
import random

# Step 2: Function to check who wins
def check_winner(user, computer):
    # If both choices are the same, it's a draw.
    if user == computer:
        return "It's a Draw..!"

    # The user wins in these 3 cases:
    # 1. Snake drinks water
    # 2. Water drowns gun
    # 3. Gun kills snake
    elif (user == 'snake' and computer == 'water') or \
         (user == 'water' and computer == 'gun') or \
         (user == 'gun' and computer == 'snake'):
        return "You Won..!"
    
    # In all other cases, the computer wins.
    else:
        return "You Lost..!"


# Step 3: Function to play one round of the game
def play_game():
    # Create a list of valid choices for both user and computer.
    choices = ['snake', 'water', 'gun']

    # Ask the user for their choice and convert it to lowercase
    # to avoid case sensitivity issues (e.g., 'Snake' or 'SNAKE' will still work).
    user_choice = input("Enter your choice (snake/water/gun): ").lower()

    # Check if the user's input is valid.
    if user_choice not in choices:
        print("Invalid choice! Try again...")
        return None  # Return None so this round doesn't count

    # Computer randomly selects one option from the list.
    computer_choice = random.choice(choices)

    # Display what the computer chose.
    print(f"Computer chose: {computer_choice}")

    # Determine the result by calling the check_winner() function.
    result = check_winner(user_choice, computer_choice)

    # Print whether the user won, lost, or drew the round.
    print(result)

    # Return who won this round so we can track scores.
    if "Won" in result:
        return "user"
    elif "Lost" in result:
        return "Computer"
    else:
        return "draw"


# Step 4: Main game function that runs multiple rounds and tracks scores
def start():
    # Initialize both scores to zero.
    user_score = 0
    computer_score = 0

    # Set the total number of rounds.
    rounds = 5

    print("Welcome to the SNAKE WATER GUN Game!")
    print(f"Total Rounds: {rounds}")
    print("-" * 80)

    # i will represent the current round number.
    i = 1

    # This loop will run until 5 rounds are completed.
    while i <= rounds:
        print(f"\nRound {i} of {rounds}")
        
        # Play one round and get the winner.
        winner = play_game()
        
        # Update the score based on who won the round.
        if winner == 'user':
            user_score += 1
        elif winner == 'Computer':
            computer_score += 1
        
        # Display the updated score after each round.
        print(f"Score ---> You: {user_score} | Computer: {computer_score}")
        print("-" * 80)
        # Move to the next round.
        i += 1

    # After all rounds, show the final results.
    print("\nFinal Results:")
    print(f"Your Score: {user_score}")
    print(f"Computer Score: {computer_score}")

    print("-" * 80)
    # Compare scores to declare the overall winner.
    if user_score > computer_score:
        print("You are the winner of this game!")
    elif computer_score > user_score:
        print("Computer is the winner of this game!")
    else:
        print("It's a tie!")

    # End message after the game is over.
    print("Thanks for playing.")


# Step 5: Start the game by calling the start() function
start()

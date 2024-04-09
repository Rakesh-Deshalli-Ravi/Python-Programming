# Name: Rakesh Deshalli Ravi
# Date: 11 Oct 2023
# Honor statement: I have not given or received any unauthorized assistance on this assignment
# YouTube link: https://youtu.be/h22-05_0DUA
# Assignment 0502: Rolling Game

import assignment_5a as A  # Importing the module for the dice game
import random  # Importing the random module for generating random numbers

def get_integer_input(prompt):
    """
    Get an integer input from the user, handling exceptions for invalid input.

    Args:
        prompt (str): The prompt to display to the user.

    Returns:
        int: The integer input provided by the user.
    """
    while True:
        try:
            user_input = int(input(prompt))  # Attempt to get an integer input from the user
            return user_input
        except ValueError:
            print("Please enter a valid integer.")  # Display an error message for invalid input

def get_play_again_input():
    """
    Get the play again input from the user, handling exceptions for invalid responses.

    Returns:
        str: The user's play again input, which is either 'yes' or 'no'.
    """
    while True:
        play_again_input = input("Do you want to play again? (yes/no): ").lower()  # Prompt the user for play again input
        try:
            if play_again_input in ["yes", "no"]:
                return play_again_input  # Return 'yes' or 'no' if it's a valid response
            else:
                raise ValueError
        except ValueError:
            print("Please enter 'yes' or 'no'.")  # Display an error message for invalid input

def main():
    """
    Main function for the Dice Rolling Game.
    """
    print("Welcome to the Dice Rolling Game!")
    player_name = input("What's your name? ")  # Prompt the user for their name

    play_again = True  # Initialize the play_again flag to True
    total_score = 0  # Initialize the total score to 0

    while play_again:
        print("\nLet's play a game, " + player_name + "!")
        goal = random.randint(1, 100)  # Generate a random goal between 1 and 100
        print("The goal is:", goal)

        six_sided_count = get_integer_input("How many 6-sided dice would you like to roll? ")  # Get the number of 6-sided dice
        ten_sided_count = get_integer_input("How many 10-sided dice would you like to roll? ")  # Get the number of 10-sided dice
        twenty_sided_count = get_integer_input("How many 20-sided dice would you like to roll? ")  # Get the number of 20-sided dice

        cup = A.Cup(six_sided_count, ten_sided_count, twenty_sided_count)  # Create a Cup object with the specified dice counts
        cup.roll()  # Roll the dice in the cup
        roll_result = cup.getSum()  # Get the sum of the rolled dice
        print('roll result = ', roll_result)

        if roll_result == goal:
            score = 10  # If the roll matches the goal, earn 10 points
            print("Congratulations! You rolled the goal and earned 10 points!")
        elif abs(roll_result - goal) <= 3:
            score = 5  # If the roll is within 3 of the goal, earn 5 points
            print("You were within 3 of the goal and earned 5 points!")
        elif abs(roll_result - goal) <= 10:
            score = 2  # If the roll is within 10 of the goal, earn 2 points
            print("You were within 10 of the goal and earned 2 points.")
        else:
            score = 0  # Otherwise, earn 0 points
            print("You didn't earn any points this time.")

        total_score += score  # Update the total score with the earned score
        print(f"Your total score is now {total_score} points, {player_name}!")

        play_again = get_play_again_input() == "yes"  # Ask the user if they want to play again and set the play_again flag accordingly

    print(f"Thanks for playing, {player_name}! Your final score is {total_score} points.")  # Display the final score

if __name__ == "__main__":
    main()  # Call the main function if the script is run as the main program

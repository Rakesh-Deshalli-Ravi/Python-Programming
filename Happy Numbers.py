# Name: Rakesh Deshalli Ravi
# Date: 27 Sep 2023
# Honor statement: I have not given or received any unauthorized assistance on this assignment
# YouTube link: https://youtu.be/dHD8JI6cKe8
# Assignment 0302: Happy Numbers
def is_happy_number(n):
    """
    Check if a number is a happy number and return a tuple with the result and a list of visited numbers during the process.

    Args:
        n (int): The number to check for happiness.

    Returns:
        tuple: A tuple containing a boolean indicating if the number is happy and a list of visited numbers.
    """
    visited = []  # List to keep track of visited numbers
    while n != 1 and n not in visited:
        visited.append(n)  # Add the current number to the visited list
        # Calculate the next number in the sequence by summing the squares of its digits
        n = sum(int(digit) ** 2 for digit in str(n))
    # Check if the loop ended because n became 1 (happy number) or due to a cycle (sad number)

    if n == 1:
        return True, visited   # Number is happy
    else:
        # The number is sad, find the second occurrences of same number
        second_occurrence = visited.index(n)

        # Append the first and second occurrences to the visited list
        visited.append(visited[second_occurrence])

        return False, visited

if __name__ == '__main__':
    results = {}  # Dictionary to store results for different numbers
    while True:
        try:
            user_input = input("Enter a positive integer number (or 'end' to finish): ")
            if user_input.lower() == 'end':
                break  # Exit the loop if the user enters 'end'
            num = int(user_input)
            if num <= 0:
                print("Please enter a positive integer number.")
                continue  # Skip to the next iteration if the input is not positive
            is_happy, visited_numbers = is_happy_number(num)  # Check if the number is happy
            if is_happy:
                print(f"{num} is a happy number: {visited_numbers + [1]}")
                results[num] = ('happy', visited_numbers + [1])  # Store the result as 'happy'
            else:
                print(f"{num} is a sad number: {visited_numbers}")
                results[num] = ('sad', visited_numbers)  # Store the result as 'sad'
        except ValueError:
            print("Invalid input. Please enter a positive number or 'end' to finish.")

    print("Summing up the results:")
    print(results)  # Print the results dictionary

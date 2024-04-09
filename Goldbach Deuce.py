# Name: Rakesh Deshalli Ravi
# Date: 04 Oct 2023
# Honor statement: I have not given or received any unauthorized assistance on this assignment
# YouTube link: https://youtu.be/FkUDHHZNT4M
# Assignment 0401: Goldbach Deuce

import random

def generate_random_list(length):
    """
    Generate a list of random numbers between 0 and 100.

    Args:
        length (int): The length of the list.

    Returns:
        list: A list of random numbers.
    """
    # Generate random integers between 0 and 100, create a list, and sort it
    return sorted([random.randint(0, 100) for _ in range(length)])

def binary_search(sorted_list, target):
    """
    Perform binary search to find the target in a sorted list.

    Args:
        sorted_list (list): A sorted list of numbers.
        target (int): The target value to find.

    Returns:
        bool: True if the target is found, False otherwise.
    """
    left = 0
    right = len(sorted_list) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if sorted_list[mid] == target:
            return True
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False

def find_two_numbers_with_sum(sorted_list, target_sum):
    """
    Find two numbers in a sorted list that sum up to the target sum using binary search.

    Args:
        sorted_list (list): A sorted list of numbers.
        target_sum (int): The target sum to find.

    Returns:
        tuple: A tuple containing the two numbers that sum up to the target sum, or None if no such pair exists.
    """
    for num in sorted_list:
        complement = target_sum - num
        if binary_search(sorted_list, complement):
            return num, complement

if __name__ == '__main__':
    print("Welcome to Goldbach Deuce Program")
    print("Length of the list should be greater than or equal to 2 to find the sum ")
    print("Sum should be positive integer")
    while True:
        try:
            length = int(input("Enter the length of the list: "))
            target_sum = int(input("Enter the target sum: "))
            if (length > 1) and (target_sum >= 0):
                # Generate a random list and sort it
                random_list = generate_random_list(length)
                print("Random numbers generated are:", random_list)

                # Find two numbers with the target sum
                result = find_two_numbers_with_sum(random_list, target_sum)

                if result:
                    num1, num2 = result
                    print(f"Two numbers that sum up to {target_sum} are {num1} and {num2}.")
                    break
                else:
                    print("No pair of numbers found that sum up to the target sum.")
                    break
            else:
                print("Invalid input")

        except ValueError:
            print("Invalid input. Please enter a positive number")

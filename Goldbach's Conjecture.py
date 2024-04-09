# Name: Rakesh Deshalli Ravi
# Date: 27 Sep 2023
# Honor statement: I have not given or received any unauthorized assistance on this assignment
# YouTube link: https://youtu.be/1cHlT47lrnI
# Assignment 0301: Goldbach's Conjecture

def is_prime(n):
    """
    Check if a number is prime.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


if __name__ == '__main__':
    # Test Goldbach's Conjecture for integers less than 100
    for num in range(4, 101, 2):
        # Check for two prime numbers that sum up to 'num'

        for i in range(2, num // 2 + 1):
            if is_prime(i) and is_prime(num - i):
                print(f"{num} = {i} + {num - i}")
                break

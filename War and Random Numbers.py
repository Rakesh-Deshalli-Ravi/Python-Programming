# Name: Rakesh Deshalli Ravi
# Date: 26 Oct 2023
# Honor statement: I have not given or received any unauthorized assistance on this assignment
# YouTube link: https://youtu.be/ic8INqNYVp8
# Assignment 0701: War and Random Numbers
from statistics import mean

class PseudoRandomNumberGenerator:
    def __init__(self, seed=1000):
        """
        Initialize the PseudoRandomNumberGenerator.

        Args:
        - seed (int): The seed value used to start the pseudo-random number generation process.
        """
        self.seed = seed
        self.bits_list = []
        # Weight list for generating pseudo-random numbers
        self.weight_list = [1/2**i for i in range(1, 33)]

    def file_read(self, file_path):
        """
        Read bytes from a file and generate a list of bits for pseudo-random number generation.

        Args:
        - file_path (str): The path to the file to be used as a source of randomness.
        """
        file_obj = open(file_path, 'rb')
        # Iteration counter
        i = 0
        while i < 32:
            if i == 0:
                file_obj.seek(self.seed, 0)
            else:
                file_obj.seek(100, 1)
            ch1 = file_obj.read(1)
            file_obj.seek(100, 1)
            ch2 = file_obj.read(1)
            if ch1 != b'' and ch2 != b'' and ch1 != ch2:
                i = i + 1
                if ch1 > ch2:
                    self.bits_list.append(1)
                else:
                    self.bits_list.append(0)
            elif ch1 != b'' and ch2 != b'' and ch1 == ch2:
                while ch1 == ch2 and ch2 != b'':
                    if ch2 == b'':
                        # Handle reaching the end of the file by wrapping to the beginning
                        print('Reached the end of the file')
                        file_obj.seek(0)
                        file_obj.seek(100, 1)
                        ch2 = file_obj.read(1)
                    else:
                        file_obj.seek(100, 1)
                        ch2 = file_obj.read(1)
                i = i + 1
                if ch1 > ch2:
                    self.bits_list.append(1)
                else:
                    self.bits_list.append(0)
            else:
                # Handle reaching the end of the file by wrapping to the beginning
                print('Reached the end of the file')
                file_obj.seek(0)

    def generate_random(self):
        """
        Generate a pseudo-random number based on the bits list and weights.

        Returns:
        - float: A pseudo-random number between 0 and 1.
        """
        random_number = 0
        for i in range(len(self.bits_list)):
            random_number += self.bits_list[i] * self.weight_list[i]
        return random_number

def random():
    """
    Generate a list of pseudo-random values using different seed values.

    Returns:
    - list: A list of pseudo-random values.
    """
    generated_values = []
    for i in range(10000):
        seed = i
        prng = PseudoRandomNumberGenerator(seed)
        prng.file_read('C:/Users/harsh/Downloads/python_program/war-and-peace.txt')
        random_value = prng.generate_random()
        generated_values.append(random_value)
    return generated_values

if __name__ == '__main__':
    generated_values = random()
    # Print the first 20 generated pseudo-random values
    print('Top 20 generated pseudo-random values are:', generated_values[:21])

    # Calculate and print statistics of the generated values
    print('Maximum value of the list generated with random values is {}'.format(max(generated_values)))
    print('Minimum value of the list generated with random values is {}'.format(min(generated_values)))
    print('Mean of the list generated with random values is {}'.format(mean(generated_values)))

# Name: Rakesh Deshalli Ravi
# Date: 11 Oct 2023
# Honor statement: I have not given or received any unauthorized assistance on this assignment
# YouTube link: https://youtu.be/NjDveSNCWek
# Assignment 0501: Dice and Cups
import random

# Define a class for a six-sided die
class SixSidedDie:
    def __init__(self):
        """
        Initialize a SixSidedDie object with a face value of None.
        """
        self.s_die = 'Six'
        self.face_value = None

    def roll(self):
        """
        Roll the six-sided die and set the face value to a random number between 1 and 6.
        """
        self.face_value = random.randint(1, 6)

    def getFaceValue(self):
        """
        Get the face value of the six-sided die.
        """
        return self.face_value

    def __repr__(self):
        """
        Return a string representation of the SixSidedDie object.
        """
        return f'{self.s_die}SidedDie({self.face_value})'

# Define a class for a ten-sided die, which inherits from SixSidedDie
class TenSidedDie(SixSidedDie):
    def roll(self):
        """
        Roll the ten-sided die and set the face value to a random number between 1 and 10.
        """
        self.s_die = 'Ten'
        self.face_value = random.randint(1, 10)

# Define a class for a twenty-sided die, which inherits from SixSidedDie
class TwentySidedDie(SixSidedDie):
    def roll(self):
        """
        Roll the twenty-sided die and set the face value to a random number between 1 and 20.
        """
        self.s_die = 'Twenty'
        self.face_value = random.randint(1, 20)

# Define a class for a cup of dice
class Cup:
    def __init__(self, num_six_sided=1, num_ten_sided=1, num_twenty_sided=1):
        """
        Initialize a Cup object with a specified number of each type of die.
        """
        self.dice = []
        for _ in range(num_six_sided):
            self.dice.append(SixSidedDie())
        for _ in range(num_ten_sided):
            self.dice.append(TenSidedDie())
        for _ in range(num_twenty_sided):
            self.dice.append(TwentySidedDie())

    def roll(self):
        """
        Roll all the dice in the cup.
        """
        for die in self.dice:
            die.roll()

    def getSum(self):
        """
        Get the sum of the face values of all the dice in the cup.
        """
        return sum(die.getFaceValue() for die in self.dice)

    def __repr__(self):
        """
        Return a string representation of the Cup object, including all dice.
        """
        return f'Cup({", ".join(map(repr, self.dice))}'

# Main section to demonstrate the dice classes
if __name__ == '__main__':
    d = SixSidedDie()
    d.roll()
    print('Face value of six-sided die = ',d.getFaceValue())
    print('Object = ',d)

    print('In this program, we have considered 1 SixSidedDie, 2 TenSidedDie, and 1 TwentySidedDie')
    cup = Cup(1, 2, 1)
    cup.roll()
    print('Sum of the total face value of all dice = ',cup.getSum())
    print('Object = ',cup)

# Name: Rakesh Deshalli Ravi
# Date: 4 Oct 2023
# Honor statement: I have not given or received any unauthorized assistance on this assignment
# YouTube link: https://youtu.be/N_PV4gEvM-g
# Assignment 0402: Human Pyramid

def humanPyramid(row, column):
    """
    Calculate the weight on a person's shoulder in a human pyramid.

    Args:
        row (int): The row number (0-based index).
        column (int): The column number (0-based index).

    Returns:
        float: The weight on the person's shoulder in pounds.
    """
    # Base case: If we're at the top of the pyramid, the weight is 128.
    if row == 0:
        return 128

    # Special case: If we're at the edges (column 0 or column == row),
    # then we only have one person above.
    if column == 0 or column == row:
        return 128 + 0.5 * humanPyramid(row - 1, 0)

    # Recursive case: Calculate the weight by splitting it between two people above.
    return 128 + 0.5 * (humanPyramid(row - 1, column - 1) + humanPyramid(row - 1, column))


if __name__ == '__main__':
    print("\nWelcome to human pyramid program, enter the specific row and column number to know the weight on his shoulder.")
    print("Row and Column is starting from 0th index")
    while True:
        try:
            row = int(input("\nEnter row : "))
            column = int(input("Enter column: "))
            if (column <= row) and (column >= 0) and (row >= 0):
                # Calculate the weight on the person's shoulder and deduct their own weight (128 lbs).
                print(f"Shoulder weight = {humanPyramid(row,column) - 128 } lbs")
                print("Exiting the program,\nThank you")
                break
            else:
                print("Enter the specific number according to the human pyramid.")

        except:
            print("Enter the integer numbers.")

# Name: Rakesh Deshalli Ravi
# Date: 20 Sep 2023
# Honor statement: I have not given or received any unauthorized assistance on this assignment
# YouTube link: https://youtu.be/u1mOM73x40Y
# Assignment 0202: Stem-and-Leaf Implementation

import matplotlib.pyplot as plt # Import the matplotlib library for plotting

# Define a function to display a stem-and-leaf plot
def display_stem_and_leaf(data):
    """
    Display a stem-and-leaf plot for a given dataset.
    Args:
        data (list): List of integer values to create the plot from.
    Returns:
        None
    """
    # Initializing empty lists to store stem and leaf values
    stems = []
    leaves = []

    # Iterate through each value in the data
    for value in data:
        # Divide each value into stem and leaf parts
        stem, leaf = divmod(value, 10)
        stems.append(stem)
        leaves.append(leaf)

    # Sort stems and leaves while preserving their association
    sorted_data = sorted(zip(stems, leaves), key=lambda x: (x[0], x[1]))

    # Initialize variables to track the current stem
    current_stem = None
    current_leaves = []

    for stem, leaf in sorted_data:
        if current_stem is None:
            current_stem = stem

        if stem == current_stem:
            current_leaves.append(leaf)
        else:
            # Print the stem and its leaves
            print(f"{current_stem} | {'   '.join(map(str, current_leaves))}")
            current_stem = stem
            current_leaves = [leaf]

    # Print the last stem and its leaves
    print(f"{current_stem} | {'   '.join(map(str, current_leaves))}")

    # Plot the stem-and-leaf graph using matplotlib
    plt.figure(figsize=(10, 6))  # Create a figure for the plot with a specific size
    plt.stem(stems, leaves)  # Create the stem-and-leaf plot
    plt.xlabel('Stem')  # Set the x-axis label
    plt.ylabel('Leaf')  # Set the y-axis label
    plt.title('Stem-and-Leaf Plot')  # Set the plot title
    plt.grid(True)  # Display a grid on the plot
    plt.show()  # Show the plot


# Main loop
if __name__ == '__main__':
    print("Welcome to the Stem-and-Leaf Plot Generator")  # Greeting to the user
    while True:
        print('Select the below option')
        print("1. Load Data from StemAndLeaf1.txt")
        print("2. Load Data from StemAndLeaf2.txt")
        print("3. Load Data from StemAndLeaf3.txt")
        print("0. Exit")

        choice = input("Please select an option (1/2/3/0): ")

        if choice == '1':
            # Load data from StemAndLeaf1.txt
            with open('data/StemAndLeaf1.txt', 'r') as file:
                data = [int(line.strip()) for line in file]
            display_stem_and_leaf(data)

        elif choice == '2':
            # Load data from StemAndLeaf2.txt
            with open('data/StemAndLeaf2.txt', 'r') as file:
                data = [int(line.strip()) for line in file]
            display_stem_and_leaf(data)

        elif choice == '3':
            # Load data from StemAndLeaf3.txt
            with open('data/StemAndLeaf3.txt', 'r') as file:
                data = [int(line.strip()) for line in file]
            display_stem_and_leaf(data)

        elif choice == '0':
            print("Exiting the program. Goodbye!")
            exit()
        else:
            print('\n')  # Print a newline for better formatting.
            print("Invalid input. Please select a valid option (1/2/3/0).")
            print('\n')  # Print a newline for better formatting.

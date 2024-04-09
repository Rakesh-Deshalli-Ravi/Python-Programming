# Name: Rakesh Deshalli Ravi
# Date: 1 Nov 2023
# Honor statement: I have not given or received any unauthorized assistance on this assignment
# YouTube link: https://youtu.be/7ebzzcg90jA
# Assignment 0801: Karate Club

import numpy as np
import warnings 
warnings.filterwarnings("ignore")

# Function to check if a matrix is symmetric
def is_symmetric(matrix):
    """
    Check if a matrix is symmetric.

    Parameters:
        matrix (numpy.ndarray): The input matrix to be checked for symmetry.

    Returns:
        bool: True if the matrix is symmetric, False otherwise.
    """
    return np.array_equal(matrix, matrix.T)

# Function to analyze the interaction matrix
def analyze_interaction_matrix(matrix):
    """
    Analyze the interaction matrix of a social club.

    Parameters:
        matrix (numpy.ndarray): The interaction matrix representing interactions among club members.

    This function prints various statistics about the interaction matrix.
    """
    num_members = len(matrix)
    print(f"The Karate club had {num_members} members.")
    
    # Calculate the sum of interactions per member
    interactions_per_member = matrix.sum(axis=1)
    print("Interactions per member:")
    for i in range(num_members):
        print(f"Member {i+1}: {interactions_per_member[i]} interactions")

    print(interactions_per_member)
    
    # Find the least and most active members
    least_active_member = np.argmin(interactions_per_member)
    most_active_member = np.argmax(interactions_per_member)
    print(f"Least active member: Member {least_active_member + 1}")
    print(f"Most active member: Member {most_active_member + 1}")

    # Check if there is an interaction between the least and most active members
    least_active_interactions = interactions_per_member[least_active_member]
    most_active_interactions = interactions_per_member[most_active_member]
    print(f"Interaction between them? {'Yes' if matrix[least_active_member][most_active_member] else 'No'}")
    
    # Calculate and print average interactions and standard deviation
    average_interactions = interactions_per_member.mean()
    std_interactions = interactions_per_member.std()
    print(f"Average interactions across all members: {average_interactions:.2f}")
    print(f"Standard deviation of interactions: {std_interactions:.2f}")

if __name__ == '__main__':
    # Load the interaction matrix from a file
    interaction_matrix = np.loadtxt("karate_club_interactions.txt", dtype=int)

    # print(interaction_matrix)
    if is_symmetric(interaction_matrix):
        print("The interaction matrix is symmetric.")
    else:
        print("The interaction matrix is not symmetric.")

    # Analyze the interaction matrix and print the results
    analyze_interaction_matrix(interaction_matrix)

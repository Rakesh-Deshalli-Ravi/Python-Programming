# Name: Rakesh Deshalli Ravi
# Date: 14 Nov 2023
# Honor statement: I have not given or received any unauthorized assistance on this assignment
# YouTube link: https://youtu.be/NU1Tc4lD0_s
# Assignment 1001: PlanetAnalysis


import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tqdm import tqdm

class CelestialBody:
    def __init__(self, identifier, orbital_radius, orbital_period):
        """
        Initialize the celestial body with its identifier, orbital radius, and orbital period.

        Args:
        identifier (str): The name of the celestial body.
        orbital_radius (float): The radius of the orbit (in some units).
        orbital_period (int): The time it takes to complete one orbit (in days).
        """
        self.identifier = identifier
        self.orbital_radius = orbital_radius
        self.orbital_period = orbital_period

    def locate(self, day):
        """
        Calculate the x and y coordinates of the celestial body for a given day.

        Args:
        day (int): The day number to calculate the position for.

        Returns:
        tuple: A tuple containing the x and y coordinates.
        """
        xcoor = self.orbital_radius * math.cos(2 * math.pi * day / self.orbital_period)
        ycoor = self.orbital_radius * math.sin(2 * math.pi * day / self.orbital_period)
        return xcoor, ycoor

def calculate_distance(planet1, planet2, day):
    """
    Calculate the distance between two planets on a given day.

    Args:
    planet1 (CelestialBody): The first planet.
    planet2 (CelestialBody): The second planet.
    day (int): The day number to calculate the distance for.

    Returns:
    float: The distance between the two planets.
    """
    x1, y1 = planet1.locate(day)
    x2, y2 = planet2.locate(day)
    
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def simulate_1000_days(earth, planets, noise_std=None):
    """
    Simulate the distances from Earth to other planets over 1000 days.

    Args:
    earth (CelestialBody): The Earth object.
    planets (list): List of other planet objects.
    noise_std (float, optional): Standard deviation of noise to add to the distances.

    Returns:
    dict: A dictionary with planets as keys and lists of distances as values.
    """
    calculate_distances = {planet: [] for planet in planets}
    
    for day in tqdm(range(1000)):
        for planet in planets:
            if noise_std:
                noise = np.random.normal(0, noise_std)
                calculate_distances[planet].append(calculate_distance(earth, planet, day) + noise)
            else:
                calculate_distances[planet].append(calculate_distance(earth, planet, day))
    return calculate_distances

def plot_calculate_distances(calculate_distances, noise_std=None):
    """
    Plot the calculated distances for each planet.

    Args:
    calculate_distances (dict): A dictionary with planets as keys and lists of distances as values.
    noise_std (float, optional): Standard deviation of noise used in the distance calculation.
    """
    colors = ['blue', 'orange', 'green']
    
    for i, (planet, values) in enumerate(calculate_distances.items()):
        plt.plot(values, label=planet.identifier, alpha=0.4)
        plt.axhline(y=np.mean(values), label=f'{planet.identifier} calculate_distance mean', color=colors[i])
    
    plt.title(f"Distances {'with Noise (STD=' + str(noise_std) + ')' if noise_std else 'without Noise'}")
    plt.xlabel("Days")
    plt.ylabel("Distance (CM)")
    plt.legend()
    plt.show()

def simulate_1000_years(planets):
    """
    Simulate the average distances between all pairs of planets over 1000 years.

    Args:
    planets (list): List of planet objects.

    Returns:
    numpy.ndarray: A 2D array of average distances between each pair of planets.
    """
    num_days_in_year = 365
    num_years = 1000
    calculate_distances = np.zeros((len(planets), len(planets)))

    for year in tqdm(range(num_years)):
        for day in range(num_days_in_year):
            for i in range(len(planets)):
                for j in range(i+1, len(planets)):
                    dist = calculate_distance(planets[i], planets[j], day)
                    calculate_distances[i, j] += dist
                    calculate_distances[j, i] += dist

    avg_calculate_distances = calculate_distances / (num_years * num_days_in_year)
    # Create a DataFrame for storing average distances
    planet_names = [planet.identifier for planet in planets]
    avg_calculate_distances_df = pd.DataFrame(avg_calculate_distances, columns=planet_names, index=planet_names)
    return avg_calculate_distances_df

def main():
    # Initialize celestial bodies
    mercury = CelestialBody("Mercury", 3.5, 88)
    venus = CelestialBody("Venus", 6.7, 225)
    earth = CelestialBody("Earth", 9.3, 365)
    mars = CelestialBody("Mars", 14.2, 687)
    jupiter = CelestialBody("Jupiter", 48.4, 4333)
    saturn = CelestialBody("Saturn", 88.9, 10759)
    uranus = CelestialBody("Uranus", 179, 30687)
    neptune = CelestialBody("Neptune", 288, 60190)

    # Run simulations and plot results
    three_planets = [mercury, venus, mars]
    all_planets = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

    # Simulate and plot distances without noise
    calculate_distances_no_noise = simulate_1000_days(earth, three_planets)
    plot_calculate_distances(calculate_distances_no_noise)

    # Simulate and plot distances with different noise levels
    std_values = [0.5, 3.0, 5.0, 7.0, 10.0]
    for std in std_values:
        calculate_distances_with_noise = simulate_1000_days(earth, three_planets, noise_std=std)
        plot_calculate_distances(calculate_distances_with_noise, noise_std=std)
    
    # Simulate distances over 1000 years
    avg_calculate_distances = simulate_1000_years(all_planets)

    # Check if the array is symmetric and find the closest planet to Earth
    is_symmetric = avg_calculate_distances.equals(avg_calculate_distances.T)
    print("The Pandas DataFrame is symmetric." if is_symmetric else "The Pandas DataFrame is not symmetric.")

    closest_planet_index = avg_calculate_distances.iloc[2].drop("Earth").idxmin()
    print(f'Closest planet in the 1000-years simulation is {closest_planet_index}')

    # Display the DataFrame with formatted distances
    pd.set_option('display.float_format', lambda x: '{:.2f}'.format(x))
    print(avg_calculate_distances)

    # Calculate distance between Earth and Mars on a specific day
    calculate_distance_732 = calculate_distance(earth, mars, 732)
    print(f'The Distance between Earth and Mars on day 732 is {calculate_distance_732} CM')


if __name__ == "__main__":
    main()


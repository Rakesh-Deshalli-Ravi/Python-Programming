# Name: Rakesh Deshalli Ravi
# Date: 26 Oct 2023
# Honor statement: I have not given or received any unauthorized assistance on this assignment
# YouTube link: https://youtu.be/5gWqOOe3nQo
# Assignment 0702: Overlapping Ellipses
import math
import Assignment_701

class Point:
    """
    Point class to represent a point in 2D space.

    Attributes:
        x (float): The x-coordinate of the point.
        y (float): The y-coordinate of the point.
    """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get(self):
        """Get the coordinates of the point as a tuple (x, y)."""
        return self.x, self.y

class Ellipse:
    """
    Ellipse class to represent an ellipse in 2D space.

    Attributes:
        p1 (Point): The first point defining the center of the ellipse.
        p2 (Point): The second point defining the size and orientation of the ellipse.
        width (float): The width of the ellipse.
    """

    def __init__(self, p1, p2, width):
        self.p1 = p1
        self.p2 = p2
        self.width = width

    def get(self):
        """Get the attributes of the ellipse: p1, p2, and width."""
        return self.p1, self.p2, self.width

def generate_random_point(x1, y1, x2, y2, i):
    """
    Generate a random point within a given rectangular region.

    Args:
        x1 (float): The minimum x-coordinate of the region.
        y1 (float): The minimum y-coordinate of the region.
        x2 (float): The maximum x-coordinate of the region.
        y2 (float): The maximum y-coordinate of the region.
        i (int): An integer used as a seed for randomness.

    Returns:
        tuple: A tuple containing the generated random point (x, y).
    """

    seed = (i * 2) + 12
    prng = Assignment_701.PseudoRandomNumberGenerator(seed)
    prng.file_read('C:/Users/harsh/Downloads/python_program/war-and-peace.txt')
    x = (x2 - x1) * prng.generate_random() + x1

    seed = (i * 2) + 27
    prng = Assignment_701.PseudoRandomNumberGenerator(seed)
    prng.file_read('C:/Users/harsh/Downloads/python_program/war-and-peace.txt')
    y = (y2 - y1) * prng.generate_random() + y1

    return x, y

def get_ellipse_coordinates(ellipse1, ellipse2):
    """
    Get the coordinates of a bounding rectangle that contains two ellipses.

    Args:
        ellipse1 (Ellipse): The first ellipse.
        ellipse2 (Ellipse): The second ellipse.

    Returns:
        tuple: A tuple containing the minimum x, minimum y, maximum x, and maximum y coordinates of the bounding rectangle.
    """

    x11 = ellipse1.get()[0].x
    y11 = ellipse1.get()[0].y
    x12 = ellipse1.get()[1].x
    y12 = ellipse1.get()[1].y
    x21 = ellipse2.get()[0].x
    y21 = ellipse2.get()[0].y
    x22 = ellipse2.get()[1].x
    y22 = ellipse2.get()[1].y

    min_x = min(x11, x12, x21, x22) - (ellipse1.get()[2] / 2)
    min_y = min(y11, y12, y21, y22) - (ellipse1.get()[2] / 2)
    max_x = max(x11, x12, x21, x22) + (ellipse2.get()[2] / 2)
    max_y = max(y11, y12, y21, y22) + (ellipse2.get()[2] / 2)

    return min_x, min_y, max_x, max_y

def is_point_inside_ellipses(ellipse1, ellipse2, point, i):
    """
    Check if a random point is inside both ellipses.

    Args:
        ellipse1 (Ellipse): The first ellipse.
        ellipse2 (Ellipse): The second ellipse.
        point (tuple): The random point as a tuple (x, y).
        i (int): An integer used as a seed for randomness.

    Returns:
        bool: True if the point is inside both ellipses, False otherwise.
    """

    el_p1 = (ellipse1.get()[0].x, ellipse1.get()[0].y)
    el_p2 = (ellipse1.get()[1].x, ellipse1.get()[1].y)
    e2_p1 = (ellipse2.get()[0].x, ellipse2.get()[0].y)
    e2_p2 = (ellipse2.get()[1].x, ellipse2.get()[1].y)
    el_in = math.dist(el_p1, point) + math.dist(el_p2, point) < ellipse1.get()[2]
    e2_in = math.dist(e2_p1, point) + math.dist(e2_p2, point) < ellipse2.get()[2]
    if el_in and e2_in:
        return True

def calculate_rectangle_area(min_x, min_y, max_x, max_y):
    """
    Calculate the area of a rectangle.

    Args:
        min_x (float): The minimum x-coordinate of the rectangle.
        min_y (float): The minimum y-coordinate of the rectangle.
        max_x (float): The maximum x-coordinate of the rectangle.
        max_y (float): The maximum y-coordinate of the rectangle.

    Returns:
        float: The area of the rectangle.
    """

    area = (max_x - min_x) * (max_y - min_y)
    return area

def compute_overlap_of_ellipses(ellipse1, ellipse2, num_random_points):
    """
    Compute the overlap area of two ellipses using a Monte Carlo method.

    Args:
        ellipse1 (Ellipse): The first ellipse.
        ellipse2 (Ellipse): The second ellipse.
        num_random_points (int): The number of random points to use in the calculation.

    Returns:
        float: The estimated overlap area of the two ellipses.
    """

    min_x, min_y, max_x, max_y = get_ellipse_coordinates(ellipse1, ellipse2)
    area = calculate_rectangle_area(min_x, min_y, max_x, max_y)
    hits = 0

    for i in range(num_random_points):
       point = generate_random_point(min_x, min_y, max_x, max_y, i)
       position = is_point_inside_ellipses(ellipse1, ellipse2, point, i)
       if position:
            hits += 1

    overlap_area = (hits * area) / num_random_points
    print(f"Number of points inside both ellipses: {hits}, Total points: {num_random_points}, Estimated overlap area: {overlap_area}")
    return overlap_area


if __name__ == '__main__':
  rand_pts = int(input('Enter the number of random points to hit the bounding rectangle in total: '))

  # Example 1: Two ellipses at the origin
  center1 = Point(0, 0)
  size1 = Point(0, 0)
  center2 = Point(0, 0)
  size2 = Point(0, 0)
  width1 = 2
  width2 = 2
  ellipse1 = Ellipse(center1, size1, width1)
  ellipse2 = Ellipse(center2, size2, width2)
  overlap = compute_overlap_of_ellipses(ellipse1, ellipse2, rand_pts)
  print('Example:1')
  print(f'Overlap area for random points is: {overlap}')

  # Example 2: Two ellipses with different positions and sizes
  center1 = Point(5, 3)
  size1 = Point(0, 0)
  center2 = Point(3, 5)
  size2 = Point(0, 0)
  width1 = 10
  width2 = 8
  ellipse1 = Ellipse(center1, size1, width1)
  ellipse2 = Ellipse(center2, size2, width2)
  overlap = compute_overlap_of_ellipses(ellipse1, ellipse2, rand_pts)
  print('Example:2')
  print(f'Overlap area for random points is: {overlap}')

  # Example 3: Two ellipses with negative coordinates
  center1 = Point(-1, -1)
  size1 = Point(1, 1)
  center2 = Point(-3, 3)
  size2 = Point(3, -3)
  width1 = 6
  width2 = 9
  ellipse1 = Ellipse(center1, size1, width1)
  ellipse2 = Ellipse(center2, size2, width2)
  overlap = compute_overlap_of_ellipses(ellipse1, ellipse2, rand_pts)
  print('Example:3')
  print(f'Overlap area for random points is: {overlap}')

  # Example 4: Two horizontally aligned ellipses
  center1 = Point(-4, 0)
  size1 = Point(0, 0)
  center2 = Point(0, 0)
  size2 = Point(4, 0)
  width1 = 6
  width2 = 6
  ellipse1 = Ellipse(center1, size1, width1)
  ellipse2 = Ellipse(center2, size2, width2)
  overlap = compute_overlap_of_ellipses(ellipse1, ellipse2, rand_pts)
  print('Example:4')
  print(f'Overlap area for random points is: {overlap}')
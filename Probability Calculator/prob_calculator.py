# FCC Course: Scientific Computing with Python
# Project: Probability Calculator
# Author: Wojciech Woźniak
# Date: 12.05.2023


# Import nessesary modules
import copy
import random


# Definition of Hat class
class Hat:

    # Constructor
    def __init__(self, **all_item):

        # Create a list of items
        self.contents = []
        for key, value in all_item.items():
            for itr in range(value):
                self.contents.append(key)

    # draw() method - Draw balls from the hat
    def draw(self, num_balls):
        # If the number of balls to draw is greater than or equal to the number of balls in the hat, return all the balls in the hat
        if num_balls >= len(self.contents):
            return self.contents

        # Otherwise, choose num_balls balls randomly and remove them from the contents list
        balls_drawn = []
        for i in range(num_balls):
            ball = random.choice(self.contents)
            self.contents.remove(ball)
            balls_drawn.append(ball)

        return balls_drawn


# Run an experiment to determine the probability of drawing a specified set of balls from a hat
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    # Track the number of successful experiments
    num_successful_experiments = 0

    # Run the experiment num_experiments times
    for i in range(num_experiments):
        # Make a copy of the hat so we can modify its contents without affecting the original hat
        copy_hat = Hat(**{ball: hat.contents.count(ball)
                       for ball in set(hat.contents)})

        # Draw num_balls_drawn balls from the hat
        balls_drawn = copy_hat.draw(num_balls_drawn)

        # Check if we drew the expected number of each ball type
        success = True
        for ball, expected_quantity in expected_balls.items():
            if balls_drawn.count(ball) < expected_quantity:
                success = False
                break

        # If we drew the expected number of each ball type, count the experiment as successful
        if success:
            num_successful_experiments += 1

    # Calculate the probability of drawing the expected set of balls
    return num_successful_experiments / num_experiments

#!/usr/bin/env python3

# Created by Ryan Chung Kam Chung
# Created in January 2021
# Program generates 10 random numbers and displays the smallest


import random


def smallest(random_numbers):
    # Finds the smallest number

    smallest_number = random_numbers[0]

    for single_element in random_numbers:
        if smallest_number > single_element:
            smallest_number = single_element

    return smallest_number


def main():
    # Generates 10 random numbers and displays the smallest

    random_numbers = []

    for loop_counter in range(0, 10):
        random_numbers.append(random.randint(1, 100))

        if loop_counter < 9:
            print(random_numbers[loop_counter], end=", ")
        else:
            print(random_numbers[loop_counter])

    smallest_number = smallest(random_numbers)

    print("The smallest number is: {}".format(smallest_number))


if __name__ == "__main__":
    main()

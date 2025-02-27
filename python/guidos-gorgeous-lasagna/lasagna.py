"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40 #Bake time in minutes
PREPARATION_TIME = 10 #Preparation time in minutes


def bake_time_remaining(time_in_the_oven: int) -> int:
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    
    return EXPECTED_BAKE_TIME - time_in_the_oven

def preparation_time_in_minutes(layers_lasagna: int) -> int:
    """Calculate the preparation time .

    :param layers_lasagna: int - numbers of layers.
    :return: int - layers

    """
  
    return layers_lasagna * 2
  


def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    """Calculate the total time (prep+bake).

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
 

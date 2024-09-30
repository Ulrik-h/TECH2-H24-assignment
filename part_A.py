# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 07:59:55 2024

@author: ulrik
"""

def std_loops(x):
    
    # Importing square root function
    from math import sqrt
    
    # The length and sum of the sequence of numbers (x) is set to 0 before the loop initiates
    length = 0
    sum_x = 0
    
    # The Sum of Squares is also set to 0
    sum_squares = 0
    
    # The loop itirates over the sequence of numbers (x) and calculated the sum and length of the sequence, as well as the sum of squares
    for i in x:
        sum_x += i
        length += 1
        sum_squares += i**2
    
    # Computing the mean 
    mean = sum_x/length  
    
    # Computing the mean of squares
    mean_of_squares = sum_squares/length
    
    # Computing the variance
    variance = mean_of_squares - (mean**2)
    
    # Computing the standard deviation
    std_deviation = sqrt(variance)
    
    # Returns the standard deviation as a float
    return std_deviation 

 
def std_builtin(x):

    # Importing square root function
    from math import sqrt
    
    # Calculates sum and lenght of the sequence
    sum_x = sum(x)
    length = len(x)
    
    # Calculates sum of squares
    sum_squares = sum([i**2 for i in x])
    
    # Computing the mean 
    mean = sum_x/length  
    
    # Computing the mean of squares
    mean_of_squares = sum_squares/length
    
    # Computing the variance
    variance = mean_of_squares - (mean**2)
    
    # Computing the standard deviation
    std_deviation = sqrt(variance)
    
    # Returns the standard deviation as a float
    return std_deviation 
    

def main():
    
    # Importing standard deviation function from numpy
    from numpy import std
    
    # Defining the list of numbers we are calculating standard deviation for
    num_list = [1, 2, 3, 4, 5]
    
    # Calculating standard deviation using numpy and the two other functions
    std_loop = std_loops(num_list)
    std_built = std_builtin(num_list)
    std_numpy = std(num_list)
    
    # Demonstrating the results
    print(f"The standard deviation of {num_list} is calculated using loops, built-in functions and numpy. The results are: \nLoops: {std_loop: .3f} \nBuilt-in functions: {std_built: .3f} \nNumpy: {std_numpy: .3f}")
    
if __name__ == "__main__":
    main()
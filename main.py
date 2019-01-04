# Created by:   Patrick Archer
# Date:         20 December 2018
# Copyright to the above author. All rights reserved.

"""
Directions - COMPLETE:
Take a list, say for example this one:
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.

Extras - COMPLETE:
(1 - DONE) Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in
    it and print out this new list. Write this in one line of Python.
(2 - DONE) Ask the user for a number and return a list that contains only elements from the original list a that are smaller
    than that number given by the user.
"""

# ################################################# start_funcs

# Compares user-designated value to values in a list.
# All list values less (and not equal to) the user's desired value will be added to another list.
# Resulting list is returned (contains all values less than & not equal to user-specified value).
def printIfLessThan(maxValue):

    startingArray = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    resultArray = []

    for element in range(len(startingArray)):
        #print(str(startingArray[element])) # debug
        if (startingArray[element] < maxValue):
            resultArray.append(startingArray[element])

    return resultArray

# ################################################# end_funcs/start_main

userNum = input("\nPlease enter the number you want the array elements to be checked against.\n")

try:
    userNum = int(userNum)
    print("\n<CONSOLE>: Now performing calculations. The result is displayed below.\n")
    resultingArray = printIfLessThan(userNum)
    print("The values in the pre-determined list that are less than your entered value (" +
          str(userNum) + ") is: \n" + str(resultingArray))
except (ValueError):
    print("<ERROR>: ____")

# ################################################# end_main



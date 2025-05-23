def missing_number(list):
    
    #Counts how many numbers are in the list and Adds 1 to account for the missing number.
    n=len(list)+1
    
    #Calculate the expected sum of all numbers in the list 1 to n
    expected_sum =n*(n+1)//2
    
    #Calculate the actual sum of the given list
    actual_sum= sum(list) #this adds up all the numbers in the list

    #Subtract the actual sum from the expected sum to get the missing number
    missing_number = expected_sum - actual_sum
    
    return missing_number

import ast  # Abstract Syntax Trees(ast):converts string input into Python list

user_input=input("Enter the List:")

missing_value=ast.literal_eval(user_input) #Convert string to actual list safely

print("missing_value:",missing_number(missing_value))
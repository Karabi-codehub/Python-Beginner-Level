def missing_number(logs):
    
    #We are finding the biggest number in the list called logs.
    #So in [1, 2, 4, 5, 6, 8, 11], the biggest is 11.
    #We save it in a variable called n
    n=max(logs)
    
    #We are making a set of all numbers starting from 1 to n
    #The range(1, n+1) gives us numbers like [1, 2, 3, ..., 11].
    #We wrap it in set(...) to make it a set, which is like a box of numbers without duplicates.full_set will be like:{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
    full_set=set(range(1,n+1))
    
    #we change the input list logs into a set too
    log_set=set(logs) #logs = [1, 2, 4, 5, 6, 8, 11],then logs_set = {1, 2, 4, 5, 6, 8, 11}
    
    #set subtraction
    missing_value=full_set-log_set
    
    return sorted(list(missing_value))


import ast  # Abstract Syntax Trees(ast):converts string input into Python list

user_input=input("Enter the List:")

missing_value=ast.literal_eval(user_input) #Convert string to actual list safely

print("missing_value:",missing_number(missing_value))
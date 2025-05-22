#we have a list, but inside it, some elements are normal numbers and some are lists again (nested, the list with sub-lists (like [1, [2, 3]])). You want to make one flat list that includes all the numbers
#[1, [2, 3], [4, [5]]] → [1, 2, 3, 4, 5],This is called flattening the list — turning a list with sub-lists into one single list with all the values.
#Use recursion: If the item is a number, just add it to the result.
               #If the item is a list, we open it, and check its items (recursively).

def flatten_list(nested_list):
    
    result=[]    #We create an empty list called result.This will store all the final values (like [1, 2, 3, 4, 5])
    
    for item in nested_list: # Go through each item in the nested_list
    
        if isinstance(item,list): #This checks: Is the item a list?
                                  #If yes (like [2, 3]) → we need to go inside it.
                                  #If no (like 1) → it’s just a number
            
            result.extend(flatten_list(item)) # If item is a list,Call the function again (recursion) and add the result
                                              
        else:
            result.append(item)  #If the item is not a list (just a number),Add it to the result list
           

    return result

            
import ast  # Abstract Syntax Trees(ast):converts string input into Python list

user_input=input("Enter the Nested List:")

nested_list=ast.literal_eval(user_input) #Convert string to actual list safely


print("flatten_list:",flatten_list(nested_list))

#If n is 0, return 1. (This is the base case that stops the recursion.)
#Otherwise, return n * factorial(n - 1)

def factorial(n):
    
    #base case:If the input number is 0, return 1 (because 0! is 1)
    if n==0:
        return 1
    
    #recursive case
    else:
        # Recursive case: call the function again with (n - 1)
        return n * factorial(n - 1)
        

user_input=int(input("Enter the number:"))

# Call the function with user input
result = factorial(user_input)

print("Factorial is:", result)
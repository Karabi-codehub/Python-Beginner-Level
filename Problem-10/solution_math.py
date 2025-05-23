#Using mathematical operations like // and %
#n % 10: Gets the last digit of a number. e.g., 9875 % 10 = 5
#n // 10: Removes the last digit of a number.e.g., 9875 // 10 = 987

user_input=int(input("Enter the number:"))

sum_of_digit=0 #Initialize sum to 0

# Use a while loop to go through all digits

while user_input > 0:
    digit= user_input % 10 # Get the last digit
    
    sum_of_digit+=digit # Add it to the sum
    
    user_input =  user_input//10 # Remove the last digit
    
print(sum_of_digit)
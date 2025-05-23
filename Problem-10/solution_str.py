#Using string conversion and a loop.
#Convert the number into a string (so we can look at each digit like a letter)
#Loop through each character 
#Convert it back to an integer and add it to the sum.

digit=int(input("Enter the number:"))

#Convert the number to a string
digit_str=str(digit)

#Initialize the sum 
sum_of_digits=0

#Go through each character in the string
for char in digit_str:
    digit_convert=int(char) #Convert character back to an integer
    sum_of_digits+=digit_convert  # Add to the sum
    
print("sum of digits:",sum_of_digits)
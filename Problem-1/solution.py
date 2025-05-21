#create a function that reverse string
def reverse_string(text):
    
    #Start with an empty string to store the reversed result
    result=""
    
    #Loop through the string from the last character to the first
    i=len(text)-1  # Start from the last index (length - 1)
    while i >=0:
        result=result + text[i] # Add the character at position i to result
        i=i-1 # Move to the previous character
    return result #Return the reversed string

string= input("Enter the string:")
reversed_word=reverse_string(string)
print("Reversed string:", reversed_word)

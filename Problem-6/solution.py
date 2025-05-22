Input_string =input("Enter the sentence:")

#Split the string into words
words=Input_string.split() # ['python', 'for', 'web', 'developers']

# Create an empty list to hold capitalized words
capitalized_words=[]

#Loop through each word
for word in words:
    
    # Capitalize first letter and add the rest of the word
    capitalized_word=word[0].upper()+word[1:] #word[0]:This gets the first character of the word.word = "python", then word[0] = 'p'
                                               #.upper():Converts that character to uppercase. So 'p'.upper() becomes 'P'
                                               #word[1:]:This is slicing. It means “get everything in the word starting from index 1 to the end.” For "python", word[1:] is 'ython' (it skips the first letter).
                                               # + :Combines the capitalized first letter with the rest of the word. So 'P' + 'ython' = 'Python'
                                             
    # Add to the result list
    capitalized_words.append(capitalized_word)
    
#Join the capitalized words into string
result=' '.join(capitalized_words)
print(result)
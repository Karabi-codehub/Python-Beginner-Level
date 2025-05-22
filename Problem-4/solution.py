
def is_palidrome(text):
    
    text=''.join(char.lower() for char in text if char.isalnum())
    
    return text==text[::-1]

user_input=input("Enter text:")

print(is_palidrome(user_input))

#.lower()	To ignore differences between uppercase and lowercase letters
#Words like "Madam" and "madam" are the same in meaning, but Python sees them as different because of the uppercase "M".
#.isalnum()	To remove spaces and punctuation — only keep letters and numbers
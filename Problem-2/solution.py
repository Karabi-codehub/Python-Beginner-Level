sentence= input("Enter the sentence:")

#Convert the sentence to lowercase
sentence = sentence.lower() #Makes sure we treat uppercase and lowercase vowels the same.

vowels = "aeiou"

#Initialize a counter
#We’re starting from zero — we haven’t counted any vowels yet.
#As we loop through each character in the sentence, we want to increment this counter each time we find a vowel.
#Imagine you're counting coins in a box.You start with zero coins (vowel_count = 0), then add one for each coin you find (vowel_count += 1).
vowel_count = 0

#Loop through each character in the sentence
for char in sentence:
    if char in vowels: #if the character is a vowel
        vowel_count+=1  #If yes, increase the counter

print("Number of vowels:", vowel_count)
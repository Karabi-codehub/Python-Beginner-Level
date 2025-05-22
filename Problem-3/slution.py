import ast

user_input = input('Enter tags in format(tags:["word1","word2","word3",......]): ')

try:
    tag_start = user_input.index('[')  # Find where the list starts
    tag_part = user_input[tag_start:]  # Extract just the list part
    tags = ast.literal_eval(tag_part)  # Convert string to actual Python list

    if not isinstance(tags, list):
        raise ValueError("Not a list.")  # Raise error if not a list

except Exception as error:
    print("❌ Invalid input format.")
    exit()

# Create sets to track seen and duplicate items
seen = set()
duplicates = set()

for tag in tags:
    tag = tag.strip()  # Remove extra spaces
    if tag in seen:
        duplicates.add(tag)
    else:
        seen.add(tag)

# Convert to list and print
print("Duplicate tags:", list(duplicates))

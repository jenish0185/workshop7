filename = 'original_text.txt'

with open(filename, 'r') as file:
    content = file.read()

count = 0
for letter in content:
    if letter.lower() == 'e':
        count += 1

print(f"The letter 'e' appears {count} times in the file.")
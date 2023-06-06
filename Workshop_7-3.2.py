with open('origial_text.txt', 'r') as original_file:
    lines = original_file.readlines()

with open('new_text.txt', 'w') as new_file:
    for i in range(0, len(lines)):
        new_file.write(lines[i])
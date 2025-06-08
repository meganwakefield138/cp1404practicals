"""
CP1404 Practical

This file contains questions and answers for files.
Make the appropriate choice of file-reading technique for each of these questions:
1. Read()
2. Readline()
3. Readlines()
4. For line in file
"""

# 1. Write code that asks a user for their name and writes their name to a file called name.txt. Use open and close for this question.
name = input("Enter your name: ")
file_out = open("name.txt", "w")
print(name, file=file_out)
file_out.close()

# 2. Write code that opens name.txt and reads the name from it then prints it. Use open and close for this question.
file_in = open("name.txt", "r")
name = file_in.read().strip()
print(f"Hi {name}!")
file_in.close()

# 3. Create a text file called numbers.txt and save it in your pratical directory. Put the following three numbers 17, 42, 400 on separate lines.
# Then write code that only reads the first two numbers, adds them, and prints the result. Use with instead of open and close.
file_out = open("numbers.txt", "w")
print("17", file=file_out)
print("42", file=file_out)
print("400", file=file_out)
file_out.close()

file_in = open("numbers.txt", "r")
with file_in as f:
    first_line = f.readline().strip()
    second_line = f.readline().strip()
    print(f"First two: {first_line} + {second_line} = {int(first_line) + int(second_line)}")

# 4. Print the total for all lines in numbers.txt. This should work for a file with any number of numbers.
# Use with instead of open and close.
file_in = open("numbers.txt", "r")
with open("numbers.txt", "r") as numbers_file:
    total = 0
    for line in numbers_file:
        total += int(line.strip())
    print(f"Total: {total}")

file_in.close()
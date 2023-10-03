"""
CP1404 - Prac 3
Become comfortable with reading files.
"""

# Q1. Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it.
# Remember to close your file.

out_file = open("name.txt", "w")
name = input("Enter your name:  ")
print(f"{name}", file=out_file)
out_file.close()

# Q2. (In the same file, but as if it were a separate program) Write code that opens "name.txt" and reads the name (as
# above) then prints, "Your name is Bob" (or whatever the name is in the file).

in_file = open("name.txt", "r")
name = in_file.read()
in_file.close()
print(f"Your name is {name}")

# Q3. Create a text file called numbers.txt and save it in your prac directory. Put the following three numbers on
# separate lines in the file and save it:
# 17
# 42
# 400
# Write code that opens "numbers.txt", reads only the first two numbers and adds them together then prints the result,
# which should be... 59.

out_file = open("numbers.txt", "w")
print("17\n42\n400", file=out_file)
out_file.close()

in_file = open("numbers.txt", "r")
line1 = int(in_file.readline())
line2 = int(in_file.readline())
in_file.close()
sum = line1 + line2
print(sum)

# Q4. Now write a fourth block of code that prints the total for all lines in numbers.txt or a file with any number of
# numbers.

total = 0
in_file = open("numbers.txt", "r")
for line in in_file:
    total += int(line)
in_file.close()
print(total)
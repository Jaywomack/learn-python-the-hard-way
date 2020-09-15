# from the module sys import the function or argument argv
from sys import argv

# sets argv = to script and the input file entered in the terminal when you run the script
script, input_file = argv

# function that prints everything that it reads from the file passed to the function


def print_all(f):
    print(f.read())

# function that sets the chunks current position


def rewind(f):
    f.seek(0)

# function that uses the readline method to read one line at the chosen line of the file passed in using the readline method of which is established by line_count


def print_a_line(line_count, f):
    print(line_count, f.readline())


# sets current file to the method open with a parameter that accepts a file to be opened that is passed in at the terminal when the script opens
current_file = open(input_file)

print("First let's print the whole file:\n")
# prints the entire file that is passed in at the terminal initially
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
# passes current file to the rewind function that sets the chunk at the beginning of the file
rewind(current_file)

print("Let's print the three lines:")
# sets the current line var to 1 and passes the arguments current line and current file to the print a line function which will read the line and print it
current_line = 1
print_a_line(current_line, current_file)
# does the same thing but iterates to the next line
current_line += 1
print_a_line(current_line, current_file)
# does the same thing but iterates to the next line

current_line += 1
print_a_line(current_line, current_file)

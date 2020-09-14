# from sys imports the module argv which seeks input from the user at the command line before running the program
from sys import argv

# sets the values of script and filename to argv
script, filename = argv

# sets txt to the value of open with the parameter of filename which will be input at the command line from the user
txt = open(filename)

# prints a string with the title of the file
print(f"Here's your {filename}:")
# prints the file to the terminal by printing the txt.read function which will read the file that the user enters into the argv prompt for filename
print(txt.read())

# print string to terminal
print("Type the filename again:")
# sets the user input to the variable file_again
file_again = input("> ")

# sets the variable txt_again to the value of the file that the userinputs by running the open function on the user input
txt_again = open(file_again)

# print the file by reading the value of the txt_again variable which is set by the user input
print(txt_again.read())

import random
import string 
import optparse
from termcolor import colored
from prettytable import PrettyTable
from ImageDraw import DrawPasswordCard

# Create a table
table = PrettyTable()

parser = optparse.OptionParser()
parser.add_option('-c', '--column', dest='column', help='Number of columns', type='int', default=5)
parser.add_option('-l', '--charLength', dest='charLength', help='Number of characters', type='int', default=3)
parser.add_option('-o', '--output', dest='output', help='Output file', type='string', default='output.txt')
(options, args) = parser.parse_args()

if options.column:
    columnLength = options.column

def GetRandomChar(n):
    randomChars = ""
    for _ in range(n):
        randomChar = random.choice(string.ascii_letters + string.digits + string.punctuation)
        randomChars += randomChar
    return randomChars

# Create a table
table = PrettyTable()

# Add the alphabet as the field names
table.field_names = [" "] + [(chr(ord('a') + i) + chr(ord('a') + i + 1) + chr(ord('a') + i + 2)).upper() for i in range(0, 21, 3)] + ["VWX", "YZ."]

# Add the random characters as rows
for index in range(columnLength):
    row = [index+1] + [GetRandomChar(options.charLength) for _ in range(9)]
    table.add_row(row)
    table.add_row([" "] * 10)  # Add an empty row
#Write to file 
with open(options.output, 'w') as f:
    f.write(str(table))
    f.close()

# Draw the password card
DrawPasswordCard(options.output)

print(colored(table, 'green'))
print(colored(f'Output file: {options.output}', 'blue'))







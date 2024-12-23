import os
import sys
from time import sleep as wait
import shlex

def show(argument):
    print(argument)
commands =  {
    "show" : show
}
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    print("Error: No filename provided.")
    sys.exit(1)

def parse(line):
    shlexedline = shlex.split(line)
    command = shlexedline[0]
    arguments = shlexedline[1:]
    return command, arguments

def main():
    print("Opening script....")
    with open(filename, "r") as file:
        for line in file:
            command, arguments = parse(line)
            if command in commands:
                print("good job")
            else:
                print(f"Syntax error: {command} command not found in base.")

main()
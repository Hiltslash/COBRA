import os
import sys
from time import sleep as wait
import shlex
variables = {}

def show(argument):
    if "var" in argument:
        dontuse, argument = parse(argument)
        print(variables[argument])
    else:
        print(argument)
def cvar(name, value):
    try:
        int(value)
    except ValueError:
        str(value)
    variables[name] = value
commands =  {
    "show" : show,
    "cvar" : cvar,
}
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    print("Error: No filename provided.")
    sys.exit(1)

def parse(line):
    shlexedline = shlex.split(line)
    command = shlexedline[0]
    try:
        if shlexedline[2]:
            arguments = shlexedline[1:]
        else:
            arguments = shlexedline[1]
    except IndexError:
        arguments = shlexedline[1]
    return command, arguments

def main():
    with open(filename, "r") as file:
        for line in file:
            command, arguments = parse(line)
            if command in commands:
                try:
                    if command.lower() == "show":
                        show(arguments)
                    if command.lower() == "cvar":
                        cvar(*arguments)
                except TypeError as e:
                    raise TypeError
            else:
                print(f"Syntax error: {command} command not found in base.")

main()
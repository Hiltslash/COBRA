import os
from os import system as syst
import sys
from time import sleep as wait
import shlex
def clear(): syst("clear")
variables = {"calresult" : 0}
def checkvar(string):
    if "var" in string and type(string) == str:
        donotuse, important = parse(string)
        importants = variables[important]
        return importants
    else:
        return string

def ifcondition(condition, exresult, thencommand, *thenarguments):
    conditionvar = checkvar(condition)
    exresultvar = checkvar(exresult)
    if str(conditionvar) == str(exresultvar):
        if thencommand in commands:
            commands[thencommand](*thenarguments)
    else:
        pass


def calculate(numberone, operation, numbertwo):
    try:
        numberone = int(numberone)
        numbertwo = int(numbertwo)
        if operation == "*":
            return numberone * numbertwo
        elif operation == "/":
            return numberone / numbertwo
        elif operation == "+":
            return numberone + numbertwo
        elif operation == "-":
            return numberone - numbertwo
        elif operation == "#":
            return numberone ** numbertwo
    except ValueError:
        print("VALUE ERROR: PLEASE PROVIDE TWO INTEGERS")
        raise ValueError

def waittime(seconds):
    wait(int(seconds))
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

def takeinput(variable, message):
    variables[variable] = input(str(message))

def forloop(times, command, *arguments):
    for i in range(int(times)):
        commands[command](*arguments)
commands =  {
    "show" : show,
    "cvar" : cvar,
    "cal" : calculate,
    "clear" : clear,
    "input" : takeinput,
    "for" : forloop,
    "wait" : waittime,
    "if" : ifcondition
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
            if line:
                command, arguments = parse(line)
                if command in commands:
                    try:
                        if command.lower() == "show":
                            show(arguments)
                        elif command.lower() == "input":
                            takeinput(*arguments)
                        elif command.lower() == "for":
                            forloop(*arguments)
                        elif command.lower() == "wait":
                            waittime(arguments)
                        elif command.lower() == "if":
                            ifcondition(*arguments)
                        elif command.lower() == "cvar":
                            cvar(*arguments)
                        elif command.lower() == "cal":
                            # Calculate the result using the first three arguments
                            calresult = calculate(*arguments[:3])
                            # If a fourth argument (variable name) is provided, assign the result to that variable
                            if len(arguments) > 3:
                                variables[arguments[3]] = calresult
                        elif command.lower() == "clear":
                            clear()
                    except TypeError as e:
                        raise TypeError
                else:
                    print(f"Syntax error: {command} command not found in base.")

main()

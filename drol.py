#!/usr/bin/env python
#file: drol.py
#By: Bradley Sadowsky, MIT License <bradley.sadowsky@gmail.com>
#11/23/2016
#Current Version: 1.0
#Updated on 11/23/16
#Double Register Optimization Language (DROL) - Compiler
from sys import argv
from os import system
argl = len(argv)

def compile(drolstr, outfile): # Compile DROL code into C code
    # Beginning of C file
    init = '#include <stdio.h>\n#include <stdlib.h>\nvoid main(void) {\n\tint regone = 0;\n\tint regtwo = 0;\n'
    # End of C file
    end = '}\n'
    # Increment register one by 1
    i = '\tregone = regone + 1;\n'
    # Increment register two by 1
    k = '\tregtwo = regtwo + 1;\n'
    # Decrement register one by 1
    d = '\tregone = regone - 1;\n'
    # Decrement register two by 1
    e = '\tregwto = regtwo = 1;\n'
    # Display register one to the screen
    o = '\tprintf("%d", regone);\n'
    # Display register two to the screen
    p = '\tprintf("%d", regtwo);\n'
    # Display register one to the screen IF REGISTER ONE IS ASCII (0-255)
    a = '\tif (regone >= 0 && regone <= 255) {\n\t\tprintf("%c", regone);\n\t}\n'
    # Display register two to the screen IF REGISTER ONE IS ASCII (0-255)
    b = '\tif (regtwo >= 0 && regtwo <= 255) {\n\t\tprintf("%c", regtwo);\n\t}\n'
    # Display newline
    newline = '\tprintf("\\n");\n'
    # Set register one to user inputted number
    n = '\tscanf("%d", &regone);\n'
    # Set register two to user inputted number
    q = '\tscanf("%d", &regtwo);\n'
    # Set register one to zero
    z = '\tregone = 0;\n'
    # Set register two to zero
    y = '\tregtwo = 0;\n'
    # Set both registers to the contents of register one
    one = '\tregtwo = regone;\n'
    # Set both registers to the contents of register two
    two = '\tregone = regtwo;\n'
    # Set register one to the sum of the registers
    s = '\tregone = regone + regtwo;\n'
    # Set register two to the sum of the registers
    u = '\tregtwo = regone + regtwo;\n'
    # Set register one to the difference of the registers
    f = '\tregone = regone - regtwo;\n'
    # Set register two to the difference of the registers
    g = '\tregtwo = regone - regtwo;\n'
    # Set register one to the product of the registers
    m = '\tregone = regone * regtwo;\n'
    # Set register two to the product of the registers
    r = '\tregtwo = regone * regtwo;\n'
    # Set register one to register one squared
    e = '\tregone = regone * regone;\n'
    # Set register two to register two squared
    h = '\tregtwo = regtwo * regtwo;\n'
    # Tests if the registers are equal; If not equal, the program exits
    j = '\tif (regone != regtwo) {\n\t\texit(0);\n\t}\n'
    # Swaps register one and register two
    swap = '\tint tempone = regone;\n\tint temptwo = regtwo;\n\tregone = temptwo;\n\tregtwo = tempone;\n'
    # Left shift register one by one
    lshftone = '\tregone = regone << 1;\n'
    # Left shift register two by one
    lshfttwo = '\tregtwo = regtwo << 1;\n'
    # Right shift register one by one
    rshftone = '\tregone = regone >> 1;\n'
    # Right shift register two by one
    rshfttwo = '\tregtwo = regtwo >> 1;\n'
    # Flip bits in register one
    flipone = '\tregone = ~regone;\n'
    # Flip bits in register two
    fliptwo = '\tregtwo = ~regtwo;\n'
    # XOR register one to register two
    xorone = '\tregone = regone ^ regtwo;\n'
    # XOR register two to register one
    xortwo = '\tregtwo = regone ^ regone;\n'
    # OR register one to register two
    orone = '\tregone = regone | regtwo;\n'
    # OR register two to register one
    ortwo = '\tregtwo = regone | regtwo;\n'
    # AND register one to register two
    andone = '\tregone = regone & regtwo;\n'
    # AND register two to register one
    andtwo = '\tregtwo = regone & regtwo;\n'
    outfile.write(init)
    for char in drolstr:
        if char == "i":
            outfile.write(i)
        elif char == "k":
            outfile.write(k)
        elif char == "d":
            outfile.write(d)
        elif char == "e":
            outfile.write(e)
        elif char == "o":
            outfile.write(o)
        elif char == "p":
            outfile.write(p)
        elif char == "a":
            outfile.write(a)
        elif char == "b":
            outfile.write(b)
        elif char == "!":
            outfile.write(newline)
        elif char == "n":
            outfile.write(n)
        elif char == "q":
            outfile.write(q)
        elif char == "z":
            outfile.write(z)
        elif char == "y":
            outfile.write(y)
        elif char == "1":
            outfile.write(one)
        elif char == "2":
            outfile.write(two)
        elif char == "s":
            outfile.write(s)
        elif char == "u":
            outfile.write(u)
        elif char == "f":
            outfile.write(f)
        elif char == "g":
            outfile.write(g)
        elif char == "m":
            outfile.write(m)
        elif char == "r":
            outfile.write(r)
        elif char == "e":
            outfile.write(e)
        elif char == "h":
            outfile.write(h)
        elif char == "j":
            outfile.write(j)
        elif char == "*":
            outfile.write(swap)
        elif char == "<":
            outfile.write(lshftone)
        elif char == ",":
            outfile.write(lshfttwo)
        elif char == ">":
            outfile.write(rshftone)
        elif char == ".":
            outfile.write(rshfttwo)
        elif char == "~":
            outfile.write(flipone)
        elif char == "`":
            outfile.write(fliptwo)
        elif char == "^":
            outfile.write(xorone)
        elif char == "6":
            outfile.write(xortwo)
        elif char == "|":
            outfile.write(orone)
        elif char == "\\":
            outfile.write(ortwo)
        elif char == "&":
            outfile.write(andone)
        elif char == "7":
            outfile.write(andtwo)
    outfile.write(end)

def main(argnum = 1):
    try:
        inptfile = open(argv[argnum], "r")
    except IOError:
        from sys import exit
        exit("File error: File does not exist")
    try:
        outfile = open("a.c", "w")
    except IOError:
        from sys import exit
        exit("Unknown file error: Do you have permission to write to this file?")
    compile(inptfile.read(), outfile)
    inptfile.close()
    outfile.close()

if argl == 2: # Take second CLI argument as DROL source file
    main()
    system("gcc a.c") # Default C compiler selected as GCC
    system("rm a.c")
elif argl == 3: # Take single CLI flag
    if argv[1] == "-c": # Just compile to C code
        main(2)
    else:
       from sys import exit
       exit("Error: invalid flag")
else:
    from sys import exit
    exit("Error: No input files present")

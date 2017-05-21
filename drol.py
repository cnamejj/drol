#!/usr/bin/env python
#file: drol.py
#By: Bradley Sadowsky, MIT License <bradley.sadowsky@gmail.com>
#11/23/2016
#Current Version: 2.0
#Updated on 5/20/17
#Double Register Optimization Language (DROL) - Compiler
from sys import argv
from os import system
arg_length = len(argv)

def compile(drol_string, outfile): # Compile DROL code into C code
    drol_string = drol_string.replace(" ", "")
    drol_string = drol_string.replace("\n", "")
    drol_string = drol_string.replace("\t", "")
    # Beginning of C file
    init = '#include <stdio.h>\n#include <stdlib.h>\nvoid main(void) {\nint regone = 0;\nint regtwo = 0;\nint tempone;\nint temptwo;\n'
    # End of C file
    end = '}\n'
    def lookup(char):
        # Exit the program successfully
        x = 'exit(0);\n'
        # Increment register one by 1
        i = 'regone = regone + 1;\n'
        # Increment register two by 1
        k = 'tregtwo = regtwo + 1;\n'
        # Decrement register one by 1
        d = 'regone = regone - 1;\n'
        # Decrement register two by 1
        e = 'regtwo = regtwo - 1;\n'
        # Display register one to the screen
        o = 'printf("%d", regone);\n'
        # Display register two to the screen
        p = 'printf("%d", regtwo);\n'
        # Display register one to the screen IF REGISTER ONE IS ASCII (0-255)
        a = 'if (regone >= 0 && regone <= 255) {\nprintf("%c", regone);\n}\n'
        # Display register two to the screen IF REGISTER ONE IS ASCII (0-255)
        b = 'if (regtwo >= 0 && regtwo <= 255) {\nprintf("%c", regtwo);\n}\n'
        # Display newline
        newline = 'printf("\\n");\n'
        # Set register one to user inputted number
        n = 'scanf("%d", &regone);\n'
        # Set register two to user inputted number
        q = 'scanf("%d", &regtwo);\n'
        # Set register one to zero
        z = 'regone = 0;\n'
        # Set register two to zero
        y = 'regtwo = 0;\n'
        # Set both registers to the contents of register one
        one = 'regtwo = regone;\n'
        # Set both registers to the contents of register two
        two = 'regone = regtwo;\n'
        # Set register one to the sum of the registers
        s = 'regone = regone + regtwo;\n'
        # Set register two to the sum of the registers
        u = 'regtwo = regone + regtwo;\n'
        # Set register one to the difference of the registers
        f = 'regone = regone - regtwo;\n'
        # Set register two to the difference of the registers
        g = 'regtwo = regone - regtwo;\n'
        # Set register one to the product of the registers
        m = 'regone = regone * regtwo;\n'
        # Set register two to the product of the registers
        r = 'regtwo = regone * regtwo;\n'
        # Set register one to register one squared
        l = 'regone = regone * regone;\n'
        # Set register two to register two squared
        h = 'regtwo = regtwo * regtwo;\n'
        # Swaps register one and register two
        swap = 'tempone = regone;\ntemptwo = regtwo;\nregone = temptwo;\nregtwo = tempone;\n'
        # Left shift register one by one
        lshftone = 'regone = regone << 1;\n'
        # Left shift register two by one
        lshfttwo = 'regtwo = regtwo << 1;\n'
        # Right shift register one by one
        rshftone = 'regone = regone >> 1;\n'
        # Right shift register two by one
        rshfttwo = 'regtwo = regtwo >> 1;\n'
        # Flip bits in register one
        flipone = 'regone = ~regone;\n'
        # Flip bits in register two
        fliptwo = 'regtwo = ~regtwo;\n'
        # XOR register one to register two
        xorone = 'regone = regone ^ regtwo;\n'
        # XOR register two to register one
        xortwo = 'regtwo = regone ^ regone;\n'
        # OR register one to register two
        orone = 'regone = regone | regtwo;\n'
        # OR register two to register one
        ortwo = 'regtwo = regone | regtwo;\n'
        # AND register one to register two
        andone = 'regone = regone & regtwo;\n'
        # AND register two to register one
        andtwo = 'regtwo = regone & regtwo;\n'
        
        if char == "x":
            return x
        elif char == "0":
            return ""
        elif char == "i":
            return i
        elif char == "k":
            return k
        elif char == "d":
            return d
        elif char == "e":
            return e
        elif char == "o":
            return o
        elif char == "p":
            return p
        elif char == "a":
            return a
        elif char == "b":
            return b
        elif char == "!":
            return newline
        elif char == "n":
            return n
        elif char == "q":
            return q
        elif char == "z":
            return z
        elif char == "y":
            return y
        elif char == "1":
            return one
        elif char == "2":
            return two
        elif char == "s":
            return s
        elif char == "u":
            return u
        elif char == "f":
            return f
        elif char == "g":
            return g
        elif char == "m":
            return m
        elif char == "r":
            return r
        elif char == "l":
            return l
        elif char == "h":
            return h
        elif char == "*":
            return swap
        elif char == "<":
            return lshftone
        elif char == ",":
            return lshfttwo
        elif char == ">":
            return rshftone
        elif char == ".":
            return rshfttwo
        elif char == "~":
            return flipone
        elif char == "`":
            return fliptwo
        elif char == "^":
            return xorone
        elif char == "6":
            return xortwo
        elif char == "|":
            return orone
        elif char == "\\":
            return ortwo
        elif char == "&":
            return andone
        elif char == "7":
            return andtwo
        else:
            return ""
    
    outfile.write(init)
    drol_iter = iter(drol_string.lower())
    location = 0
    for char in drol_iter:
        if char == "j" or char == '"': # If registers are equal (j) or registers are not equal ("), execute next x commands, else skip
            try:
                block_length = drol_string[location + 1] + drol_string[location + 2] + drol_string[location + 3] + drol_string[location + 4]
                if block_length.isdigit() == False:
                    from sys import exit
                    exit("drol.py: LoopError: missing loop length declaration")
                block_length = int(block_length)
                if char == "j":
                    outfile.write('if (regone == regtwo) {\n')
                elif char == '"':
                    outfile.write('if (regone != regtwo) {\n')
                i = 0
                j = 1
                while i != block_length:
                    outfile.write(lookup(drol_string[location + j + 4]))
                    i = i + 1
                    j = j + 1
                outfile.write('\n}\n')
                location = location + block_length + 5
                i = 0
                while i != block_length + 4:
                    drol_iter.next()
                    i = i + 1
            except StopIteration:
                pass
            except IndexError:
                pass
        elif char == "w" or char == "'": # While the registers are equal (w) or the registers are not equal ('), the next x commands are executed
            try:
                if char == "w":
                    outfile.write('while (regone == regtwo) {\n')
                elif char == "'":
                    outfile.write('while (regone != regtwo) {\n')
                block_length = drol_string[location + 1] + drol_string[location + 2] + drol_string[location + 3] + drol_string[location + 4]
                if block_length.isdigit() == False:
                    from sys import exit
                    exit("drol.py: LoopError: missing loop length declaration")
                block_length = int(block_length)
                i = 0
                j = 1
                while i != block_length:
                    outfile.write(lookup(drol_string[location + j + 4]))
                    i = i + 1
                    j = j + 1
                outfile.write('\n}\n')
                location = location + block_length + 5
                i = 0
                while i != block_length + 4:
                    drol_iter.next()
                    i = i + 1
            except StopIteration:
                pass
            except IndexError:
                pass
        elif char == ":": # Subroutine declaration
            try:
                block_length = drol_string[location + 1] + drol_string[location + 2] + drol_string[location + 3] + drol_string[location + 4]
                if block_length.isdigit() == False:
                    from sys import exit
                    exit("drol.py: SubroutineError: missing function length declaration")
                block_length = int(block_length)
                subroutine_name = drol_string[location + 5] + drol_string[location + 6] + drol_string[location + 7] + drol_string[location + 8]
                outfile.write('void ' + subroutine_name + '(void) {\n')
                i = 0
                j = 1
                while i != block_length:
                    outfile.write(lookup(drol_string[location + j + 8]))
                    i = i + 1
                    j = j + 1
                outfile.write('\n}\n')
                location = location + block_length + 9
                i = 0
                while i != block_length + 8:
                    drol_iter.next()
                    i = i + 1
            except StopIteration:
                pass
            except IndexError:
                pass
        elif char == ";": # Subroutine call
            try:
                subroutine_name = drol_string[location + 1] + drol_string[location + 2] + drol_string[location + 3] + drol_string[location + 4]
                outfile.write(subroutine_name + '();\n')
                location = location + 4
                i = 0
                while i != 4:
                    drol_iter.next()
                    i = i + 1
            except StopIteration:
                pass
            except IndexError:
                pass
        else:
            outfile.write(lookup(char))
            location = location + 1
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

if arg_length == 2: # Take second CLI argument as DROL source file
    main()
    system("gcc a.c") # Default C compiler selected as GCC
    system("rm a.c")
elif arg_length == 3: # Take single CLI flag
    if argv[1] == "-c": # Just compile to C code
        main(2)
    else:
       from sys import exit
       exit("Error: invalid flag")
else:
    from sys import exit
    exit("Error: No input files present")

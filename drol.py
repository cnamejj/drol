#!/usr/bin/env python
#file: drol.py
#By: Bradley Sadowsky, MIT License <bradley.sadowsky@gmail.com>
#11/23/2016
#Current Version: 3.0.0
#Updated on 5/23/17
#Double Register Optimization Language (DROL) - Compiler
from sys import argv
from sys import exit
from os import system
import re
arg_length = len(argv)

def compile(drol_string, outfile, header = 1): # Compile DROL code into C code
    drol_string = re.sub(r'{.+?}', '', drol_string) # Remove comments
    drol_string = drol_string.replace(" ", "")
    drol_string = drol_string.replace("\n", "")
    drol_string = drol_string.replace("\t", "")
    if header == 1:
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
        k = 'regtwo = regtwo + 1;\n'
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
    
    if header == 1:
        outfile.write(init)
    else:
        code = ""
    drol_iter = iter(drol_string.lower())
    location = 0
    for char in drol_iter:
        if char == "j" or char == '"': # If loop
            try:
                if char == "j": # Standard block length (4 digits long)
                    block_length = drol_string[location + 3] + drol_string[location + 4] + drol_string[location + 5] + drol_string[location + 6]
                    header_length = 6 # Instruction header length
                elif char == '"': # Extended block length (8 digits long)
                    block_length = drol_string[location + 3] + drol_string[location + 4] + drol_string[location + 5] + drol_string[location + 6] + drol_string[location + 7] + drol_string[location + 8] + drol_string[location + 9] + drol_string[location + 10]
                    header_length = 8 # Instruction header length
                if block_length.isdigit() == False:
                    exit("drol.py: LoopError: missing loop length declaration")
                block_length = int(block_length)
                compare_op = drol_string[location + 1] + drol_string[location + 2]
                if compare_op == "==" or compare_op == "!=" or compare_op == ">>" or compare_op == "<<":
                    pass
                elif compare_op == ">>":
                    compare_op = ">"
                elif compare_op == "<<":
                    compare_op = "<"
                else:
                    exit("drol.py: LoopError: Invalid comparison operator")
                if header == 1:
                    outfile.write('if (regone ' + compare_op + ' regtwo) {\n')
                else:
                    code = code + 'if (regone ' + compare_op + ' regtwo) {\n'
                i = 0
                j = 1
                mini_block = ""
                while i != block_length:
                    mini_block = mini_block + drol_string[location + j + header_length]    
                    i = i + 1
                    j = j + 1
                if header == 1:
                    outfile.write(compile(mini_block, outfile, 0))
                    outfile.write('}\n')
                else:
                    code = code + compile(mini_block, outfile, 0)
                    code = code + '}\n'
                location = location + block_length + header_length + 1
                i = 0
                while i != block_length + header_length:
                    drol_iter.next()
                    i = i + 1
            except StopIteration:
                pass
            except IndexError:
                pass
        elif char == "w" or char == "'": # While loop
            try:
                compare_op = drol_string[location + 1] + drol_string[location + 2]
                if compare_op == "==" or compare_op == "!=" or compare_op == ">=" or compare_op == "<=":
                    pass
                elif compare_op == ">>":
                    compare_op = ">"
                elif compare_op == "<<":
                    compare_op = "<"
                else:
                    exit("drol.py: LoopError: invalid comparison operator")
                if header == 1:
                    outfile.write('while (regone ' + compare_op + ' regtwo) {\n')
                else:
                    code = code + 'while (regone ' + compare_op + ' regtwo) {\n'
                if char == "w": # Standard header length
                    block_length = drol_string[location + 3] + drol_string[location + 4] + drol_string[location + 5] + drol_string[location + 6]
                    header_length = 6
                elif char == "'":
                    block_length = drol_string[location + 3] + drol_string[location + 4] + drol_string[location + 5] + drol_string[location + 6] + drol_string[location + 7] + drol_string[location + 8] + drol_string[location + 9] + drol_string[location + 10]
                    header_length = 10                    
                if block_length.isdigit() == False:
                    exit("drol.py: LoopError: missing loop length declaration")
                block_length = int(block_length)
                i = 0
                j = 1
                mini_block = ""
                while i != block_length:
                    mini_block = mini_block + drol_string[location + j + header_length]
                    i = i + 1
                    j = j + 1
                if header == 1:
                    outfile.write(compile(mini_block, outfile, 0))
                    outfile.write('}\n')
                else:
                    code = code + compile(mini_block, outfile, 0)
                    code = code + '}\n'
                location = location + block_length + header_length + 1
                i = 0
                while i != block_length + header_length:
                    drol_iter.next()
                    i = i + 1
            except StopIteration:
                pass
            except IndexError:
                pass
        elif char == ":" or char == "(": # Subroutine declaration
            try:
                if char == ":":
                    block_length = drol_string[location + 1] + drol_string[location + 2] + drol_string[location + 3] + drol_string[location + 4]
                    header_length = 8
                elif char == "(":
                    block_length = drol_string[location + 1] + drol_string[location + 2] + drol_string[location + 3] + drol_string[location + 4] + drol_string[location + 5] + drol_string[location + 6] + drol_string[location + 7] + drol_string[location + 8]
                    header_length = 16
                if block_length.isdigit() == False:
                    print block_length
                    exit("drol.py: SubroutineError: missing function length declaration")
                block_length = int(block_length)
                if char == ":":
                    subroutine_name = drol_string[location + 5] + drol_string[location + 6] + drol_string[location + 7] + drol_string[location + 8]
                elif char == "(":
                    subroutine_name = drol_string[location + 9] + drol_string[location + 10] + drol_string[location + 11] + drol_string[location + 12] + drol_string[location + 13] + drol_string[location + 14] + drol_string[location + 15] + drol_string[location + 16]
                if header == 1:
                    outfile.write('void ' + subroutine_name + '(void) {\n')
                else:
                    code = code + 'void ' + subroutine_name + '(void) {\n'
                i = 0
                j = 1
                mini_block = ""
                while i != block_length:
                    mini_block = mini_block + drol_string[location + j + header_length]
                    i = i + 1
                    j = j + 1
                if header == 1:
                    outfile.write(compile(mini_block, outfile, 0))
                    outfile.write('}\n')
                else:
                    code = code + compile(mini_block, outfile, 0)
                    code = code + '}\n'
                location = location + block_length + header_length + 1
                i = 0
                while i != block_length + header_length:
                    drol_iter.next()
                    i = i + 1
            except StopIteration:
                pass
            except IndexError:
                pass
        elif char == ";" or char == ")": # Subroutine call
            try:
                if char == ";":
                    subroutine_name = drol_string[location + 1] + drol_string[location + 2] + drol_string[location + 3] + drol_string[location + 4]
                    header_length = 4
                elif char == ")":
                    subroutine_name = drol_string[location + 1] + drol_string[location + 2] + drol_string[location + 3] + drol_string[location + 4] + drol_string[location + 5] + drol_string[location + 6] + drol_string[location + 7] + drol_string[location + 8]
                    header_length = 8
                if header == 1:
                    outfile.write(subroutine_name + '();\n')
                else:
                    code = code + subroutine_name + '();\n'
                location = location + header_length + 1
                i = 0
                while i != header_length:
                    drol_iter.next()
                    i = i + 1
            except StopIteration:
                pass
            except IndexError:
                pass
        elif char == "@" or char == "#": # Forever loop (loops forever without any conditional statement)
            try:
                if char == "@":
                    block_length = drol_string[location + 1] + drol_string[location + 2] + drol_string[location + 3] + drol_string[location + 4]
                    header_length = 4
                elif char == "#":
                    block_length = drol_string[location + 1] + drol_string[location + 2] + drol_string[location + 3] + drol_string[location + 4] + drol_string[location + 5] + drol_string[location + 6] + drol_string[location + 7] + drol_string[location + 8]
                    header_length = 8
                if block_length.isdigit() == False:
                    exit("drol.py: LoopError: missing loop length declaration")
                block_length = int(block_length)
                if header == 1:
                    outfile.write('while (1) {\n')
                else:
                    code = code + 'while (1) {\n'
                mini_block = ""
                i = 0
                j = 1
                while i != block_length:
                    mini_block = mini_block + drol_string[location + j + header_length]
                    i = i + 1
                    j = j + 1
                if header == 1:
                    outfile.write(compile(mini_block, outfile, 0))
                    outfile.write('}\n')
                else:
                    code = code + compile(mini_block, outfile, 0)
                    code = code + '}\n'
                location = location + block_length + header_length + 1
                i = 0
                while i != block_length + header_length:
                    drol_iter.next()
                    i = i + 1
            except StopIteration:
                pass
            except IndexError:
                pass
        else:
            if header == 1:
                outfile.write(lookup(char))
            else:
                code = code + lookup(char)
            location = location + 1
    if header == 1:
        outfile.write(end)
    else:
        return code

def main(argnum = 1):
    try:
        inptfile = open(argv[argnum], "r")
    except IOError:
        exit("File error: File does not exist")
    try:
        outfile = open("a.c", "w")
    except IOError:
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
       exit("Error: invalid flag")
else:
    exit("Error: No input files present")

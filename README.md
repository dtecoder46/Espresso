
# Espresso

A stronger cup of Java

## Why Espresso?
1. Debugging little semicolon errors consumes time that could've been spent on testing code that actually matters
2. It's faster than Java

## How to Run

- All
    1. Install Java (https://dev.java/download/)
    2. Install Clang (https://clang.llvm.org/get_started.html)
        - Alternatively, type clang in the command line and type "y" when it prompts you to install it
- New Java project
    1. Clone the repo
- Existing Java project
    1. Download the compiler file
    2. Change .java files to .esp
    3. Remove any semicolons in the code
    4. Run the compiler file
        1. clang compiler.c
        2. ./a.out
    5. The output is in output.c

## Algorithm

1. File format: .esp
2. Compiler (C)
    1. Read the .esp file
    2. Split the .esp code by spaces into a list of tokens
    3. Translation
        1. Create a dictionary of Java keywords and their C equivalents
        2. Loop over the list of Java tokens and add their C equivalents to a string
    4. Put the C string into output.c

## Sources

w3Schools C: https://www.w3schools.com/c/index.php

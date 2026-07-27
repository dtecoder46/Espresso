
# Espresso

A stronger cup of Java

## Why Espresso?
1. Debugging little semicolon errors consumes time that could've been spent on testing code that actually matters


## How to Run

- All
    1. Install Python (https://www.python.org/downloads/)
    2. Install Go (https://go.dev/dl/)
- New Java project
    1. Clone the repo
- Existing Java project
    1. Download the compiler file
    2. Change .java files to .esp
    3. Remove any semicolons in the code
    4. Run the compiler file
        1. python3 compiler.py
    5. The output is in output.go

## Algorithm

1. File format: .esp
2. Compiler (Python)
    1. Read the .esp file
    2. Split the .esp code by spaces into a list of tokens
    3. Translation
        1. Create a dictionary of Java keywords and their Go equivalents
        2. Loop over the list of Java tokens and add their Go equivalents to a string
    4. Put the Go string into output.go

## Credits/Sources

Python tutorial - https://www.w3schools.com/python/default.asp

Go tutorial - https://www.w3schools.com/go/index.php

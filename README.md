
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

## Usage note

To make translating Java/.esp tokens into Go easier, please add a space between the function/method name and the parentheses for all your functions/methods

## Algorithm

- File format: .esp
- Compiler (Python)
    - Read the .esp file
    - Create an array of lines by splitting on newline
    - Preprocessing
        - Remove the first and last lines of the .esp file, since a main class is not required in Go
        - Loop over the lines
            - Replace “public static" with "func"
            - Remove one level of tabs (since the outer level main class has been removed)
    - Parsing
        - Loop over the list of lines
            - Split each line by spaces into a list of tokens
            - If the first token in the list is “func”
                - Take the second token (function type) and push it up by four indices
            - Other modifications
                - Parameters: ensure anything within the parentheses is concatenated
            - Put the line list into an outer list
    - Translate to Go
        - Create a dictionary of Java tokens and their Go equivalents
        - Loop over each line
            - Loop over the list of Java tokens
                - Call their Go equivalents and add them to a Go string
                - Write the Go string into output.go

## Credits/Sources

Python tutorial - https://www.w3schools.com/python/default.asp

Go tutorial - https://www.w3schools.com/go/index.php

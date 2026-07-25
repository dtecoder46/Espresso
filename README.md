
# Espresso

A stronger cup of Java

## Why Espresso?
1. Debugging little semicolon errors consumes time that could've been spent on testing code that actually matters
2. It's faster than Java

## How to Run

- All
    1. Install Java (https://dev.java/download/)
    2. Install Zig (https://ziglang.org/learn/getting-started/#managers)
- New Java project
    1. Clone the repo
- Existing Java project
    1. Download the compiler file
    2. Change .java files to .esp
    3. Remove any semicolons in the code
    4. Run the compiler file: java Compiler.zig
    5. The output is in output.zig

## Algorithm

1. File format: .esp
2. Compiler (Zig)
    1. Read the .esp file
    2. Split the .esp code by spaces into a list of tokens
    3. Translation
        1. Create a dictionary of Java keywords and their Zig equivalents
        2. Loop over the list of Java tokens and add their Zig equivalents to a string
    4. Put the Zig string into output.zig

## Sources


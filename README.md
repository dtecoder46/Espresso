# Java: No Semicolons

A variant of Java without those annoying semicolons

## How to install/run

- New Java project
    1. Clone the repo
- Existing Java project
    1. Download the compiler file
    2. Change .java files to .jnsc
    3. Remove any semicolons in the code
    4. Run the compiler file: java output.java

## Algorithm

1. File format: .jnsc
2. Compiler (Java)
    1. Split the code line by line into an array
    2. Loop over the array of lines
        1. If a line contains } but has a numerical digit after it, add a semicolon (array)
        2. Otherwise, if a line contains //, whitespace, or }, skip over it
        3. Otherwise append a semicolon at the end of the line and put it back into the array of lines
        4. Add \n at the end of each line
    3. Concatenate all lines in the array
    4. Put the combined code into [original .jnsc file name].java

## Sources

Semicolon placement guidelines/Java coding guide: https://www.w3schools.com/java/default.asp

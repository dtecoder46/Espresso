# Espresso

A stronger cup of Java, without any semicolons to water it down

## How to install/run

- New Java project
    1. Clone the repo
- Existing Java project
    1. Download the compiler file
    2. Change .java files to .esp
    3. Remove any semicolons in the code
    4. Run the compiler file: java Compiler.java
    5. The output is in output.java

## Algorithm

1. File format: .esp
2. Compiler (Java)
    1. Read the .esp file
    2. Split the code line by line into an array
    3. Take the first line of the array, replace the original class name with Output
    4. Loop over the array of lines
        1. If a line contains } but has a numerical digit after it, add a semicolon (array)
        2. Otherwise, if a line contains //, whitespace, or }, skip over it
        3. Otherwise append a semicolon at the end of the line and put it back into the array of lines
        4. Add \n at the end of each line
    5. Concatenate all lines in the array
    6. Put the combined code into Output.java

## Sources

Semicolon placement guidelines/Java coding guide: https://www.w3schools.com/java/default.asp

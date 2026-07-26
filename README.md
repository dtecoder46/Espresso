
# Espresso

A stronger cup of Java

## Why Espresso?
1. Debugging little semicolon errors consumes time that could've been spent on testing code that actually matters


## How to Run

- All
    1. Install Lua (https://www.lua.org/download.html)
        - Alternatively, type "lua" in the command line and type "y" when it prompts you to install it
- New Java project
    1. Clone the repo
- Existing Java project
    1. Download the compiler file
    2. Change .java files to .esp
    3. Remove any semicolons in the code
    4. Run the compiler file
        1. lua compiler.lua
    5. The output is in output.lua

## Algorithm

1. File format: .esp
2. Compiler (Lua)
    1. Read the .esp file
    2. Split the .esp code by spaces into a list of tokens
    3. Translation
        1. Create a dictionary of Java keywords and their Lua equivalents
        2. Loop over the list of Java tokens and add their Lua equivalents to a string
    4. Put the Lua string into output.lua

## Credits/Sources

Powered by Lua - https://www.lua.org/

Lua manual - https://www.lua.org/manual/5.5/

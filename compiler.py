"""
Name: file_read()
Purpose: Reads the .esp file
Parameters: none
Return: espresso_string - the file contents 
"""

def file_read():
	
	espresso_file = open("Main.esp", "r")

	espresso_string = espresso_file.read()

	espresso_file.close()

	return espresso_string

espresso_string = file_read()

espresso_lines = espresso_string.splitlines()

print(espresso_lines)

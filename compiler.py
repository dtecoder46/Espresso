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

"""
Name: preprocess()
Purpose: to remove any unnecessary code lines and characters
Parameters: code_lines - the array of lines of code to process
Return: new_code_lines - the processed array of code lines
"""

def preprocess(code_lines):
	# removes the first and last lines of code since Go does not require a main class

	code_lines.pop(0)
	code_lines.pop()
	
	line_index = 0

	while line_index < len(code_lines):
		code_lines[line_index] = code_lines[line_index].replace("\t", "", 1)
		line_index += 1

	return code_lines

espresso_string = file_read()

# Break the .esp code into an array of lines

espresso_lines = espresso_string.splitlines()

# Preprocess

espresso_lines = preprocess(espresso_lines)

print(espresso_lines)

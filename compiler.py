"""
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
		code_lines[line_index] = code_lines[line_index].replace("public static", "func") # simplifies parsing later on
		line_index += 1

	return code_lines

"""
Name: parser()
Purpose: to break down a list of code lines into a 2D array of tokens
Parameters: lines_list - the list of code lines
Return: tokens - the 2D array of tokens
"""

def parser(lines_list):
	tokens = []
	
	for line in lines_list:
		line_tokens = line.split(" ")

		if line_tokens[0] == "func":
			line_tokens.insert(5, line_tokens[1])
			line_tokens.pop(1)		
		
		for token_index in range(len(line_tokens) - 1):

			# Checks for two consecutive tokens containing matching parentheses
			if line_tokens[token_index].find("(") != -1 and line_tokens[token_index + 1].find(")") != -1: 

				line_tokens[token_index] = line_tokens[token_index] + " " + line_tokens[token_index + 1] 
				# Merge the tokens into the first token's slot
				
				line_tokens.pop(token_index + 1) # Remove the previous slot of the other token

		tokens.append(line_tokens)
	
	return tokens

espresso_string = file_read()

# Break the .esp code into an array of lines

espresso_lines = espresso_string.splitlines()

# Preprocess

espresso_lines = preprocess(espresso_lines)

# Parse

tokens = parser(espresso_lines)
print(tokens)

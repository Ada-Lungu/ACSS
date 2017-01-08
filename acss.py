
import sys

value_of_variable = {}
file = open(sys.argv[1])

for line in file:
	words_in_line = line.split(" ")

	if words_in_line[0] == "var":
		var_name = words_in_line[1]
		var_value = words_in_line[3]
		value_of_variable[var_name] = var_value
	else:

		for word in words_in_line:
			if word[0]=='~':
				print value_of_variable[word] + " ",
			else:
				print word + " ",
		print " "
















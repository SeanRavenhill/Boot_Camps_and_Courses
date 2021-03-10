def arithmetic_arranger(problems, solved=False):
  
  # Creates empty variables as lists to store the function parameter (problems) operators and operands. 
  first_operand = []
  second_operand = []
  operators = []

  # Splits the string from function parameter (problems), catergorises them and appends to the empty variables lists.
  for probs in problems:
    separate = probs.split()
    first_operand.append(separate[0])
    operators.append(separate[1])
    second_operand.append(separate[2])

  ############################################################
  ####################   LOGIC TEST #1   #####################
  ############################################################

  # Creates Boolean to test if there are multiplication or division symbols in the operators.
  operators_verify = False

  # Creates list variable with multiplication and division operator symbols.
  operators_check = ["*", "/"]

  # Loops though (operators_check) & (operators) variables independant of each other, checks for any matches between both. 
  for x, y in ((a, b) for a in operators_check for b in operators):
    if x in y:
      operators_verify = True
      
  ############################################################
  ####################   LOGIC TEST #2   #####################
  ############################################################
  
  # Creates Boolean to test if there are non-numeral characters in the operands.
  chars_test = False

  # Combines first_operand list and second_operand list into one list.
  operands = first_operand + second_operand

  # Creates a string of the alphabet in upper and lowercase characters.
  import string
  chars = string.ascii_letters

  # Loops though (operands) & (chars) variables independant of each other, checks for any matches between both.
  for x, y in ((a, b) for a in operands for b in chars):
    if y in x:
      chars_test = True

  ############################################################
  ####################   LOGIC TEST #3   #####################
  ############################################################
  
  # Creates Boolean to test if there over 4 numeral characters in the operands.
  len_test = False

  # Recyles (operands) list variable created in LOGIC TEST #2. 
  # Checks if numeral characters exceed the limit of 5 for each item in the list.
  for x in operands:
    if len(x) > 4:
      len_test = True
  
  ############################################################
  #################   ERROR TESTING BLOCK   ##################
  ############################################################

  # First statement runs logic to test if there are too many problems.
  # Returns error message string if True.
  if len(problems) > 5:
    return "Error: Too many problems."

  # Second statement checks the result of the LOGIC TEST #1.
  # Returns error message string if True.
  if operators_verify == True:
    return "Error: Operator must be '+' or '-'."

  # Third statement checks the result of the LOGIC TEST #2.
  # Returns error message string if True.
  if chars_test == True :
    return "Error: Numbers must only contain digits."

  # Forth statement checks the result of the LOGIC TEST #3.
  # Returns error message string if True.
  if len_test == True :
    return "Error: Numbers cannot be more than four digits."

  # Returns the (print_arrangement) function below and provides the required parameters from this (arithmetic_arranger)
  # functions outputs. Carries over optional variable (sovled).
  return print_arrangement(first_operand, second_operand, operators, solved)

############################################################
###   FUNCTION TO RETURN STRING OF ARTHIMETIC FORMULAS   ###
############################################################

# Function used to seperate into modules, one function to handle the extraction and computaion of information from the 
# paramaters passed into (arithmetic_arranger) and the (print_arrangement) to render the output to a string that 
# answers the requirements of the prohect brief. This will help to maintian good practice in regards to cyclomatic complexity of program.

def print_arrangement(first_operand, second_operand, operators, solved):

  # Creates a set of empty list varibles in which to store the data that will be used to create the strings.
  # Naming conventions of the lists are self explanatory in accordance the brief requirements.
  prob_dash_line = []

  prob_solved = []

  four_empty_char_list = []

  first_line_indents = []

  second_line_indents = []

  fourth_line_indents = []

  # Creats a zip object that can be iterated through using a tuple of same amount of items in the zip object.
  operands_zip = zip(first_operand, second_operand, operators)

  # Imports the Operator module so that the arithmetic symbols that are currently strings in the 
  # operater list varible can be used as actual mathematical operators.
  import operator
  ops = {"+":operator.add, "-":operator.sub}

  # For loop with a tuple of 3 variables, that will iterate through the zip object made at varible (operands_zip).
  for x, y, z in operands_zip:
    # Creates a string varibale with each iteration loop that determines dashed line length for each arithmetic formula. Appends to list (prob_dash_line).
    prob_dash_line.append("-" * ((max(len(x), len(y))) + len("  ")))
    # The Operator module takes the (operator)/(z) input as a string and computes the sum of the (operands)/(x, y). Appends to list (prob_solved).
    prob_solved.append(str(ops[z](int(x), int(y))))
    # Determines the indents from left (or the margin). Appends to list(first_line_indents)
    first_line_indents.append(" " * ((max(len(x), len(y)) + 2) - (len(x))))
    # Determines the indents from left (or the margin), including the (operator)/(z). Appends to list (second_line_indents).
    second_line_indents.append(" " * ((max(len(x), len(y)) + 2) - ((len(y)) + 1)))
    # As required by the brief. All formulas require a space of 4 empty spaces. Appends strings of 4 blank spaces to list (fourth_line_empty_chars).
    four_empty_char_list.append('    ')

  # Remove the last blank character string from the list (four_empty_char_list)
  four_empty_char_list.pop(-1)

  ############################################################
  ###############   FIRST LINE STRING LOGIC   ################
  ############################################################

  # Creates a list of None values to act as place holders for building a new list (first_line_list).  
  first_line_list = [None] * (len(first_line_indents) + len(first_operand) + len(four_empty_char_list))
  # Uses list slicing and the step parameters to place the elements of the lists (first_line_indents, first_operand, four_empty_char_list).
  # into the list (first_line_list).
  first_line_list[::3] = first_line_indents
  first_line_list[1::3] = first_operand
  first_line_list[2::3] = four_empty_char_list

  # Uses the .join() method to create a string from the (first_line_list) list.
  first_line_string = ''.join(first_line_list)

  ############################################################
  ###############   SECOND LINE STRING LOGIC   ###############
  ############################################################

  # Creates a list of None values to act as place holders for building a new list (second_line_list).
  second_line_list = [None] * (len(operators) + len(second_line_indents) + len(second_operand) + len(four_empty_char_list))
  
  # Uses list slicing and the step parameters to place the elements of the lists (operators, second_line_indents ,second_operand, four_empty_char_list).
  # into the list (first_line_list)
  second_line_list[::4] = operators
  second_line_list[1::4] = second_line_indents
  second_line_list[2::4] = second_operand
  second_line_list[3::4] = four_empty_char_list

  # Uses the .join() method to create a string from the (second_line_list) list.
  second_line_string = ''.join(second_line_list)

  ############################################################
  ###############   THIRD LINE STRING LOGIC   ################
  ############################################################

  # Creates a list of None values to act as place holders for building a new list (second_line_list).
  third_line_list = [None] * (len(prob_dash_line) + len(four_empty_char_list))

  # Uses list slicing and the step parameters to place the elements of the lists (prob_dash_line, four_empty_char_list).
  # into the list (third_line_list)  
  third_line_list[::2] = prob_dash_line
  third_line_list[1::2] = four_empty_char_list

  # Uses the .join() method to create a string from the (third_line_list) list.
  third_line_string = ''.join(third_line_list)

  ############################################################
  ###############   FORTH LINE STRING LOGIC   ################
  ############################################################

  # Creats a zip object that can be iterated through using a tuple of same amount of items in the zip object.
  probs_zip = zip(prob_dash_line, prob_solved)

  # Determines the indents from left (or the margin). Appends to list (fourth_line_indents).
  for x, y in probs_zip:
    fourth_line_indents.append(" " * (len(x) - len(y)))

  # Uses list slicing and the step parameters to place the elements of the lists (prob_dash_line, four_empty_char_list).
  # into the list (fourth_line_list) 
  fourth_line_list = [None] * (len(fourth_line_indents) + len(prob_solved) + len(four_empty_char_list))
  fourth_line_list[::3] = fourth_line_indents
  fourth_line_list[1::3] = prob_solved
  fourth_line_list[2::3] = four_empty_char_list

  # Uses the .join() method to create a string from the (fourth_line_list) list.
  fourth_line_string = ''.join(fourth_line_list)

  # Creates if else block to create and return two iterations of the (arranged_problems) strings using string concatenation.
  # Takes the optional function parameter (solved) from the (arithmetic_arranger) function and uses 
  # the (solved) variable created in that function and returned to this functions parameters to return
  # what that Boolean is stated as.
  if solved == True:
    arranged_problems = first_line_string + '\n' + second_line_string + '\n' + third_line_string + '\n' + fourth_line_string
  else:
    arranged_problems = first_line_string + '\n' + second_line_string + '\n' + third_line_string

  return arranged_problems
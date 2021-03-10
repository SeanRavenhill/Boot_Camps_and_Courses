def arithmetic_arranger(problems, solved=False):

  first_operand = []
  second_operand = []
  operators = []

  for probs in problems:
    separate = probs.split()
    first_operand.append(separate[0])
    operators.append(separate[1])
    second_operand.append(separate[2])

  operators_verify = False

  operators_check = ["*", "/"]

  for x, y in ((a, b) for a in operators_check for b in operators):
    if x in y:
      operators_verify = True

  chars_test = False

  operands = first_operand + second_operand

  import string
  chars = string.ascii_letters

  for x, y in ((a, b) for a in operands for b in chars):
    if y in x:
      chars_test = True

  len_test = False

  for x in operands:
    if len(x) > 4:
      len_test = True
  
  if len(problems) > 5:
    return "Error: Too many problems."

  if operators_verify == True:
    return "Error: Operator must be '+' or '-'."

  if chars_test == True :
    return "Error: Numbers must only contain digits."

  if len_test == True :
    return "Error: Numbers cannot be more than four digits."

  return arrangements_lists(first_operand, second_operand, operators, solved)

def arrangements_lists(first_operand, second_operand, operators, solved):

  prob_dash_line = []
  prob_solved = []
  first_line_indents = []
  second_line_indents = []
  fourth_line_indents = []

  import operator
  ops = {"+":operator.add, "-":operator.sub}

  prob_zip = zip(first_operand, second_operand, operators)
  
  for x, y, z in prob_zip:
    prob_dash_line.append("-" * ((max(len(x),len(y)))+2))
    prob_solved.append(str(ops[z](int(x), int(y))))
    first_line_indents.append(" " * ((max(len(x),len(y)))+2 - len(x)))
    second_line_indents.append(" " * ((max(len(x),len(y)))+2 - len(y) - 1))
    fourth_line_indents.append(" " * ((max(len(x),len(y)))+2 - (len(str(ops[z](int(x), int(y)))))))
  
  return print_formula(first_operand, second_operand, operators, prob_dash_line, prob_solved, first_line_indents, second_line_indents, fourth_line_indents, solved)

def print_formula(first_operand, second_operand, operators, prob_dash_line, prob_solved, first_line_indents, second_line_indents, fourth_line_indents, solved):

  formula_string = ""

  for i in range(len(first_operand)):
    formula_string += first_line_indents[i]
    formula_string += first_operand[i] + "    " 
  formula_string = formula_string[:-4] + "\n"

  for i in range(len(second_operand)):
    formula_string += operators[i] + second_line_indents[i] + second_operand[i] + "    "
  formula_string = formula_string[:-4] + "\n"

  for i in range(len(prob_dash_line)):
    formula_string += prob_dash_line[i] + "    "
  formula_string = formula_string[:-4]

  solution_string = ""

  for i in range(len(prob_solved)):
    solution_string += fourth_line_indents[i] + prob_solved[i] + "    "
  solution_string = solution_string[:-4]

  if solved == True:
    return formula_string + "\n" +solution_string
  else:
    return formula_string
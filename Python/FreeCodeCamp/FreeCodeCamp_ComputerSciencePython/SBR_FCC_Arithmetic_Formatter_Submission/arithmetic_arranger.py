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

  return print_arrangement(first_operand, second_operand, operators, solved)

def print_arrangement(first_operand, second_operand, operators, solved):

  prob_dash_line = []
  prob_solved = []
  four_empty_char_list = []
  first_line_indents = []
  second_line_indents = []
  fourth_line_indents = []

  operands_zip = zip(first_operand, second_operand, operators)

  import operator
  ops = {"+":operator.add, "-":operator.sub}

  for x, y, z in operands_zip:
    prob_dash_line.append("-" * ((max(len(x), len(y))) + len("  ")))
    prob_solved.append(str(ops[z](int(x), int(y))))
    first_line_indents.append(" " * ((max(len(x), len(y)) + 2) - (len(x))))
    second_line_indents.append(" " * ((max(len(x), len(y)) + 2) - ((len(y)) + 1)))
    four_empty_char_list.append('    ')

  four_empty_char_list.pop(-1)
 
  first_line_list = [None] * (len(first_line_indents) + len(first_operand) + len(four_empty_char_list))
  first_line_list[::3] = first_line_indents
  first_line_list[1::3] = first_operand
  first_line_list[2::3] = four_empty_char_list

  first_line_string = ''.join(first_line_list)

  second_line_list = [None] * (len(operators) + len(second_line_indents) + len(second_operand) + len(four_empty_char_list))
  second_line_list[::4] = operators
  second_line_list[1::4] = second_line_indents
  second_line_list[2::4] = second_operand
  second_line_list[3::4] = four_empty_char_list

  second_line_string = ''.join(second_line_list)

  third_line_list = [None] * (len(prob_dash_line) + len(four_empty_char_list))
  third_line_list[::2] = prob_dash_line
  third_line_list[1::2] = four_empty_char_list

  third_line_string = ''.join(third_line_list)

  probs_zip = zip(prob_dash_line, prob_solved)

  for x, y in probs_zip:
    fourth_line_indents.append(" " * (len(x) - len(y)))

  fourth_line_list = [None] * (len(fourth_line_indents) + len(prob_solved) + len(four_empty_char_list))
  fourth_line_list[::3] = fourth_line_indents
  fourth_line_list[1::3] = prob_solved
  fourth_line_list[2::3] = four_empty_char_list

  fourth_line_string = ''.join(fourth_line_list)

  if solved == True:
    arranged_problems = first_line_string + '\n' + second_line_string + '\n' + third_line_string + '\n' + fourth_line_string
  else:
    arranged_problems = first_line_string + '\n' + second_line_string + '\n' + third_line_string

  return arranged_problems
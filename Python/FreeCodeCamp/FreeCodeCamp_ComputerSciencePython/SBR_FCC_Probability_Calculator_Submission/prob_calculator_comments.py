import copy
import random

# Instantiates class
class Hat:
  # Instantiate an object of the class with a **kwargs or key words argument parameter.
  def __init__(self, **ball):

    # Empty list and dictionay variables to for loops store output data.
    self.contents = []
    self.dict = {}

    # Takes the ball object created iterates through a for loop with a key and value from the .items() function.
    for ball_colour, ball_amount in ball.items():
      # Loops through each item in the object.
      for ball in range(ball_amount):
        # Will append the string (ball_colour) to the (self.contents) list for as many instances of the (ball_amount).
        self.contents.append(ball_colour)
        # Will append to and update the (self.dict) dictionary for each instance of the loop.
        self.dict.update({ball_colour : ball_amount})

  # Creates a class method (draw) with parameter (remove)
  def draw(self, remove):
    # If the remove parameter is greater than the amount of items in the (self.contents) list. Will reset the (self.contents) list. 
    if remove > len(self.contents):
      return self.contents
    
    balls_drawn = []
    
    # If the remove parameter is equal to or less than. For loop will interate the range of the remove parameter provided.
    for i in range(remove):
      # Uses the imported random library to select at random an item from the (self.contents) list.
      ball_drawn = random.choice(self.contents)
      # Appends that item to the empty (balls_drawn) list variable above.
      balls_drawn.append(ball_drawn)
      # Will then remove that item from the self.contents) list so it can not be drawn again.
      self.contents.pop(self.contents.index(ball_drawn))

    return balls_drawn

  ############################################################
  #######   BONUS CODE FOR MORE INFORMATIVE RENDER #1  #######        
  ############################################################
  
  def __str__(self):

    dict_content_list = []
    dict_content_output = []
    dict_content_string = ""

    # Appends the amount of balls and their colour to the empty (dict_content_list) list variable.
    for key, value in self.dict.items():
      dict_content_list.append(str(value) +  " " + str(key))

    # Appends all the items expect the last item in the list. Also used for grammar. ie. 1 red ball, 2 yellow balls.
    for x in dict_content_list[0:-1:]:
      if x[0] != "1":
        dict_content_output.append(x + " balls")
      else:
        dict_content_output.append(x + " ball")
    
    # Appends last item in the list. Also used for grammar. ie. 1 red ball, 2 yellow balls.
    for x in dict_content_list[-1::]:
      if x[0] != "1":
        dict_content_output.append(x + " balls")
      else:
        dict_content_output.append(x + " ball")

    # Adds the first items from (dict_content_output) list as a string.
    for x in dict_content_output[0:1:]:
      dict_content_string += x

    # Adds the first through to second last items from (dict_content_output) list as a string.
    for x in dict_content_output[1:-1:]:
      dict_content_string += ', ' + ''.join(x)

    # Adds last item in the (dict_content_output) list as a string.
    for x in dict_content_output[-1::]:
      dict_content_string += ' and ' + ''.join(x)
    
    # Returns the full string in a informative manner.
    return "If a hat contains: " + dict_content_string + ".\n"

# Creats a function to calculate and render the probibilty outcome.
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

  match_count = 0
  
  # Iterates throuhg this loop for the range of the (num_experiments) parameter.
  # If True makes a deep copy object created in the class above.
  # Runs the class method (drawn) with the (num_balls_drawn) parameter on this copy of the object. Original object remains unchanged.
  for i in range(num_experiments):
    match_found = True
    hat_copy = copy.deepcopy(hat)
    drawn = hat_copy.draw(num_balls_drawn)
    
    # If the key from (expected_balls) paramter does not match any of the keys now in the (balls_drawn) list
    # created when the class method (drawn) was called. Or if there is a match, but the amount is not a match.
    # Changes the (match_found) Boolean variable to False and breaks out of the loop allowing the loop to run again.
    for key, value in expected_balls.items():
      if key not in drawn or expected_balls[key] > drawn.count(key):
        match_found = False
        break
    
    # If a match is found (match_found) Boolean varible changes back to a True value and a count is added to the 0 value (match_count) variable.
    while match_found == True:
      match_found = True
      match_count += 1
      break

  # Returns the probiblity as a float.
  return match_count/num_experiments

############################################################
#######   BONUS CODE FOR MORE INFORMATIVE RENDER #2  #######        
############################################################

# Uses the same logic as BONUS CODE #1. Please reference BONUS CODE #1 comments.
def eb_string(expected_balls):
  expected_balls_list = []
  expected_balls_output = []
  expected_balls_string = ""

  for key, value in expected_balls.items():
    expected_balls_list.append(str(value) +  " " + str(key))
  
  for x in expected_balls_list[0:-1:]:
    if x[0] != "1":
      expected_balls_output.append(x + " balls")
    else:
      expected_balls_output.append(x + " ball")

  for x in expected_balls_list[-1::]:
    if x[0] != "1":
      expected_balls_output.append(x + " balls")
    else:
      expected_balls_output.append(x + " ball")

  for x in expected_balls_output[0:1:]:
    expected_balls_string += x

  for x in expected_balls_output[1:-1:]:
    expected_balls_string += ', ' + ''.join(x)

  for x in expected_balls_output[-1::]:
    expected_balls_string += ' and ' + ''.join(x)
  
  return print("What is the probibilty of drawing " + expected_balls_string + "?" + "\n")

############################################################
#######   BONUS CODE FOR MORE INFORMATIVE RENDER #3  #######        
############################################################

# Uses the same logic as BONUS CODE #1. Please reference BONUS CODE #1 comments.
def draw_and_experi_string(num_balls_drawn, num_experiments):
  
  draw_and_experi_string = ""

  if str(num_balls_drawn) != "1":
      draw_and_experi_string += str(num_balls_drawn) + " balls are drawn and "
  else:
    draw_and_experi_string += str(num_balls_drawn) + " ball is drawn and "
  
  if str(num_experiments) != "1":
    draw_and_experi_string += str(num_experiments) + " experiments are run?"
  else:
    draw_and_experi_string += str(num_experiments) + " experiment is run?"
 
  return print("If " + draw_and_experi_string + "\n")
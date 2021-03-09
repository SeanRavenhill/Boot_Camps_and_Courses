import copy
import random

class Hat:
  def __init__(self, **ball):

    self.contents = []
    self.dict = {}

    for ball_colour, ball_amount in ball.items():
      for ball in range(ball_amount):
        self.contents.append(ball_colour)
        self.dict.update({ball_colour : ball_amount})

  def draw(self, remove):
    if remove > len(self.contents):
      return self.contents
    
    balls_drawn = []

    for i in range(remove):
      ball_drawn = random.choice(self.contents)
      balls_drawn.append(ball_drawn)
      self.contents.pop(self.contents.index(ball_drawn))

    return balls_drawn
  
  def __str__(self):

    dict_content_list = []
    dict_content_output = []
    dict_content_string = ""

    for key, value in self.dict.items():
      dict_content_list.append(str(value) +  " " + str(key))

    for x in dict_content_list[0:-1:]:
      if x[0] != "1":
        dict_content_output.append(x + " balls")
      else:
        dict_content_output.append(x + " ball")

    for x in dict_content_list[-1::]:
      if x[0] != "1":
        dict_content_output.append(x + " balls")
      else:
        dict_content_output.append(x + " ball")

    for x in dict_content_output[0:1:]:
      dict_content_string += x

    for x in dict_content_output[1:-1:]:
      dict_content_string += ', ' + ''.join(x)

    for x in dict_content_output[-1::]:
      dict_content_string += ' and ' + ''.join(x)

    return "If a hat contains: " + dict_content_string + ".\n"

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

  match_count = 0

  for i in range(num_experiments):
    match_found = True
    hat_copy = copy.deepcopy(hat)
    drawn = hat_copy.draw(num_balls_drawn)

    for key, value in expected_balls.items():
      if key not in drawn or expected_balls[key] > drawn.count(key):
        match_found = False
        break

    while match_found == True:
      match_found = True
      match_count += 1
      break

  return match_count/num_experiments

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
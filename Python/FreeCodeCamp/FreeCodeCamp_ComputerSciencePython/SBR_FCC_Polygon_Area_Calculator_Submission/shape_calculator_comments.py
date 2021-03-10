class Rectangle:

  # Instantiate an object of the class.
  def __init__(self, width, height):
    # Sets the width and height variables based on the parameter inputs.
    self.width = width
    self.height = height

  # Creates class method to change width value.
  def set_width(self, width):
    self.width = width

  # Creates class method to change height value.
  def set_height(self, height):
    self.height = height

  # Creates class method that returns the area value.
  def get_area(self):
    area = self.width * self.height
    return area

  # Creates class method that returns the perimeter value.
  def get_perimeter(self):
    perimeter = 2 * self.width + 2 * self.height
    return perimeter

  # Creates class method that returns the diagonal value.
  def get_diagonal(self):
    diagonal = (self.width ** 2 + self.height ** 2) ** .5
    return diagonal
  
  # Creates class method that returns the objects shape, printed in strings of * characters.
  def get_picture(self):
    # Checks to see if the width or height values are greater than the nurmeric value of 50.
    # Returns a string if either are true.
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    # Else takes the width value and creates a string of that many * characters long with a break line.
    # And duplicates that line by the value of the height variable.
    # Return the output string variable.
    else:
      horizontal = "*" * self.width + "\n"
      output = horizontal * self.height
      return output

  # Creates class method that returns the perimeter value.
  def get_amount_inside(self, shape):
    return self.get_area()//shape.get_area()

  # Returns a string describing the values of the polygon if a print(object) ie. print(rect) is called.
  def __str__(self):
    output = "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"
    return output
    
# Instantiates and new class that will inherit the class methods from the Rectangle class.
class Square(Rectangle):

  # Instantiate an object of the class.
  def __init__(self, side):
    # Sets the width and height variables based on the parameter input.
    # In this case with a sqaure only one paramenter (side) is required and can be applied to both variables.
    self.width = side
    self.height = side
  
  # Creates class method to change side value. And apply that to both variables.
  def set_side(self, side):
    self.width = side
    self.height = side

  # Returns a string describing the values of the square if a print(object) ie. print(sq) is called.
  def __str__(self):
    output = "Square(side=" + str(self.width) + ")"
    return output
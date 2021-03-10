class Category:
  
  # Will instantiate an object of the class.
  def __init__(self, category):
    # In this case (self.catergory = category) is the name given to the object in the paramenter.
    self.category = category
    # Creates an empty list variable to store class methods output values.
    self.ledger = []
    # Creates varible with numeric value of 0. To store either Interger or Float outputs.
    self.total_spend = 0
  
  # When the object is called in (main.py) with this method, parameters for the deposit amount and name are provided.
  def deposit(self, amount, description=""):
    # Creates an empty dictionary variable.
    self.dep = {}
    # Sets the (amount) parameter as dictionary key. In this case it should be an interger or float.
    self.dep["amount"] = amount
    # Sets the (description) parameter as dictionary value. In this case it should be a string.
    self.dep["description"] = description
    # Appends the dictionary created to the objects (self.ledger) list variable.
    self.ledger.append(self.dep)
  
  # When the object is called in (main.py) with this method, parameters for the withdraw amount and name are provided.
  def withdraw(self, amount, description=""):
    # Runs the class (self.check_funds) method. 
    x = self.check_funds(amount)
    # If (self.check_funds) returns True. The loop executes, else returns a False Boolean.
    while x == True:
      # Creates an empty dictionary variable.
      self.witdr = {}
      # Sets the (amount) parameter as dictionary key. In this case it should be an interger or float and makes converts to a negative value.
      self.witdr["amount"] = - amount
      # Sets the (description) parameter as dictionary value. In this case it should be a string.
      self.witdr["description"] = description
      # Appends the dictionary created to the objects (self.ledger) list variable.
      self.ledger.append(self.witdr) 
      # Adds the (amount) to the objects (self.total_spend) Interger/Float variable. ** Note NOT converted to a negative.
      self.total_spend += amount
      return True
    else:
      return False

  # When the object is called in (main.py) with this method, parameters for the tranfer amount and the catergory it's being drawn from are provided.
  def transfer(self, amount, category):
    # Creates a string variable of the objects name being called.
    category_name = category.category
    # Runs the class (self.check_funds) method.
    i = self.check_funds(amount)
    # If (self.check_funds) returns True. The loop executes, else returns a False Boolean.
    while i == True:
      # Runs the class (self.withdraw) method. Provides the (amount) parameter value, 
      # and uses string formatting to add the string "Transfer to" to the (category_name) string variable, for the parameter value.  
      self.withdraw(amount, f"Transfer to {category_name}")
      # Runs the class method (deposit) on the (category) object called in the methods parameters.
      category.deposit(amount,f"Transfer from {self.category}")
      return True
    else:
      return False

  # Creates the class method that will be called on in the methods above.
  def check_funds(self, amount):
    # Creates varible with numeric value of 0. To store either Interger or Float outputs.
    funds = 0
    # Loops through the range of the class list (self.ledger). As the list as appended to. This method will account for that.
    for x in range(len(self.ledger)):
      # Uses x to find the (self.ledger) lists current index and then uses the key value to pull the amount from the dictionay being stored in the list.
      # Adds that amount to the (funds) numeric variable.
      funds += self.ledger[x]['amount']
    # If the amount being requested is greater than the funds avaible. Returns a False Boolean, esle returns True.
    if funds < amount:
      return False
    else:
      return True

  # Works very much in the same way as the (check_funds) method above. Does not require paraments as is used to check and return the class objects balance.
  def get_balance(self):
    balance = 0
    for x in range(len(self.ledger)):
      balance += self.ledger[x]['amount']
    return balance 

  ############################################################
  ####   BLOCK OF LOGIC TO COMPUTE BUDGET OUTPUT STRING   ####
  ############################################################

  # The __str__ built-in fuction here is required to render the object as a 
  # string or "Something a human can read". When the print function of the 
  # object is called Otherwise you would print the actual object of the class. 
  # Which would look like this: <budget.Category object at 0x7f2e83822a30>

  def __str__(self):
    # Uses string formatting to place the category string inbetween * characters in a string that is 30 characters in total.
    title = f"{self.category:*^30}\n"
    
    items = ""
    
    total = 0

    # Loops through the range of items in the (self.ledger)
    for x in range(len(self.ledger)):
      # Uses string formating to create a describtion that is 23 char max length and renders a string to the 23 index posistion if needed.
      # Then uses string concatanation to concatenation to add the next string format, which is the amount at a max of 7 characters and 2 decimal places.
      # Adds this string to the empty string variable above (items). The "\n" break will make sure each string print on a new line.
      items += f"{self.ledger[x]['description'][0:23]:23}" + f"{self.ledger[x]['amount']:>7.2f}" + '\n'
      # Takes the amounts. Posistive and negative values and adds or subtracts those to the empyt numerical value (total) above.
      total += self.ledger[x]['amount']

    # Uses string formatting to round the total ouput float down to 2 decimal places and converts to a string.
    total_output = f"{total:.2f}"

    # Uses string concatenation to build the rendered output string.
    output = title + items + "Total: " + total_output
    
    # Returns that string.
    return output

#############################################################
#########   FUNCTION RETURNS BUDGET GRAPHS VALUES   #########
#############################################################

# Function that calls in the objects created using the class as parameters.
def create_spend_chart(categories):
  
  category_names = []

  total_spent = 0

  total_spends = []

  spending_percentages = []

  for i in categories:
    # Takes the name of each object. ie. (self.catergory = category) and appends to empty list variable (category_names).
    category_names.append(i.category)
    # Appends the (self.total_spend) variable of each object to the empty list variable (total_spends).
    total_spends.append(i.total_spend)
    # Loops through each item in the objects (self.ledger) variable.
    for item in i.ledger:
      # if the numeric amount at the key ("amount") is less than 0 .ie a negative value: withdraw or transfer.
      if item["amount"] < 0:
        # Adds that amount to a sum total at the 0 numeric variable (total_spend) for each class object. 
        # abs() function converts to absolute value. ie. from negative values to postive.
        total_spent += abs(float(item["amount"]))

  # Iterates/Loops throgh the recenty created (total_spends) list variable.
  for i in total_spends:
    # Creates a rounded percentage of that amount based on decimal ceiling or floor value.
    percentage = round((i / total_spent) * 100)
    # Appends these values to the empty list varibale (spending_percentages).
    spending_percentages.append(percentage)

  # Stores the max length of characters from the string in string (category_names) list. 
  longest = len(max(category_names, key=len))
  
  # Loop iterates through each string (category_names) list.
  for i in category_names:
    # Makes each category string the same length of characters by using the .ljust() string method 
    # to left justify each string by that max (longest) length variable. Replaces the original list items with
    # these adjusted ones.
    category_names[category_names.index(i)] = i.ljust(longest)
  
  # Returns a call for the next function with the following outputs from this function as parameters.
  return render_graph(longest, category_names, spending_percentages)

#############################################################
####   FUNCTION RETURNS GRAPH VALUES AS RENDERED GRAPH   ####
#############################################################

def render_graph(longest, category_names, spending_percentages):

  ############################################################
  #########   PRINTS PERCENTAGES IN VERTICAL LINES   #########
  ############################################################

  # Empty string variable to store the output of the loop below
  graph = ""

  # Creates a loop that starts at a range of 100, decreases that amount by -10 each loop and ends at but not including -10, therefor ending at 0. 
  for i in range(100, -10, -10):
    # Creates a string variable with 1 blank characters space.
    bar = " "
    # Creates a string starting with the range(100, -10, -10) integer of 100 (3 character spaces). Will use the .rjust() function to right align each
    # of the strings in the range created by 3 characters. String concatenate a Vertical "|" to the end of each of these strings.
    line = str(i).rjust(3) + "|"
    # Loops throught the (spending_percentages) list.
    for percent in spending_percentages:
      # Until those values either match or are less than the (i) variable in the loop. Adds "o  " to the string.
      if percent >= i:
        bar += "o  "
      # If the values don't mathch add three empty characters to the string.
      else:
        bar += "   "
    # Adds the (bar) string variable created in each loop iteration to the (line) string variable.
    line += bar
    # And for each interation adds that (line) string variable to the (graph) string variable.
    graph += line + "\n"

  # By looking at the above loop. We know that the dashed lines string variable needs to be aligned 4 characters spaces from the left.
  # And that we will need sets of dashed lines that are 3 dashed lines, multipled by the amount of category objects. Add a final dash to
  # to the end of that and a break line.
  dashes = "    " + (len(category_names) * 3) * "-" + "-" +  "\n"

  #############################################################
  ##########   PRINTS CATEGORIES IN VERTICAL LINES   ##########
  #############################################################
  
  # We know that the graph string above will be 5 characters long before we want to start adding the catergories.
  # Thus we need to start the string with 5 blank characters in the string.
  category_string = "     "

  # Using range indexing of the longest character string in (category_names) list to iterate the loops.
  # Had to split into two seperate (for) loops. The first starts at the 0 index and ends at the second last index (longest-1).
  # The second for loop starts and the (longest-1) so will it will only loop once. To avoid adding another "\n" break line at the end of the string. 
  for i in range(0, longest-1):
    # Loops through the indexes 0 through to 6 in this case.
    if i <= longest:
      # Uses that index to extract the charater in the string at that index.
      for index in category_names:
        # Adds that character to the (category_string) string variable. With 2 blank charater spaces concatenated onto it.
        category_string += index[i] + "  "
      # Once each loop has completed add a "\n" new line break, with 5 blank character space so the next line starts inline with the last string.
      category_string += "\n     "

  # Loops through the last index in this case index 7.
  for i in range(longest-1, longest):
    # Uses that index to extract the charater in the string at that index.
    for index in category_names:
      # Adds that character to the (category_string) string variable. With 2 blank charater spaces concatenated onto it
      category_string += index[i] + "  "

  # String concatenation to build the final graph output render string.
  output = "Percentage spent by category" + "\n" + graph + dashes + category_string

  # Returns the string made in the (output) variable above.
  return output
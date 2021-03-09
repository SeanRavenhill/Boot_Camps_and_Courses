class Category:
  
  def __init__(self, category):
    self.category = category
    self.ledger = []
    self.total_spend = 0
  
  def deposit(self, amount, description=""):
    self.dep = {}
    self.dep["amount"] = amount
    self.dep["description"] = description
    self.ledger.append(self.dep)

  def withdraw(self, amount, description=""): 
    x = self.check_funds(amount)
    while x == True:
      self.witdr = {}
      self.witdr["amount"] = - amount
      self.witdr["description"] = description
      self.ledger.append(self.witdr)
      self.total_spend += amount
      return True
    else:
      return False

  def transfer(self, amount, category):
    category_name = category.category

    i = self.check_funds(amount)

    while i == True:
      self.withdraw(amount, f"Transfer to {category_name}")
      category.deposit(amount,f"Transfer from {self.category}")
      return True
    else:
      return False

  def check_funds(self, amount):

    funds = 0

    for x in range(len(self.ledger)):
      funds += self.ledger[x]['amount']
    if funds < amount:
      return False
    else:
      return True

  def get_balance(self):
    balance = 0
    for x in range(len(self.ledger)):
      balance += self.ledger[x]['amount']
    return balance 

  def __str__(self):

    title = f"{self.category:*^30}\n"
    items = ""
    total = 0

    for x in range(len(self.ledger)):
      items += f"{self.ledger[x]['description'][0:23]:23}" + f"{self.ledger[x]['amount']:>7.2f}" + '\n'
      total += self.ledger[x]['amount']

    total_output = f"{total:.2f}"

    output = title + items + "Total: " + total_output

    return output

def create_spend_chart(categories):
  
  category_names = []
  total_spent = 0
  total_spends = []
  spending_percentages = []

  for i in categories:
    category_names.append(i.category)
    total_spends.append(i.total_spend)
    for item in i.ledger:
      if item["amount"] < 0:
        total_spent += abs(float(item["amount"]))

  for i in total_spends:
    percentage = round((i / total_spent) * 100)
    spending_percentages.append(percentage)

  longest = len(max(category_names, key=len))
  
  for i in category_names:
    category_names[category_names.index(i)] = i.ljust(longest)
  
  return render_graph(longest, category_names, spending_percentages)

def render_graph(longest, category_names, spending_percentages):

  graph = ""

  for i in range(100, -10, -10):
    bar = " "
    line = str(i).rjust(3) + "|"
    for percent in spending_percentages:
      if percent >= i:
        bar += "o  "
      else:
        bar += "   "
    line += bar
    graph += line + "\n"

  dashes = "    " + (len(category_names) * 3) * "-" + "-" +  "\n"

  category_string = "     "

  for i in range(0, longest-1):
    if i <= longest:
      for index in category_names:
        category_string += index[i] + "  "
      category_string += "\n     "

  for i in range(longest-1, longest):
    for index in category_names:
      category_string += index[i] + "  "

  output = "Percentage spent by category" + "\n" + graph + dashes + category_string

  return output
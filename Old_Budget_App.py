class Category:
  def __init__(self,name):
    self.ledger = []
    self.balance = 0
    self.CategoryName = name
    self.totalWithdraws = 0
  
  def deposit(self, amount, description=""):
    self.ledgerObject = {}
    self.amount = amount
    self.balance = self.balance + self.amount
    self.description = description
    self.ledgerObject["amount"] = self.amount
    self.ledgerObject["description"] = self.description
    self.ledger.append(self.ledgerObject)

  def check_funds(self, amount):
    if amount > self.balance:
      return False
    else:
      return True
  
  def withdraw(self, amount, description=""):
    if self.check_funds(amount) is True:
      self.amount = amount
      self.totalWithdraws = self.totalWithdraws + self.amount
      self.ledgerObject = {}
      self.amount = amount*(-1)
      self.balance = self.balance + self.amount
      self.description = description
      self.ledgerObject["amount"] = self.amount
      self.ledgerObject["description"] = self.description
      self.ledger.append(self.ledgerObject)
      return True
    else:
      return False
    
  def get_balance(self):
    return(self.balance)
    
  def transfer(self, amount, othercategory):  
    if self.check_funds(amount) is True:
      self.withdraw(amount,f"Transfer to {othercategory.CategoryName}")
      othercategory.deposit(amount,f"Transfer from {self.CategoryName}")
      return True
    else:
      return False

  def __str__(self):
    asterBar = ""
    asterLen = int((30-len(self.CategoryName))/2)
    for number in range(asterLen):
      asterBar = asterBar + "*"
    title = asterBar + self.CategoryName + asterBar
    ledgerStrList = []
    finalLedgerStr = ""
    for element in self.ledger:
      prntDescription = element["description"]
      if len(prntDescription) >= 23:
          prntDescription = prntDescription[0:23]
      else:
        spaceBarLen = 23-len(prntDescription)
        spaceBar = ""
        for number in range(spaceBarLen):
          spaceBar = spaceBar + " "
        prntDescription = prntDescription + spaceBar
      prntAmount = element["amount"]
      if type(prntAmount) is int:
        prntAmount = str(prntAmount) + ".00"
      else:
        prntAmount = str(prntAmount)
      if len(prntAmount) >= 7:
        prntAmount = prntAmount[0:7]
      else:
        spaceBarLen2 = 7-len(prntAmount)
        spaceBar2 = ""
        for number in range(spaceBarLen2):
          spaceBar2 = spaceBar2 + " "
        prntAmount = spaceBar2 + prntAmount
      line = prntDescription + prntAmount
      ledgerStrList.append(line)
    for element in ledgerStrList:
      finalLedgerStr = finalLedgerStr + element +"\n"
    if type(self.balance) == int:
      fancyBalance = str(self.balance) + ".00"
    else:
      fancyBalance = str(self.balance)
    totalStr = "Total: " + fancyBalance
    objStr = title + "\n" + finalLedgerStr + totalStr
    return objStr
      

def create_spend_chart(categories):
  totalspent = 0
  percentageList = []
  simpPercentageList = []
  finalstr = ""
  longestLen = 0
#generating floating point percentages
  for object in categories:
    totalspent = totalspent + object.totalWithdraws
    if len(object.CategoryName) > longestLen:
      longestLen = len(object.CategoryName)
  for object in categories:
    percentageList.append((object.totalWithdraws*100)/totalspent)
#rounding down
  for number in percentageList:
    tempNumber = number/10
    tempNumber = int(tempNumber)
    tempNumber = tempNumber*10
    simpPercentageList.append(int(tempNumber/10))
      
# parsing the string.
  # parsing the percentage bars, and adding them to finalstr.
  percLineList = ["  0|"," 10|"," 20|", " 30|"," 40|"," 50|"," 60|"," 70|"," 80|"," 90|","100|"]
  for number in reversed(range(11)):
    for percentage in simpPercentageList:
      if percentage >= (number) :
        percLineList[number] = percLineList[number] + " " + "o" + " "
      else:
        percLineList[number] = percLineList[number] + "   "
    percLineList[number] = percLineList[number] + " "
  for element in reversed(percLineList):
    finalstr = finalstr + element + "\n"
  # parsing the dash-line, adding it to finalstr
  dashString = "    "
  for object in categories:
    dashString = dashString + "---"
  dashString = dashString + "-"
  finalstr = finalstr + dashString
  # parsing the names and adding them to finalstr
  nameStr = ""
  for number in range(longestLen):
    nameStr = nameStr + "     "
    for object in categories:
      try:
        nameStr = nameStr + object.CategoryName[number] + "  "
      except:
        nameStr = nameStr + "   "
    nameStr = nameStr+"\n"
  nameStr = nameStr[0:-1]
  finalstr = "Percentage spent by category\n" + finalstr +"\n"+ nameStr

  return(finalstr)


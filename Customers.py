from datetime import date
class Customers:
  def __init__(self, CustID, CustName, CustAddress, Dateofjoin, Revenue):
    self.CustID = CustID
    self.CustName = CustName
    self.CustAddress = CustAddress
    self.Dateofjoin = Dateofjoin
    self.Revenue = Revenue
  
  def setID(self,CustID):
    if isinstance(CustID, str):
      self.CustID = CustID
    raise ValueError("ID must be string")
  def getID(self):
    return self.CustID
  
  def setName(self,CustName):
    if isinstance(CustName, str):
      self.CustName = CustName
    raise ValueError("Name must be string")
  def getName(self):
    return self.CustName
  
  def setAdd(self,CustAddress):
    if isinstance(CustAddress, str):
      self.CustAddress = CustAddress
    raise ValueError("Address must be string")
  def getAdd(self):
    return self.CustAddress
  
  def setDate(self,Dateofjoin):
    if isinstance(Dateofjoin, date):
      self.Dateofjoin = Dateofjoin
    else:
      raise ValueError("Date must be of type date")

  def setRev(self,Revenue):
    if isinstance(Revenue, float):
      self.Revenue = Revenue
    raise ValueError("Revenue must be float")
  def getRev(self):
    return self.Revenue
  
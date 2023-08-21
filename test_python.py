#Ex.1
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
  
# Ex.2
def addCustomer():
  id = input("nhap ID: ")
  name = input('nhap ten: ')
  addr = input('nhap dia chi: ')
  datej = input('nhap ngay tham gia: ')
  rev = input('nhap doanh thu: ')
  cus = Customers(id,name,addr,datej,rev)
  return cus

def addListCustomer(customers):
  num_cust = int(input("nhap so luong khach: "))
  for i in range(num_cust):
    print(f'nhap du lieu cua khach thu #{i+1}: ')
    cus = addCustomer()
    customers.append(cus)
  return customers

def searchCustomer(customers):
  name = input('nhap ten can tim: ')
  for customer in customers:
    if customer.getName() == name:
      return customer
    return None
  
def printCustomer(customers):
  for i in customers:
    print('ID: ', i.getID())
    print('Name: ', i.getName())
    print('Address: ', i.getAdd())
    print('Date of join: ', i.getDate())
    print('Revenue: ', i.getRev())
    print("********************")

def calRevenue(customers):
  total = 0.0
  for customer in customers:
    total += float(customer.getRev())
  return total

def main():
  customers = []
  while True:
    print('1. Add a customer')
    print('2. Add a list of customers')
    print('3. Find the Name')
    print('4. Print all customers')
    print('5. Calculate sum of all revenue')
    print('6. exit')
    chon = int(input('Nhap so: '))
    if chon == 1:
      cus = addCustomer()
      customers.append(cus)
    elif chon == 2:
      addListCustomer(customers)
    elif chon == 3:
      found_cus = searchCustomer(customers)
      if found_cus:
        print('ID: ', found_cus.getID())
        print('Name: ', found_cus.getName())
        print('Address: ', found_cus.getAdd())
        print('Date of join: ', found_cus.getDate())
        print('Revenue: ', found_cus.getRev())
      print('khong tim thay!')
    elif chon == 4:
      printCustomer(customers)
    elif chon == 5:
      print("tong doanh so la: ", calRevenue(customers))
    elif chon == 6:
      break

if __name__ == '__main__':
  main()

from Customers import Customers

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
    chon = int(input('Nhap so muon chon: '))
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

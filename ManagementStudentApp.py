
from Student import Student

ls = []
def addStudent():
    print('--Nhập thông tin sinh viên--')
    id = int(input("Nhập id: "))
    ten = input("Nhập tên: ")
    math = float(input("Nhập điểm toán: "))
    phy = float(input("Nhập điểm lý: "))
    chem = float(input("Nhập điểm hóa: "))
    stu = Student(id, ten, math, phy, chem)
    return stu

def viewStudent(Student):
    print('view')

def addListOfStudent():
    print('add List')
    sl = int(input("Nhập số lượng sinh viên: "))
    for i in range(sl):
        print('Nhập thông tin sv ' + str(i+1))
        stu = addStudent()
        ls.append(stu)

def printListOfStudent():
    for i in ls:
        print(i.getInfo())
       
def findTheBestOfStudent():
    max = ls[0].getAverageMark()
    im = 0
    for i in range(len(ls)):
        if(ls[i].getAverageMark() > max):
            max = ls[i].getAverageMark()
            im = i
    print(ls[im].getInfo())

def main():
    while True:
        print('1. Add List')
        print('2. Print List')
        print('3. Find the best')
        print('nhấn 0 để thoát')
        chon = int(input("chọn chức năng"))
        if(chon == 1):
            addListOfStudent()
        elif(chon == 2):
            printListOfStudent()
        elif(chon == 3):
            findTheBestOfStudent()
        else:
            print('kết thúc chương trình')
            break


main()

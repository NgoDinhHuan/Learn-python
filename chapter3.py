
# vidu1

# sum = 0
# for i in range(1,51):
#     sum = sum + i
# print (sum)

#vidu2

# n = int (input("nhap n:"))
# giaithua = 1
# for i in range (1,n+1):
#     giaithua = giaithua * i
# print(giaithua)

# vidu3 tong cac so le

# n = int (input ("nhap n:"))
# sum = 0
# for i in range (1,n+1):
#     if i % 2 !=0:
#         sum = sum + i
# print (sum)


# # bai6 assg
# while true:
#     Code = input("nhap code sv : ")
#     Name = input("nhap name sv : ")
#     Sex = input("nhap sex sv : ")
#     Age = input("nhap tuoi sv :")
#     print("masv:" + Code)
#     print("Name:" + Name)
#     print("Sex:" + Sex)
#     print("Age:" + Age)

#     choice = input("tiep(y), ketthu(n)")
#     if(choice.lower()=='n'):
#         print("ket thuc")
#         break


# vidu the tesr scores program

# while True:
#     test_score = int (input("enter test code:"))
#     if test_score >=0 and test_score <= 100:
#         score_total + 



# bai tap 1
# print ('the mile program')
# while True:
#     m = int (input("Enter m:"))
#     g = float(input("Enter g:"))
#     c = float(input("Enter c:"))
#     mpg = m/g
#     tgc = c * g
#     cpm = mpg/tgc
#     print("MPG:", mpg)
#     print("TGC:", tgc)
#     print("CPM:", cpm)
#     choice = input("yes (y) or (No) n")
#     if(choice == "n"):
#         break

# bai tap in tam giac
# n = int (input("nhap so canh:"))
# for i in range(0, n):    
#     for j in range(0, i+1): 
#         print("* ",end="") 
#     print("\n") 

# xoay 180
# n = int (input("nhap so canh:"))
# k = 2*n - 2
# for i in range(0, n): 
#     for j in range(0, k): 
#         print(end=" ")   
#     k = k - 2     
#     for j in range(0, i+1): 
#         print("* ", end="") 
#     print("\n") 

# xoay nguoc
n = int (input("nhap so canh:"))
for i in range(0, n):
    for j in range(0, i):
        print(end = "  ");
    for j in range(i, n):
        print(" *", end = "");
    print("\n")
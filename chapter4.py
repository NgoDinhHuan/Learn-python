# def tong_tich(x,y):
#     tong = x+y
#     tich = x*y
#     return tong,tich
# t, ti = tong_tich(2,3)
# print(t)
# print(ti)


# def ful_value():
#     while True:
#         mon_in = int(intput("enter monthy investment:"))
#         year_in = int(input("enter year interest rate:"))
#         year = int (input("enter year"))

#         c = input("countinue: y/n")
#         if (c == 'y'):
#             break


# def computepay(hours, rate):
#     return hours * rate

# regular_rate = float(input("Hourly rate in dollars: "))
# regular_hours = float(input("Regular hours worked: "))
# print(f"pay: ${total_pay:}")


# def computegrade(tmp_score):
#     if 0.0 <= tmp_score <= 1.0:
#         if tmp_score >= 0.9:
#             return 'A'
#         if tmp_score >= 0.8:
#             return 'B'
#         if tmp_score >= 0.7:
#             return 'C'
#         if tmp_score >= 0.6:
#             return 'D'
#         return 'F'

#     return 'Bad score'


# input_score = input('Enter score: ')
# score = 0.0

# try:
#     score = float(input_score)           
# except ValueError:
#     print('Bad score')
    
  

# grade = computegrade(score)
# print(grade)


# input : aba --> xâu đối xứng, abab --> ko đối xứng


# def xau_doi_xung(string):
    
#     string = input("nhap vao chuoi:")
#     if string == string[::-1]:
#         print("xâu đối xứng")
#     else:
#         print("xâu ko đối xứng")
#     print(string)


def kiem_tra(chuoi):
    if len(chuoi) % 2 !=0:
        return "ko doi xung"
    else:
        d = ""
        c = ""
        t = len(chuoi)//2
        for i in range(0,t):
            d = d + chuoi[i]
        for i in range(t, len(chuoi)):
            c = c + chuoi[i]
        x = d[::-1]
        if(x == c):
            return "doi xung"
        else:
            return"ko doi xung"
print(kiem_tra("abba"))

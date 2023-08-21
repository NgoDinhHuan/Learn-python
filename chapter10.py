# s = input("Nhập câu:")
# d={"UPPER CASE":0, "LOWER CASE":0}
# for c in s:
#     if c.isupper():
#         d["UPPER CASE"]+=1
#     elif c.islower():
#         d["LOWER CASE"]+=1
#     else:
#         pass
# print ("Chữ hoa:", d["UPPER CASE"])
# print ("Chữ thường:", d["LOWER CASE"])

# s = "hello"
# s1 = list(s)
# print(s.split("  "))

# s = "tinhpham2@fpt.edu.vn"
# print(s.find('@'))# tra ve vi tri dau ki tu @
# print(s.replace('.','/'))

# mail = input("nhap mail:")
# v = mail.index("@")# tim vi tri cua @ trong chuoi
# ten_mail = mail[0:v]
# print(ten_mail.upper())


# bt2
# def khong_trung_lap(s):
#     #Chuoi luu cac ky tu khong trung lap
#    KetQua = ""
#    #Su dung vong lap for duyet qua cac ky tu cua chuoi s
#    for kyTu in s:
#        #Neu ky tu chua xuat hien trong KetQua thi them vao
#        if kyTu not in KetQua:
#            KetQua += kyTu
#    return KetQua

# def dem_ky_tu(s):
#    #Goi ham de tra ve chuoi gom cac ky tu xuat hien trong chuoi s
#    chuoiKyTu = khong_trung_lap(s)
               
#    for kyTu in chuoiKyTu:#Su dung vong lap for de duyet cac ky tu
#        #Su dung phuong thuc count() de dem so lan xuat hien trong chuoi s
#        dem = s.count(kyTu)
#        print("{}-{}\n ".format(kyTu, dem) )

# s = input("nhap chuoi:")
# dem_ky_tu(s)

# string = " iviettech"
# count = {}
# for i in string:
#     if i in count:
#         count[i] += 1
#     else:
#         count[i] = 1
#         print(count)


#bt1
s=input("Nhập họ tên: ")

A=s.split(" ")

print("Tên: ", A[len(A)-1])
print("Tên đệm: ", A[len(A)-2])
print("Họ:", A[len(A)-3])
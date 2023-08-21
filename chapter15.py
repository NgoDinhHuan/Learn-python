# class cha:
#   def __init__(self, tien, nha):
#     self.tien = tien
#     self.nha = nha

#   def taisan(self):
#     return "so tien:" + str(self.tien) + 'so nha' + str(self.nha)
  
# class con(cha):
#   def __init__(self,tien, nha, bangcap):
#     super().__init__(tien, nha)
#     self.bangcap = bangcap
#   def taisan(self):
#     return super().taisan() + 'bang cap: ' + self.bangcap
  
#   def taisan(self, soLuong):
#     return super().taisan() +'bang cap: ' + str(soLuong)

# con = con(500, 1, "DH")


# print(con.taisan(3))


# bt asm

# def Circumference(n, s):
#     Circumference = 1
#     Circumference = n * s

#     return Circumference

# if __name__== '__main__':
    
#     n = int(input("nhap so canh:"))
 
#     s = float(input("nhap do dai canh:"))
#     # find perimeter
#     peri = Circumference(s, n)
 
#     print("chu vi cua da giac voi:"
#           ,n,"canh va do dai",s,"=",peri)
     


# bt 2
class Polygon:

    def __init__(self, n):
        self.number_of_sides = n

    def print_num_sides(self):
        print(f'There are {self.number_of_sides} sides.')

class Triangle(Polygon):

    def __init__(self, lengths_of_sides):
        Polygon.__init__(self, 3)
        self.lengths_of_sides = lengths_of_sides  # list of three numbers

    def get_area(self):
        a, b, c = self.lengths_of_sides
        s = (a + b + c) / 2
        return (s*(s-a)*(s-b)*(s-c)) ** 0.5

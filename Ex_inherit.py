class Poly:
  def __init__(self, sides, dimension):
    self.sides = sides
    self.dimension = dimension


  def circumference(self):
    return sum(self.dimension)
  
  def sides_polygon(self):
    for i in self.dimension:
      print(i)

class Triangle(Poly):
  def __init__(self, dimension):
    super().__init__(3, dimension)
  
  def perimeter(self):
    super().circumference
  
  def sides_valid(self):
    if len(self.dimension) != 3:
      return False
    a, b, c = self.dimension
    return a + b > c and a + c > b and b + c > a
  
  def triangle_area(self):
    a, b, c = self.dimension
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

  def show_peri_are(self):
    print(self.perimeter() + self.triangle_area())

dimension = [4,5,6]

ta = Triangle(dimension)

print(ta.triangle_area())


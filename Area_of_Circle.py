#Create a Python program that computes the area of a circle

def main():
 class Circle:
  def __init__(self, measurement=1):
   self._measurement = measurement


 class AreaUsingRadius(Circle):
  def area_radius(self):
   pi = 3.14
   return (pi * (self._measurement ** 2))

 radius = float(input("Enter the Radius of the Circle: "))
 solve = AreaUsingRadius(radius)
 print("The Area of the Circle is", str(solve.area_radius()) + " square unit", ".")

 class AreaUsingDiameter(Circle):
  def area_diameter(self):
   pi = 3.14
   return pi * ((self._measurement/2) ** 2)

 diameter = float(input("Enter the Diameter of the Circle: "))
 solve = AreaUsingDiameter(diameter)
 print("The Area of the Circle is", str(solve.area_diameter()) + " square unit", ".")


main()

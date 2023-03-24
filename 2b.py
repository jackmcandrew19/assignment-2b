# TASK: calculates the area and circumference of the circle
#diameter/2 = r
#A = πr2 or
#C = 2πr or pi*D
#Show A and C


#def getRadius(diameter):
  # Write your function here
 # radius = float(diameter) / 2
 # return float(radius)
 
def GetArea(radius):
  # Wrie your function here
  Area = 3.14 *(radius * radius)
  return float(Area)
 
def GetCirc(radius):
  Circ = 3.14 *(radius) * 2
  return Circ
 
 
diameter = input("What is your diameter? ")
radius = float(diameter) / 2

#print("Your radius is: ",getRadius(diameter))
print("Your area is: ", GetArea(radius))

print("Your Circumference is: ", GetCirc(radius))


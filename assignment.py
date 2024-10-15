import math

# Detect if it's a float string, found code from pythonhow.com
def is_float(string):
    if string.replace(".", "").isnumeric():
        return True
    else:
        return False

def get_diameter():
    print("Enter the diameter, without units.")
    dia = input()
    if is_float(dia) == True:
      dia = float(dia)
      return dia
    else:
      print("That isn't a number!")
      dia = get_diameter()
      return dia

d = get_diameter()
print("Calculating...")
r = d/2
a = r**2*math.pi
c = 2*math.pi*r
print("The radius is:", r,"units")
print("The area is:", a,"units")
print("The circumference is:", c,"units")
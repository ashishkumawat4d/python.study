print("press 1 for Kilometer to Meter")
print("press 2 for Meter to Kilometer")
print("press 3 for Kilogram to Gram")
print("press 4 for Gram to Kilogram")

choice = int(input("Enter your choice "))


while True:
  if choice == 1:
      km = float(input("Enter kilometers: "))
      print("Meters =", km * 1000)
  
  elif choice == 2:
      m = float(input("Enter meters: "))
      print("Kilometers =", m / 1000)
  
  elif choice == 3:
      kg = float(input("Enter kilograms: "))
      print("Grams =", kg * 1000)
  
  elif choice == 4:
      g = float(input("Enter grams: "))
      print("Kilograms =", g / 1000)
  
  else:
      print("Invalid Choice")
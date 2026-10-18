
print("Welcome to the Interactive Personal Data Collector!\n")

name= input("Please enter your name:")

age = int(input("Please enter your age:"))
height= float(input("Please enter your height in meters:"))
fav= int(input("Please enter your Favourite number:"))

print("Thank you! Here is the information mwe collected:\n")

print(f"name: {name} (Type: {type(name)}, Memory Address: {id(name)})")

print(f"age: {age} (Type: {type(age)}, Memory Address: {id(age)})")

print(f"height: {height} (Type: {type(height)}, Memory Address: {id(height)})")

print(f"favourite number: {fav} (Type: {type(fav)}, Memory Address: {id(fav)})")

birth_year = 2026-age

print("\n Your birth year is approximately:")
print(birth_year,f"(based on your age of {age})")

print("\nThank you  for using the Personal Data Collector. Goodbye!")
      
      

      

      
          

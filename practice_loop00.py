#The code under uses the list of composers and a for loop to generate a message to each of the names in the list. At the end a single thank you message is displayed for everyone

classical_composers = ["Johann Sebastian Bach", "Wolfgang Amadeus Mozart", "Ludwig van Beethoven", "Frédéric Chopin", "Pyotr Ilyich Tchaikovsky"]


for classical_composer in classical_composers:
    print(f"{classical_composer.title()}, that was epic!")
    print(f"I can`t wait to hear your next musical performance, {classical_composer}!")

print("Thank you everyone. That was great!")


#Using the list fruits, python runs a for loop to give a message before each of the fruits, at the end gives a another message outside the loop
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

for fruit in fruits:
    print(f"I really like {fruit.title()}")
print("Fruits are good")

#Trying out numbers
#Testing out the range function to easily generate some numbers
for verdi in range(1,6):
    print(verdi)

#Genererer og lager en liste fra tallet 1-20 og printer det ut
numbers = list(range(1,21))
print(numbers)

""""
#Denne koden printer kun hele listen numbers 20 ganger og ikke teksten "Tallet, 1" "Tallet, 2
for number in numbers:
    print(f"Tallet, {numbers}")
"""
#Generer og lagrer et oddetalls liste
odd_numbers = list(range(1,26, 3))
print(odd_numbers)


#Listen square lagrer for loopen sin regnestykke. Regnestykket er å gange tallet på seg selv. altså 2*2=4 blir då etter på 4*4=16 og så videre og videre.
squares = []

#This for loop squares numbers and appends them into the "squares" list
for value in range(1, 11):
    square=value** 2
    squares.append(square)
print(squares)

#This generates a list ranging from 1 to 300
many_numbers = list(range(1,301))

#Finds the minimum number in the "many_numbers" list
minimum = min(many_numbers)
#Finds the maximum number in the "many_numbers" list
maximum = max(many_numbers)
#Sums all numbers togheter in the "many_numbers" list
total = sum(many_numbers)

#Prints the results
print(f"The smalles number is {minimum}")
print(f"The maximum number is {maximum}")
print(f"The total sum of the numbers is {total}")
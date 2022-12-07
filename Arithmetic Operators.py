# Practice
print("\n")
print("Number 1 is 10 \nNumber 2 is 20")
print("\n")
number1 = 10
number2 = 20

# 1. Addition +
summation = number1 + number2
print("The summation of number1 and number2 is:   ", summation)
print("\n")

# 2, Subtraction -
subtraction = number1 - number2
print("The su btraction of number2 from number1 is:   ", subtraction)
print("\n")

# 3. Multiplication *
multiplication = number1 * number2
print("The multiplication of number1 and number2 is:   ", multiplication)
print("\n")

# 4. FloatDivision /
division = number1 / number2
print("The FloatDivision of number1 by number2 is:   ", division)
print("\n")

# 5. Remainder %
"""Needs different number for calculation of remainder"""

r1 = 20
r2 = 3
remainder = r1 % r2
print("The remainder of 20 % 3 is:   ", remainder)
print("\n")

# 6. IntegerDivision //
"""Integer division is a division without the decimal point shown"""

integerDivision = r1 // r2
print("The IntegerDivision of 20 and 3 is:   ", integerDivision)
print("\n")

# 7. Exponential ** means to the power

exponential = 2 ** 3
print("The exponential; 2 to the power of 3 is:   ", exponential)
print("\n")

# Concatenation of words

c1 = "Tohibur "
c2 = "Rahman"
c3 = "Tauhid"

C = c1 + c2 + c3
print(r"The concatenation of", "Tohibur ", "Rahman" "Tauhid", "is:   ", C)
print("\n")

# Concatenation of number

cn1 = 1
cn2 = 2
cn3 = 3

C = cn1 + cn2 + cn3
print(r"The concatenation of 1, 2 and 3 is:   ", C)
print("\n")

"""There is no deference of between a = 3 ; a = 2 + 3   a += 2; ok ??? """

# Square

''' This is the Area of a Square'''

# The Area

a = float(input("Insert the length of one arm:   "))
area = a * a
print("The Area of the square is:   ", area)
print("\n")

# The Circumferences of square
circumferences = 4 * a
print("The circumferences of the qube of that square is:", circumferences)
print("\n")

# The Volume of the cube

volume = pow(a, 3)
print("The volume of the square is:   ", volume)
print("\n")

# The Temperature Measurement
# Fahrenheit
c = float(input("Insert the Celsius value:   "))
F = 1.4 * c + 32
K = c + 273.15
print("The Fahrenheit Value of the Celsius is:   ", F)
print("\n")
print("The Kelvin value of temperature is:   ", K)
print("\n")

# Celsius
f = float(input("Insert the Fahrenheit value:   "))
C = (f-32)/1.4
K = ((f-32)/1.4) + 273.15
print("The Celsius value of The temperature is:   ", C)
print("\n")

print("The Kelvin value of the temperature is:   ", K)
print("\n")

# Kelvin
k: float = float(input("Insert the  Kelvin value:   "))
C = k - 273.15
F = ((k - 273.15) * 1.4) + 32
print("The Celsius value of the temperature is:   ", C)
print("\n")

print("The Fahrenheit valur of the temperature is:   ", F)

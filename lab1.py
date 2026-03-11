print(type(1))
print(type(1.0))
print(type(-10) )
print(type(0)  )
print(type(0.0) )   # float
print(type(2.2) )   # float
print(type(4E2))    # float -> 4*10 to the power of 2type(4E2)    # float -> 4*10 to the power of 2


# Arithmetic

print(10 + 3 )  # 13
print(10 - 3)   # 7
print(10 * 3  ) # 30
print(10 ** 3)  # 1000
print(10 / 3)   # 3.3333333333333335
print(10 // 3 ) # 3 -> floor division - no decimals and returns an int
print(10 % 3  ) # 1 -> modulo operator - return the remainder. Good for deciding if number is even or odd


# Basic Functions

pow(5, 2)       # 25 -> like doing 5**2
abs(-50)        # 50
round(5.46)     # 5
round(5.468, 2) # 5.47 -> round to nth digit
bin(512)        # '0b1000000000' -> binary format
hex(512)        # '0x200' -> hexadecimal format


# Converting Strings to Numbers

age = input("How old are you?")
age = int(age)

pi = input("What is the value of pi?")
pi = float(pi)

#name

name= "Andreea Lavinia"
print(name[2])
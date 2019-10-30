#This program calculates the GCD of two numbers, a and b. Peadar o Cathain 30/10/2019

a = 50
b = 20

while b > 0:
  a, b = b, a % b
#LHS = NEw Values, RHS = Old Values

  print(b)


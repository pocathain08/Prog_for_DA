#This program calculates the GCD of two numbers, a and b. Peadar o Cathain 30/10/2019

def gcd(a, b):
  """ 
  #triple " allows the addition of a line
  Returns the Greatest Common Divisor of a and b.
  """
  if a < b:
    a, b = b, a
  #This swops the values to keep the greater on the left
    
  while b > 0:
    a, b = b, a % b

  return a

print (gcd(50, 20))
print (gcd(22, 143 ))

#The following is the original prog that didn't work!
#a = 50
#b = 20

#while b > 0:
#  a, b = b, a % b
#LHS = New Values, RHS = Old Values

  #print(b)


from time import sleep
from math import sqrt
a=int(input("Enter a number:"))
mill=float(input("Enter delay in milliseconds:"))
sleep(mill/1000)
print("Square root of",a,"after",mill," miliseconds is",sqrt(a))
"""
Project Name: Euclid Algorithm 
Project Description: 
Programmer: Michaela Pierce
Date: 10/31/22
UNCW, CSC 592 - Introduction to Cryptography
"""



import math
import time 
import random


#Euclid Algorithm to find GCD of two Inputs
def euclid(m,n):
    print(' i '  "\t", ' q '  "\t", ' m '  "\t", ' n ' "\t", ' r ')
    print( '_' * 40)
    if m < n:                                               # if m is less than n
        m,n = n,m                                           # swap (m,n)

    i=0
    while n != 0:                                           # while n does not equal 0
        r = m % n                                           # r = m mod n
        print ("\n")
        print(i,"\t", (m // n) ,"\t", m,"\t", n,"\t", r)
        
        i += 1

        m = n
        n = r
        
        
    print('STOP')
    return m 
    
    # At each round of iteration (i), m is divided by n, the quotient is called q,
    # and the remainder is called r. We keep repeating this till n = 0. At last,
    # we output m which is the greatest common divisor of our inputs.



    #Driver Code 
if __name__ == "__main__":
    #print(euclid(250, 111))
    print("\n")
    print("Euclid Algorithm")
    print("\n")
    print("This program will find the greatest common divisors (gcd) of two integers. ")
    print(" A table will be produced to list all of the factors (divisors) of m and" , \
          "all of the factors of n, and then compare the two lists and find the greatest", \
          "factor which serves as the gcd (m,n) ")
    print("\n")
    print("\n")
    m = int(input("Please enter the first integer (m) : "))
    print("\n")
    n = int(input("Please enter the second integer (n) : "))

    print("\n")
    print("\n")

    print(euclid(m,n))



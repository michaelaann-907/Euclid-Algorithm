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
def euclid(original_m, original_n, m, n):
    print(f"{'i':<4} {'q':<8} {'m':<10} {'n':<10} {'r':<10}")
    print('_' * 40)

    if m < n:          # if m is less than n                                           # if m is less than n
        m, n = n, m    # swap (m,n)                                 # swap (m,n)

    i=0
    while n != 0:    # while n does not equal 0                                         # while n does not equal 0
        r = m % n    # r = m mod n
        print(f"{i:<4} {(m // n):<8} {m:<10} {n:<10} {r:<10}")

        i += 1
        m = n
        n = r

    print("\n")
    print('STOP')
    print(f"The GCD of {original_m} and {original_n} is: {m}")
    return m

    # At each round of iteration (i), m is divided by n, the quotient is called q,
    # and the remainder is called r. We keep repeating this till n = 0. At last,
    # we output m which is the greatest common divisor of our inputs.



    #Driver Code 
if __name__ == "__main__":
    print("\n")
    m = int(input("Please enter the first integer (m): "))
    n = int(input("Please enter the second integer (n): "))

    print("\n")
    print(euclid(m,n,m,n))




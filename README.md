# Euclid Algorithm

## Project Description
This project implements the Euclid Algorithm to find the Greatest Common Divisor (GCD) of two integers. The program iteratively applies the Euclidean algorithm, which repeatedly calculates the remainder of division until it reaches zero, at which point the last non-zero remainder is the GCD. The program provides a step-by-step trace of the algorithm's execution, displaying the quotient, dividend, divisor, and remainder at each step.

<br/>
This program will implement algorithm below.

![image](https://user-images.githubusercontent.com/114198365/199097010-318a8b11-46ef-45b3-99d5-d41778119b90.png)

<br/>


A table will be the output for this program:


![image](https://user-images.githubusercontent.com/114198365/199097096-cc9f5bbb-8c35-48fa-b4bf-cd2367a70d60.png)


<br/>

## Features

1. **Input:** The program prompts the user to enter two integers, `m` and `n`.
2. **Execution:** The program applies the Euclid Algorithm to compute the GCD of `m` and `n`.
3. **Output:** The program outputs a table that shows each iteration of the algorithm, including the iteration index, quotient, dividend, divisor, and remainder. Finally, the GCD is displayed.

### Example
When the program runs, it will look like this:

```plaintext
Euclid Algorithm

This program will find the greatest common divisors (gcd) of two integers.
A table will be produced to list all of the factors (divisors) of m and
all of the factors of n, and then compare the two lists and find the greatest
factor which serves as the gcd (m,n) 


Please enter the first integer (m): 250

Please enter the second integer (n): 111


 i 	  q 	  m 	  n 	  r 
________________________________________


0 	  2 	  250 	  111 	  28


1 	  3 	  111 	  28 	  27


2 	  1 	  28 	  27 	  1


3 	  27 	  27 	  1 	  0
STOP

The GCD of 250 and 111 is: 1
```


## Installation & Usage
1. Make sure you have Python installed on your machine.
2. Run the `euclid_algorithm.py` file using Python:
   ```bash
   python euclid_algorithm.py
   ```
3. Follow the prompts to enter the two integers.



## Examples
Example 1
![euclid3](https://github.com/user-attachments/assets/5d60ee6c-bca8-49cd-80ac-d6a12666431b)
<br/>
<br/>
<br/>
Example 2
![euclid4](https://github.com/user-attachments/assets/3ee1a84f-ca1b-476f-8d24-acd1a0a930e3)






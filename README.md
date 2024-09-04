# Euclid Algorithm

## Project Description
This project implements the Euclid Algorithm to find the Greatest Common Divisor (GCD) of two integers. The algorithm iteratively computes the remainder of division until it reaches zero, at which point the last non-zero remainder is the GCD. The program provides a step-by-step trace of the algorithm's execution, displaying the quotient, dividend, divisor, and remainder at each step.

<br/>
The algorithm is visualized as follows:

![image](https://user-images.githubusercontent.com/114198365/199097010-318a8b11-46ef-45b3-99d5-d41778119b90.png)

<br/>


The program outputs a table like this:


![image](https://user-images.githubusercontent.com/114198365/199097096-cc9f5bbb-8c35-48fa-b4bf-cd2367a70d60.png)


<br/>

## Features
- **Input:** Prompts the user to enter two integers, `m` and `n`.
- **Execution:** Applies the Euclidean Algorithm to compute the GCD of `m` and `n`.
- **Output:** Displays a table showing each iteration of the algorithm, including the iteration index, quotient, dividend, divisor, and remainder. Finally, it shows the GCD.

<br/>

## Example
When running the program, the output will look like this:

```plaintext

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
1
```

<br/>

## Installation & Usage
1. Clone the repository or download the source code.
2. Run the `euclid_algorithm.py` file using Python:
   ```bash
   python euclid_algorithm.py
   ```
3. Follow the prompts to enter the two integers.

<br/>

## Examples

#### Example 1
![euclid3](https://github.com/user-attachments/assets/5d60ee6c-bca8-49cd-80ac-d6a12666431b)
<br/>
<br/>
#### Example 2
![euclid4](https://github.com/user-attachments/assets/3ee1a84f-ca1b-476f-8d24-acd1a0a930e3)






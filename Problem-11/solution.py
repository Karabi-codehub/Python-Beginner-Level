#import the math module to use the square root function
import math
def is_prime(n): #  This function checks if a number 'n' is a prime number.
                #A prime number is a number greater than 1 that has no divisors other than 1 and itself.
    
        if n<=1: #If the number is less than or equal to 1, it is not prime
             return False
        for i in range(2,int(math.sqrt(n)+1)): #Loops from 2 to √n, because if a number has any divisors, one of them will be less than or equal to its square root
            if n %1==0: #If n is divisible by any number in this range, it's not prime
               return False
           
        return True
 
user_input=int(input("Enter number:"))
print(is_prime(user_input)) 

#FizzBuzz

#Write a program that prints the numbers from 1 to 100.
#But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”.
#For numbers which are multiples of both three and five print “FizzBuzz".

#numbers 1 to 100
for i in range (1, 101):
    
    #multiples of 3 AND 5
     if i % 3 == 0 and i % 5 == 0:
         print("FizzBuzz")
         
    #multiples of just 3
     elif i % 3 == 0:
         print("Fizz")
         
    #multiples of just 5
     elif i % 5 == 0:
         print("Buzz")
         
    #neither a multiple of 3 nor 5
     else:
         print(i)
            

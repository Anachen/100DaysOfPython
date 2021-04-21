'''
EXERCISE FROM:
https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt
'''

#day 1
'''
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''
def div_by_seven():
    result = []
    for i in range(2000,3200):
        if i%7==0 and i%5>0:
            result.append(i)
    return print(result)
'''
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320

'''
import math
def factorial():
    try:
        x =int(input("Give me a number: "))
        return print(math.factorial(x))
    except ValueError as err:
        print(err)

'''
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
'''
def integral_num(num):
    result={}
    for i in range(1,num+1):
        result[i]=i*i
    return print(result)
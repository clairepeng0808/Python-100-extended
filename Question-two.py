'''
Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a 
single line.Suppose the following input is supplied to the program: 
8 Then, the output should be:40320
'''

'''
Hints:
In case of input data being supplied to the question, 
it should be assumed to be a console input.
'''
factorial = 1
n = int(input('Please provide a number: '))

for i in range(1, n+1):
    factorial = factorial*i

print(f'The factorial of {n} is {factorial}.')
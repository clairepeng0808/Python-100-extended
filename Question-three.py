'''
Question:
With a given integral number n, write a program to generate a 
dictionary that contains (i, i x i) such that is an integral 
number between 1 and n (both included). and then the program 
should print the dictionary.Suppose the following input is supplied to 
the program: 8
'''

'''
Hints:
In case of input data being supplied to the question, it should 
be assumed to be a console input. Consider use dict()
'''

n = int(input('Please enter a num: '))
result = {}
for i in range(1, n+1):
    result[i] = i*i

print(result)

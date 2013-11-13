#!/usr/bin/python

#n! means n  (n  1)  ...  3  2  1
#For example, 10! = 10  9  ...  3  2  1 = 3628800,and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#Find the sum of the digits in the number 100!

n = 100
numbers = range(1,n+1)
product = 1
for i in numbers:
    product = product*i
string = list(str(product))

digits = [float(i) for i in string]
digsum = sum(digits)

print digsum
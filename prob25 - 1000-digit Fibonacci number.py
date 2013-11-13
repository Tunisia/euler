#!/usr/bin/python

#The Fibonacci sequence is defined by the recurrence relation:
#Fn = Fn1 + Fn2, where F1 = 1 and F2 = 1.
#Hence the first 12 terms will be:
#F1 = 1
#F2 = 1
#F3 = 2
#F4 = 3
#F5 = 5
#F6 = 8
#F7 = 13
#F8 = 21
#F9 = 34
#F10 = 55
#F11 = 89
#F12 = 144
#The 12th term, F12, is the first term to contain three digits.
#What is the first term in the Fibonacci sequence to contain 1000 digits?

#1000 digits = > 10**1000

def fib():
    prevthis = [1, 1]
    yield 1
    yield 1
    while True:
        prevthis.append(sum(prevthis))
        prevthis.remove(prevthis[0])
        yield prevthis[-1]

f = fib()
count = 0

while True:
    count += 1
    this = f.next()
    if this > 10**1000:
        print count
        break



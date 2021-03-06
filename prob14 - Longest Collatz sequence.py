#!/usr/bin/python

#The following iterative sequence is defined for the set of positive integers:
#n  n/2 (n is even)
#n  3n + 1 (n is odd)
#Using the rule above and starting with 13, we generate the following sequence:
#13  40  20  10  5  16  8  4  2  1
#It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#Which starting number, under one million, produces the longest chain?
#NOTE: Once the chain starts the terms are allowed to go above one million.

def collatz(seed):
    seed = [float(seed)]
    i = seed[-1]
    while not seed[-1] == 1:
        if i / 2 == round(i/2):
            nexti = i/2
        else:
            nexti = i*3+1
        i = nexti
        seed.append(i)
    return seed

bestSeed = 0
longestChain = 0
    
for i in range(1,1000001):
    chain = collatz(i)
    if len(chain) > longestChain:
        longestChain = len(chain)
        bestSeed = i

print bestSeed
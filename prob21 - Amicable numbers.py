#!/usr/bin/python

#Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
#If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#Evaluate the sum of all the amicable numbers under 10000.

def mkfactorlist(bignumber):
    factorlist = set([1])
    
    for i in range(2,int(floor(sqrt(bignumber))+1)):
        if bignumber % i == 0:
            factorlist.update([i,bignumber/i])
        
    return factorlist

my_dict = {i : sum(mkfactorlist(i)) for i in range(1,10001)}

numlist = set([])

for key in my_dict:
    if my_dict[key] in my_dict:
        if key == my_dict[my_dict[key]]:
            numlist.update([key, my_dict[key]])

print sum(numlist)
#!/usr/bin/python

#If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used? 
#
#NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

numbers = {
    0 : '',
    1 : 'one',
    2 : 'two',
    3 : 'three',
    4 : 'four',
    5 : 'five',
    6 : 'six',
    7 : 'seven',
    8 : 'eight',
    9 : 'nine',
    10 : 'ten',
    11 : 'eleven',
    12 : 'twelve',
    13 : 'thirteen',
    14 : 'fourteen',
    15 : 'fifteen',
    16 : 'sixteen',
    17 : 'seventeen',
    18 : 'eighteen',
    19 : 'nineteen',
    20 : 'twenty',
    30 : 'thirty',
    40 : 'forty',
    50 : 'fifty',
    60 : 'sixty',
    70 : 'seventy',
    80 : 'eighty',
    90 : 'ninety'}

def printname(number):
    name = str()
    numstrlist = list(str(number))
    while len(numstrlist) < 4:
        numstrlist.insert(0,'0')
    numlist = [int(i) for i in numstrlist]
    if numlist[0] > 0:
        name += numbers[numlist[0]] + 'thousand'
    if numlist[1] > 0:
        name += numbers[numlist[1]] + 'hundred'
    lastnum = int(numstrlist[2]+numstrlist[3])
    if lastnum > 0:
        if numlist[0] + numlist[1] > 0:
            name += 'and'
        if lastnum < 21:
            name += numbers[lastnum]
        else:
            name += numbers[lastnum-lastnum%10] + numbers[lastnum%10]
    return name

words = [printname(i) for i in range(1,10001)]
fullstr = ''.join(words)

print len(fullstr)
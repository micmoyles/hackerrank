#!/usr/bin/python
'''
https://www.hackerrank.com/challenges/special-palindrome-again/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
'''

from palin import getSubStrings
import math



def isSpecial(s):
	'''
	Special string if 
	1) length = 1
	2) all chars are the same
	3) all chars the same expect for middle
	'''

	# case 1)
	if len(s) == 1:
		return True
	# case 2)
	elif len(set(s)) == 1:
		return True
	elif len(s) % 2 == 0:
		return False
	else:
		middleIndex = int(math.floor(len(s)/2.0)) 
		newString = s[:middleIndex]+s[middleIndex+1:]
		if len(set(newString)) == 1:
			return True
	return False



def substrCount(s):
	count = 0
	substrings = getSubStrings(s,unique = False)
	for s in substrings:
		#print s, isSpecial(s)
		if isSpecial(s): count+=1
	print count

f = open('specialPalindromeInput02.txt')
data = f.read()
f.close()
#substrCount(data.strip('\n'))
substrings = getSubStrings(data.strip('\n'))
print len(substrings)
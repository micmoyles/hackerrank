#!/usr/bin/python 

'''
An integer P is a whole square if it is a square of some integer
Q; i.e. if P = Q .
Write a function:
def solution(A, B)
that, given two integers A and B, returns the number of whole
squares within the interval [A..B] (both ends included).
'''
import math

def solution(A,B):

	count = math.ceil(math.sqrt(B)) - math.floor(math.sqrt(A)) - 1
	if math.sqrt(A) % 1 == 0:
		count+=1
	if math.sqrt(B) % 1 == 0:
		count+=1
	return count

print solution(9,49)
#!/usr/bin/python 

'''
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
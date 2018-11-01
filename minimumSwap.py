#!/usr/bin/python
'''
https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

problem test cases are wrong
a constraint is that arr[i] < len(arr) 
but this is not reflected in test cases 

'''

def swap(arr,index1,index2):
	newIndex1 = arr[index2]
	newIndex2 = arr[index1]

	arr[index1] = newIndex1
	arr[index2] = newIndex2
	return arr

def minimumSwaps(arr):
	# construct hash
	arrhash   = {}
	swapCount = 0
	print arr

	for i in xrange(0,len(arr)):
		arrhash[arr[i]] = i
	
	print arrhash

	for i in xrange(0,len(arr) - 1):
		print('i = %d' % i)
		index = arrhash.get(i+1)
		print('index = %d' % index)
		if i == index:
			continue
		arr = swap(arr,i,index)
		print arr
		swapCount+=1
	print('Number of swaps = %d' % swapCount)

A = [5,7,3,1,4,6,2]
A = [1,3,5,2,4,6,8]
minimumSwaps(A) 
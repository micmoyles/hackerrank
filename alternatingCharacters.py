#!/usr/bin/python
'''
https://www.hackerrank.com/challenges/alternating-characters/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
You are given a string containing characters and only. Your task is to change it into a string such that there are no matching adjacent characters. To do this, you are allowed to delete zero or more characters in the string.

Your task is to find the minimum number of required deletions.

For example, given the string , remove an at positions and to make in deletions
'''

s = 'AABBABAB'
s = 'AAAA'
s = 'AAABBB'

def alternatingCharacters(s):
	count = i = 0
	while i < len(s) - 1:
		j = i+1
		print('Comparing element %d - %s and %d - %s' % (i,s[i],j,s[j]))
		while s[i] == s[j]:
			print('remove')
			count+=1
			j+=1
			if j >= len(s): break

		i = j
	return count
print alternatingCharacters(s)
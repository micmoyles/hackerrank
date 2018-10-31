#!/usr/bin/python
'''
https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
Sherlock considers a string to be valid if all characters 
of the string appear the same number of times.
It is also valid if he can remove just 1 character at 1 index 
in the string, 
and the remaining characters will occur the same number of times. 
Given a string S, determine if it is valid. 
If so, return YES, otherwise return NO.
'''
def isValid(S):
	print S
	countMap = {}
	for s in set(S):
		countMap[s] = S.count(s)
	print countMap
	print countMap.keys()
	print countMap.values()

	values = countMap.values()
	# if set contains one element, all counts are the same so return YES
	if len(set(values)) == 1:
		return 'YES'
	# if there are more than two differing counts the string cannot be valid
	elif len(set(values)) > 2:
		return 'NO'

	# exactly two counts
	else:
		# if either counts are 1 the string is valid as we can remove it
		v = list(set(values))
		if values.count(1) == 1:
			return 'YES'
		vals = values
		if (vals.count(v[0]) == 1 or vals.count(v[1]) == 1) and abs(v[0] - v[1]) == 1:
			return 'YES'
		return 'NO'
		
# expect YES
print isValid('ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd')
# expect NO
print isValid('aabbcd')
# expect NO
print isValid('aabbccddeefghi')
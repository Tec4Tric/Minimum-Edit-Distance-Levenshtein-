# Minimum Edit Distance using Levenshtein formula
# Algorithm by Dan Jurafsky
# Implemented by Sayan De


# Input your Strings
str1="Intension"
str2="Execution"

def med(str1,str2,len_str1,len_str2):
	if len_str1 == 0:
		return len_str2
	if len_str2 == 0:
		return len_str1
	if str1[len_str1-1] == str2[len_str2-1]:
		return med(str1,str2,len_str1-1,len_str2-1)
	return min(med(str1,str2,len_str1,len_str2-1) + 1, med(str1,str2,len_str1-1,len_str2) + 1, med(str1,str2,len_str1-1,len_str2-1) + (2 if str1[len_str1] !=str2[len_str1] else 0))

print(med(str1,str2,len(str1),len(str2)))

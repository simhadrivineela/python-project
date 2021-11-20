def ispalindrome(s):
	return s==s[::-1]
s="mom"
ans=ispalindrome(s)
if ans :
	print("palindrome")
else:
	print("not a palindrome")
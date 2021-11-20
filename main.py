def ispalindrome(s):
	return s==s[::-1]
s="mom"
ans=ispalindrome(s)
if ans :
	print("pal")
else:
	print("not a palindrome")
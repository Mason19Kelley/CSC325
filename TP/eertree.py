

class Eertree:


	def __init__(self, palindrome: str):
		# creates graph based on input string
		self.eertree = self.construct(palindrome)

	# builds stucture
	def construct(self, palindrome):
		if self.checkPalindrome(palindrome) == False:
			print("That is not a palindrome!")
			del self
			return
		print('accepted')



	# checks if inputted string is a palindrome
	def checkPalindrome(self, string):
		if len(string) == 1:
			return True
		if len(string) == 2:
			if string[0] == string[1]:
				return True
			return False
		n = len(string) - 1
		for i in range(n//2):
			if string[i] != string[n-i]:
				return False
		return True

e = Eertree('eertree')


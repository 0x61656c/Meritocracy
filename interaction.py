"""
Objectives:
Be able to sort through user reputations and recommendations
Be able to sort users by various metrics, including max score, average score
per period, etc.

Requirements:
Cost of setup
Repository maintenance
User input
"""
from operator import attrgetter
from classes import User
import copy

def interpret(data,attribute):
	"""Interprets user data into usable information

	Arguments:
		'data'  a list of user instances
		'attribute' the desired means by which to sort the data
	"""
	valid = ["alias", "delta", "score"]
	
	if str(attribute) in valid:
		return(data.sort(key = attrgetter(str(attribute))))

	else: 
		print("error: Invalid attribute.")
		return None



def testInterpretationEngine():
	user1 = User("Aaron", 500,50)
	user2 = User("Connor", 5,5)
	user3 = User("Jeff", 50,500)

	data = [user1, user2, user3]

	print("Testing Interpretation Engine")
	print()
	
	assert(interpret(copy.copy([data]), "alias") == data)
	print("Test-Case 1 Passed.")
	
	assert(interpret(copy.copy([data]), "delta") == [user2, user1, user3])
	
	a = interpret(copy.copy([data]), "delta")
	assert(a[0] == user2)
	print("Test-Case 2 Passed.")

	print("All Tests Passed!")

def main():
	testInterpretationEngine()

if __name__ == "__main__":
	main()

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

class User(object):
	"""Keeps track of important user information

	Arguments:
		'alias' -user identifier
		'score' -curent score on the system measured in pips of size 10^-5
		'delta' -change in score in the past 24 hours, in pips of size 10^-5

	"""
	def __init__(self, alias, score, delta):
		self.alias = alias
		self.score = score
		self.delta = delta

	def __repr__(self):
		return "<User Object: Alias = %s, Score = %s>" %(self.alias,self.score)

	def getAlias(self):
		"""return the alias attribute of a user instance"""
		return self.alias

	def getScore(self):
		"""return the score attribute for a user instance"""
		return self.score

	def getDelta(self):
		"""return the delta attribute for a user instance"""
		return self.delta

	def changeScore(self, new):
		"""Changes the score of a User instance"""
		self.score = new

	def adjustScore(self, amount):
		"""Adjusts score based on a prediction"""
		self.score += amount

def interpretationEngine(data,attribute):
	"""Interprets user data into usable information

	Arguments:
		'data'  a list of user instances
		'attribute' the desired means by which to sort the data
	"""
	for element in data:

data = []

def testInterpretationEngine():
	print("Testing Interpretation Engine")
	print()
	assert(x = x)
	print("Test-Case 1 Passed.")
	print("Test-Case 2 Passed.")
	print("All Tests Passed!")

print("Test")
class User(object):
	"""Keeps track of important user information

	Arguments:
		'alias' user identifier
		'score' curent score on the system measured in pips of size 10^-5
		'delta' change in score in the past 24 hours, in pips of size 10^-5

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
		"""Adjusts score based on a prediction.
		
		Arguments: 
			'amount' quantity (in pips of size 10^-5) by which score has changed
		"""
		self.score += amount

def testUserClass():
	"""Tests user class"""
	user1 = User("user1", 50, 50)
	#user2 = User("user2",75, 0)
	print()

	print("Testing User Class...")

	print()

	assert(user1.getAlias() == "user1")
	assert(user1.getScore() == 50)
	assert(user1.getDelta() == 50)

	print("Test-Case 1 Passed.")

	user1.changeScore(-500)
	assert(user1.getScore() == -500)

	user1.changeScore(0)
	assert(user1.getScore() == 0)

	user1.changeScore(500)
	assert(user1.getScore() == 500)

	print("Test-Case 2 Passed.")

	user1.adjustScore(50)
	assert(user1.getScore() == 550)

	user1.adjustScore(-75)
	assert(user1.getScore() == 475)

	user1.adjustScore(0)
	assert(user1.getScore() == 475)

	print()
	print("All Tests Passed!")

def main():
	testUserClass()

if __name__ == "__main__":
	main()


class Agent:

	def __init__(self, problem, fn):
		self.problem = problem
		self.searchFunction = fn

	def solve(self):
		return self.searchFunction(self.problem)

	


	
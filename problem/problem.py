class Problem():

	def __init__(self, startState):
		self.startState = startState

	def getStartState(self):
		return self.startState

	def getSuccessors(self, state):
		successors = []
		possibleActions=state.get_possible_actions()
		for action in possibleActions:
			nextState=state.get_succesor(action)
			cost=0
			successors.append((nextState, action, cost) )
		return successors

	def isGoalState(self, state):
		return state.board.isSolved()

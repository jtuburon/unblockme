import copy


class GameState:

	def __init__(self, board):
		self.board=board

	def __str__(self):
		return str(self.board)

	def get_possible_actions(self):
		return self.board.get_possible_actions()

	def get_succesor(self, action):
		blockID= action[0]
		offset= action[2]

		nextState= copy.deepcopy(self)
		block= nextState.board.blocksMap[blockID]
		block.move(offset)
		return nextState

	def get_predecessor(self, action):
		blockID= action[0]
		offset= action[2]

		nextState= copy.deepcopy(self)
		block= nextState.board.blocksMap[blockID]
		block.move(-1*offset)
		return nextState
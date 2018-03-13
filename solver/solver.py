from models.board import *
from models.block import *

from problem.gamestate import *
from problem.problem import *
from problem.agent import *

class Solver:
	def __init__(self, puzzle_path, method):
		self.puzzle_path = puzzle_path
		self.method = method
		self._init_problem()

	def _init_board(self):
		board= Board()
		f= file(self.puzzle_path)
		blocks_lines=f.readlines() 
		for index, line in enumerate(blocks_lines):
			values= line.replace("\n", "").split(",")
			orientation = Block.HORIZONTAL_ORIENTATION if values[0] == 'H' else Block.VERTICAL_ORIENTATION
			size=int(values[1])
			row=int(values[2])
			col=int(values[3])
			objetive= True if index==0 else False
			block= Block(orientation, size, row, col, objetive)
			board.add_block(block)
		return board

	def _init_problem(self):
		board= self._init_board()
		startState = GameState(board)
		currentGameState= startState

		self.problem= Problem(startState)

	def solve(self):
		agent= Agent(self.problem, self.method)
		return agent.solve()

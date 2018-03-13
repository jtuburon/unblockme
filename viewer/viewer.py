import sys, pygame
import time
from models.block import *


class SolutionViewer:
	def __init__(self, startState, solution, auto_play=False):
		pygame.init()
		self.auto_play=auto_play
		self.actions = solution[1]
		self.total_actions= len(self.actions)
		self.currentGameState= startState
		self.board= startState.board
		self._init_board()
		self.render_solution()

	def _init_board(self):
		size = width, height = 360, 385
		self.screen = pygame.display.set_mode(size)

		self.block_margin=5
		self.white=(255,255,255)
		self.blue=(0,0,255)
		self.red=(255,0,0)

		self.font = pygame.font.SysFont("comicsansms", 12)
		
		self.block_unit_size=60

		self.actionIndex=0

	def drawGameState(self):
		self.screen.fill(self.white)	
		for block in self.currentGameState.board.blocks:
			block_width=50
			block_height=50
			if block.orientation==Block.HORIZONTAL_ORIENTATION:
				block_width=self.block_unit_size* block.size - 2*self.block_margin
			elif block.orientation==Block.VERTICAL_ORIENTATION:
				block_height=self.block_unit_size* block.size - 2*self.block_margin
			block_color= self.red if block.objective else self.blue
			pygame.draw.rect(self.screen,block_color,(block.col* self.block_unit_size+self.block_margin, block.row*self.block_unit_size+self.block_margin,block_width,block_height))
		text = self.font.render("Action No: "+ str(self.actionIndex)+ " of "+str(self.total_actions), True, (255, 0, 0))
		textX=(360 - text.get_width())//2
		self.screen.blit(text, (textX, 365))
		pygame.display.flip()


	def apply_action(self):
		self.currentGameState= self.currentGameState.get_succesor(self.actions[self.actionIndex])
		
	def revert_action(self):
		self.currentGameState= self.currentGameState.get_predecessor(self.actions[self.actionIndex])

	def render_solution(self):
		running = True
		self.drawGameState()

		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT: sys.exit()

			time.sleep(0.01)
			if self.auto_play:
				if self.actionIndex < self.total_actions:
					self.apply_action()
					self.actionIndex+=1
					self.drawGameState()
				pygame.time.delay(60)
			else:
				for event in pygame.event.get():
					if event.type == pygame.QUIT: sys.exit()
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_LEFT:
							if self.actionIndex>0:
								self.actionIndex -= 1
								self.revert_action()
								self.drawGameState()
						if event.key == pygame.K_RIGHT:
							if self.actionIndex < self.total_actions:
								self.apply_action()
								self.actionIndex += 1
								self.drawGameState()
			
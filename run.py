from models.board import *
from models.block import *

from problem.gamestate import *
from problem.problem import *
from problem.agent import *

import sys, pygame
import time

pygame.init()

board= Board();
board.init_board02()

startState = GameState(board)
currentGameState= startState

problem= Problem(startState)
agent= Agent(problem)
solution =agent.solve()

print "SOLVED"
actions = solution[1]
total_actions= len(actions)

size = width, height = 360, 385
screen = pygame.display.set_mode(size)

block_margin=5
white=(255,255,255)
blue=(0,0,255)
red=(255,0,0)

font = pygame.font.SysFont("comicsansms", 12)
text = font.render("Hello, World", True, (0, 128, 0))

block_unit_size=60

actionIndex=0

def drawGameState():
	screen.fill(white)	
	board= currentGameState.board
	for block in board.blocks:
		block_width=50
		block_height=50
		if block.orientation==Block.HORIZONTAL_ORIENTATION:
			block_width=block_unit_size* block.size - 2*block_margin
		elif block.orientation==Block.VERTICAL_ORIENTATION:
			block_height=block_unit_size* block.size - 2*block_margin
		block_color= red if block.objective else blue
		pygame.draw.rect(screen,block_color,(block.col* block_unit_size+block_margin, block.row*block_unit_size+block_margin,block_width,block_height))
	text = font.render("Action No: "+ str(actionIndex)+ " de "+str(total_actions), True, (255, 0, 0))
	textX=(360 - text.get_width())//2
	screen.blit(text, (textX, 365))
	pygame.display.flip()


def apply_action():
	global currentGameState
	currentGameState= currentGameState.get_succesor(actions[actionIndex])

def revert_action():
	global currentGameState
	currentGameState= currentGameState.get_predecessor(actions[actionIndex])

running = True
drawGameState()

while running:

	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				if actionIndex>0:
					print "Back"
					actionIndex -= 1
					revert_action()
					drawGameState()
			if event.key == pygame.K_RIGHT:
				if actionIndex < total_actions:
					print "Next"
					apply_action()
					actionIndex += 1
					drawGameState()
	time.sleep(0.01)

	# if actionIndex < total_actions:
	# 	apply_action()
	# 	actionIndex+=1
	# 	drawGameState()
	# pygame.time.delay(60)
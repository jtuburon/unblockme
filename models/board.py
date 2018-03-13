from block import *

class Board:
	EMPTY_SPACE="."
	def __init__(self, width=6, height=6):
		self.width= width;
		self.height= height;
		self.block_count=0;
		self.blocks=[]
		self.blocksMap={}
		self.objectiveBlock=None

	def isSolved(self):
		return True if self.objectiveBlock.row==2 and self.objectiveBlock.col==4  else False
		
	def _validate_block(self, block):
		if block.orientation==Block.HORIZONTAL_ORIENTATION:
			if block.col+block.size>self.width:
				return False
		if block.orientation==Block.VERTICAL_ORIENTATION:
			if block.row+block.size>self.height:
				return False
		valid=True;
		
		busy_positions=[]
		for b in self.blocks:
			busy_positions+= b.get_positions() 

		new_block_positions= block.get_positions()
		intersection = [p for p in new_block_positions if p in busy_positions]
		return len(intersection)==0


	def add_block(self, block):
		if self._validate_block(block):
			self.blocks.append(block)
			if block.objective:
				block.id="B0"
				self.objectiveBlock=block
			else:
				self.block_count+=1
				block.id="B"+str(self.block_count)
			self.blocksMap[block.id]=block
		else:
			print "This block cant be added"

	def _validate_movement(self, block, offset):
		if block.orientation==Block.HORIZONTAL_ORIENTATION:
			col_pos_ini= block.col+offset
			col_pos_end= col_pos_ini+ block.size
			if col_pos_end>self.width or col_pos_ini<0:
				return False
			

		if block.orientation==Block.VERTICAL_ORIENTATION:
			row_pos_ini= block.row+offset
			row_pos_end= row_pos_ini + block.size
			
			if row_pos_end>self.height or row_pos_ini<0:
				return False

		other_blocks=[]
		for b in self.blocks:
			if b!=block:
				other_blocks.append(b)

		busy_positions=[]
		for b in other_blocks:
			busy_positions+= b.get_positions() 

		block_positions= block.get_positions()
		new_block_positions=[]
		for p in block_positions:
			if block.orientation==Block.HORIZONTAL_ORIENTATION:
				np=(p[0], p[1]+offset)
				new_block_positions.append(np)
			else:
				np=(p[0]+offset, p[1])
				new_block_positions.append(np)
		

		intersection = [p for p in new_block_positions if p in busy_positions]

		valid=len(intersection)==0
		return valid

	def get_possible_actions(self):
		possible_actions=[]
		for block in self.blocks:
			offset=1
			while(offset<=6 and self._validate_movement(block, offset)):
				action =(block.id, block.orientation, offset)
				possible_actions.append(action)
				offset+=1
			offset=1
			while(offset<=6 and self._validate_movement(block, -1 * offset)):
				action =(block.id, block.orientation, -1 * offset)
				possible_actions.append(action)
				offset+=1
		return possible_actions



	def __str__(self):
		board=[[Board.EMPTY_SPACE for i in range(self.height)] for j in range(self.width)]
		for block in self.blocks:
			for offset in range(block.size):
				if block.orientation==Block.HORIZONTAL_ORIENTATION:
					board[block.row][block.col+offset]=block.id
				elif block.orientation==Block.VERTICAL_ORIENTATION:
					board[block.row+offset][block.col]=block.id

		data=""
		for i in range(self.height):
			data+= "\t".join(board[i]) +"\n"
		return data


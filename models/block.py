import copy

class Block():
	HORIZONTAL_ORIENTATION="H"
	VERTICAL_ORIENTATION="V"

	def __init__(self, orientation, size, row, col, objective=False):
		self.id= None;
		self.orientation= orientation;
		self.size= size;
		self.row= row;
		self.col= col;
		self.objective= objective;

	def __str__(self):
		return self.id
	
	def get_positions(self):
		positions=[]
		for i in range(self.size):
			if self.orientation==Block.HORIZONTAL_ORIENTATION:
				p=(self.row, self.col + i)
			else:
				p=(self.row +i , self.col)
			positions.append(p)
		return positions

	def move(self, offset):
		if self.orientation==Block.HORIZONTAL_ORIENTATION:
			self.col+=offset
		else:
			self.row+=offset


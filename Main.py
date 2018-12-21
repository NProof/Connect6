# from enum import Enum

# class Direction(Enum)
	# A = 0
	# B = 1
	# C = 2
	# D = 3

class Point:
	def __init__(self, value):
		self.val = value
		
	adj = None
	val = None
	
class Board:
	def __init__(self, n):
		self.body = [[None for j in range(n)] for i in range(n)]
		self.n = 0
		
	def show(self):
		# print(' n : ' + self.body)
		print(' body : ')
		for row in self.body:
			for point in row:
				if point == None:
					print('[ ]', end='')
				else:
					print(' ' + ( 'o' if point.val else 'x' ) + ' ', end='')
			print()
		print(' --- ')
		
	def ins(self, pos, turn):
		self.n += 1
		self.body[pos[0]][pos[1]] = Point(turn)
		
	def rem(self, pos):
		self.n -= 1
		tmp = self.body[pos[0]][pos[1]]
		self.body[pos[0]][pos[1]] = None
		return tmp
		
	# body = None
	
class Rule:
	pass
	
class RuleBoard(Board):
	def __init__(self, n, rule = None):
		super().__init__(n)
		self.connect6 = False
		self.options = set([(i, j) for j in range(n) for i in range(n)])
		
	def mov(self, pos, turn):
		super().ins(pos, turn)
		self.options.remove(pos)
		connect6 = False
		if connect6:
			self.connect6 = True
		
	def over(self):
		return self.connect6 or len(self.options) < 1 or self.n >= 361
		
	# options = None
	# connect6 = None
	
class Player:
	# def __init__(self, algorithm):
		# self.alg = algorithm
		
	def gen(self, number, board):
		if self.last != None:
			tmp = self.last
			self.last = None
			return tmp
		if number == 2:
			oneOrTwo = self.select(2, board.options)
			if len(oneOrTwo) == 2:
				last = oneOrTwo[1]
				return oneOrTwo[0]
		return self.select(1, board.options)
		
	def select(self, number, options):
		if number == 1:
			return next(iter(options))
		else:
			return list(set([next(iter(options)), next(iter(options))]))
	
	last = None
	alg = None
	
if __name__ == '__main__' :
	board = RuleBoard(19)
	plys = {True:Player(), False:Player()} # dict
	turn = True
	leave = 1
	while( True ):
		over = board.over()
		while ( not over ) and leave > 0:
			print(' 1 : ' + str(leave) + ', turn : ' + str(turn))
			board.show()
			pos = plys.get(turn).gen(leave, board)
			board.mov(pos, turn)
			leave = leave - 1
			over = board.over()
		if(over):
			break
		turn = not turn
		leave = 2
		
	board.show()
	if board.connect6:
		print( ('first' if turn else 'second') + ' player is the winner.')
	else:
		print(' The Game is Draw')
	
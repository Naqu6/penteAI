import os
import time
import copy

AI_POSITION = True
PLAYER_POSITION = False

class Ai:

	outcomes = []

	def __init__(self,game):
		self.game = game
		self.lookingAt = AI_POSITION

	def isPosMine(self, x,y):
		if x<0 or y<0 or x>=len(self.board) or y>=len(self.board): return False
		if self.board[y][x] == self.lookingAt: return True
		return False		

	def isPosTheirs(self,x,y):
		if x<0 or y<0 or x>=len(self.board) or y>=len(self.board): return False	
		if self.board[y][x] == (not self.lookingAt): return True
		return False

	def findConsecutiveVertical(self,x,y):
		score = 0
		for i in range(5):
			y+=1
			if self.isPosTheirs(x,y): return 0
			if self.isPosMine(x,y): score+=1
		return score

	def findConsecutiveHorizontal(self,x,y):
		score = 0
		for i in range(5):
			x+=1
			if self.isPosTheirs(x,y): return 0
			if self.isPosMine(x,y): score+=1
		return score



	def findConsecutiveDiagonalRight(self,x,y):
		score = 0
		for i in range(5):
			x+=1
			y+=1
			if self.isPosTheirs(x,y): return 0
			if self.isPosMine(x,y): score+=1
		return score
	
	def findConsecutiveDiagonalLeft(self,x,y):
		score = 0
		for i in range(5):
			x-=1
			y+=1
			if self.isPosTheirs(x,y): return 0
			if self.isPosMine(x,y): score+=1
		return score
				
	positionFunctions = [findConsecutiveVertical,findConsecutiveHorizontal,findConsecutiveDiagonalRight,findConsecutiveDiagonalLeft]

	def getConsecutive(self):
		points = {}
		for i in range(len(self.board)):
			for j in range(len(self.board[i])):
				for positionFunction in self.positionFunctions:
					score = positionFunction(self,i,j)
					if score>0:
						if score not in points: points[score] = 1
						else: points[score] += 1
				
		return points
	def valueGameState(self,coords):
		
		self.board = self.game.board
		self.board[coords[0]][coords[1]] = True

		consecutive = self.getConsecutive()
		self.game.board[coords[0]][coords[1]] = None

		return consecutive


	def generateMoves(self,board):
		coords = []
		for i in range(len(board)):
			for j in range(len(board)):
				if board[i][j] == None: 
					coords.append((i,j))  

		return coords

#	def getMaxKey(self,score):
#
#		return (max(score.keys()),score[max(score.keys())])


	def compareScores(self,score,highScore):
		return score>highScore

	def getScore(self,scores):
		score = 0
		for number,points in scores.items(): 
			score+= 4**number*points
		return score

	def getBestMove(self,board,movingYou):
		moves = self.generateMoves(board)
		bestMove = (None,-float("inf"))
		for move in moves:
			self.lookingAt =movingYou==AI_POSITION
			score = self.getScore(self.valueGameState(move))
			self.lookingAt = movingYou==PLAYER_POSITION
			score -= 1.5*self.getScore(self.valueGameState(move))
			if self.compareScores(score,bestMove[1]):
				bestMove = (move,score)
		
		return bestMove
	
	def thinkDownTree(self, board, stepsRemaining,personMoving=AI_POSITION):
		
		if stepsRemaining > 1:
			moves = self.generateMoves(board)
			for move in moves:
				myBoard = board
				myBoard[move[0]][move[1]] = personMoving
				self.thinkDownTree(myBoard,stepsRemaining-1,personMoving=(not personMoving))
		else:
			self.outcomes.append(self.getBestMove(board,personMoving))
							
		#else: 
	
	def makeMove(self):
		self.outcomes = []
		self.thinkDownTree(self.game.board,2)
		bestMove = (None,-float("inf"))
		for move in self.outcomes:
			if move[1] > bestMove[1]:
				bestMove=move
		return bestMove[0]

			
		

# class PenteGame:

# 	def __init__(self,game_size=15):
# 		self.gameSize = game_size
# 		self.board = [[None for i in range(self.gameSize)] for i in range(self.gameSize)]
# 		self.over = False
# 		self.ai = Ai(self)		


# 	def printBoard(self):
# 		os.system('clear')
# 		for i in range(self.gameSize):
# 			for j in range(self.gameSize):
# 				if self.board[i][j] == None: 
# 					if self.gameSize/2-.5 == i == j: print("*",end=" ")
# 					else:print("+",end=" ")
				
# 				elif self.board[i][j] == False: print("X",end=" ")
# 				else: print("O",end=" ")
# 			print("") 

# 	def moveCheck(self):
# 		pass	

# 	def makeMove(self,x,y):
# 		self.board[y][x] = False
# 		self.moveCheck()
# 		self.printBoard()

# 	def checkInput(self,input):
# 		try:
# 			input[0] = int(input[0])
# 			input[1] = int(input[1])
# 		except TypeError:
# 			print("Please Enter a corrert Position")			

# 	def makeAiMove(self,coords):
#                 self.board[coords[0]][coords[1]] = True
#                 self.moveCheck()
#                 self.printBoard()


# 	def gameLoop(self):
# 		self.printBoard()
# 		while self.over == False:
# 			move = input("Please enter your move in the format x y:").split()
		
# 			self.checkInput(move)
# 			self.makeMove(move[0],move[1])
# 			self.makeAiMove(self.ai.makeMove())
					

# # game=PenteGame()

# # game.gameLoop()
# import os
# import time
# import copy


class PenteGame:

	def __init__(self,game_size=15):
		self.gameSize = game_size
		self.board = [[None for i in range(self.gameSize)] for i in range(self.gameSize)]
		self.over = False
		self.ai = Ai(self)		


	def printBoard(self):
		os.system('clear')
		for i in range(self.gameSize):
			for j in range(self.gameSize):
				if self.board[i][j] == None: 
					if self.gameSize/2-.5 == i == j: print("*",end=" ")
					else:print("+",end=" ")
				
				elif self.board[i][j] == False: print("X",end=" ")
				else: print("O",end=" ")
			print("") 

	def moveCheck(self):
		pass	

	def makeMove(self,x,y):
		self.board[y][x] = False
		self.moveCheck()
		self.printBoard()

	def checkInput(self,input):
		try:
			input[0] = int(input[0])
			input[1] = int(input[1])
		except TypeError:
			print("Please Enter a corrert Position")			

	def makeAiMove(self,coords):
                self.board[coords[0]][coords[1]] = True
                self.moveCheck()
                self.printBoard()


	def gameLoop(self):
		self.printBoard()
		while self.over == False:
			move = input("Please enter your move in the format x y:").split()
		
			self.checkInput(move)
			self.makeMove(move[0],move[1])
			self.makeAiMove(self.ai.makeMove())
					

game=PenteGame()

game.gameLoop()



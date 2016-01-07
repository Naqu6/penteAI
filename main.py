import os
import time


class Ai:
	def __init__(self,game):
		self.game = game

	def isPosMine(self, x,y):
		if x<0 or y<0 or x>=len(self.game.board) or y>=len(self.game.board): return False
		if self.game.board[y][x] == True: return True
		return False		

	def isPosTheirs(self,x,y):
		if x<0 or y<0 or x>=len(self.game.board) or y>=len(self.game.board): return False	
		if self.game.board[y][x] == False: return True
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
				
	
	def getConsecutive(self):
		points = []
		for i in range(len(self.game.board)):
			for j in range(len(self.game.board[i])):
				points.append(self.findConsecutiveVertical(i,j))		
				points.append(self.findConsecutiveHorizontal(i,j))
				points.append(self.findConsecutiveDiagonalRight(i,j))
				points.append(self.findConsecutiveDiagonalLeft(i,j))

		return points
	def valueGameState(self):
		self.board = self.game.board
		print(self.getConsecutive())
		

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

	def makeAiMove(self,x,y):
                self.board[y][x] = True
                self.moveCheck()
                self.printBoard()


	def gameLoop(self):
		self.printBoard()
		while self.over == False:
			move = input("Please enter your move in the format x y:").split()
			aiMove = input("Ai Move").split()
			self.checkInput(move)
			self.checkInput(aiMove)
			self.makeMove(move[0],move[1])
			self.makeAiMove(aiMove[0],aiMove[1])
			print(self.ai.valueGameState())
					

game=PenteGame()

game.gameLoop()

import os


class PenteGame:
	gameSize = 0
	board = []

	def __init__(self,game_size=13):
		self.gameSize = game_size
		self.board = [[None]*self.gameSize]*self.gameSize
		


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

	def makeMove(self,x,y):
		self.printBoard()

game=PenteGame()
game.makeMove(0,0)

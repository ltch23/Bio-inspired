import sys
from Snake import *
from Qlearning import *

mal_direc = {0: 2, 1: 3, 2: 0, 3: 1}

class Game:

	def __init__(self, width=300, height=200):
		self.game_over = False
		self.screenHeight = height
		self.screenWidth = width
		self.player = Snake()
		self.objetivo()

	def objetivo(self):
		height = self.screenHeight
		width = self.screenWidth
		self.pos_objetivo = [np.random.randint(0,width),
							np.random.randint(0,height)]
	#print("food: ", self.pos_objetivo)

	def revisar(self):
		pos_objetivo = self.player.pos[0]
		height = self.screenHeight
		width = self.screenWidth
		if pos_objetivo[0] < 0 or pos_objetivo[0] > width:
			self.game_over = True
		if pos_objetivo[1] < 0 or pos_objetivo[1] > height:
			self.game_over = True
		if len(np.unique(self.player.pos,axis=0)) != len(self.player.pos):
			self.game_over = True

		if pos_objetivo == self.pos_objetivo:
			print("encontre")
			sys.exit(0)

		return False

	def jugar(self):
		cur = 1
		it = 1
		ql = Qlearning()

		while True:
			self.dist_prev = -1
			self.player.__init__()
			print("intento: ",cur)
			while not self.game_over:
				pred=ql.predecir(self.get_estado())
				if mal_direc[self.player.direcc] == pred:
					self.game_over = True
				else:
					self.player.direcc = pred
					self.player.mover()
					ql.actualizar(self.get_premio(), self.get_estado())

				if self.revisar():
					ql.actualizar(10, self.get_estado())
					self.dist_prev = -1

				it+=1

			print("iteration: ",it)
			#no perder avance
			ql.actualizar(-10, self.get_estado())
			self.game_over = False
			#print('Game over')
			cur += 1

	def get_estado(self):
		pobj = self.pos_objetivo
		p_player0 = self.player.pos[0]
		pplayer = self.player.pos
		return (pobj[0] <= p_player0[0],
		pobj[1] >= p_player0[1],
		pobj[0] == p_player0[0],
		pobj[1] == p_player0[1],
		self.player.direcc,
		[pobj[0] - 1, pobj[1]] in pplayer,
		[pobj[0] + 1, pobj[1]] in pplayer,
		[pobj[0], pobj[1] - 1] in pplayer,
		[pobj[0], pobj[1] + 1] in pplayer)

	def get_premio(self):
		x = self.pos_objetivo
		y = self.player.pos[0]
		dist_actual = abs(x[0] - y[0]) + abs(x[1] - y[1]) + 1
		if self.dist_prev == -1:
			self.dist_prev = dist_actual

		if self.dist_prev < dist_actual:
			rew = -1
		else:
			rew = 1

		self.dist_prev = dist_actual
		#print("rew: ",rew)
		return rew

app = Game(100,100)
app.jugar()

import random


class GamePlayer(object):
    '''Represents the logic for an individual player in the game'''

    def __init__(self, player_id, game):
        '''"player_id" indicates which player is represented (int)
        "game" is a game object with a get_successors function'''
        self.player_id = player_id
        self.game = game
        return

    def evaluate(self, state):
        '''Evaluates a given state for the specified agent
        "state" is a game state object'''
        pass

    def minimax_move(self, state):
        '''Returns a string action representing a move for the agent to make'''
        pass

    def alpha_beta_move(self, state):
        '''Same as minimax_move with alpha-beta pruning'''
        pass


class BasicPlayer(GamePlayer):
    '''A basic agent which takes random (valid) actions'''

    def __init__(self, player_id, game):
        GamePlayer.__init__(self, player_id, game)

    def evaluate(self, state):
        '''This agent doesn't evaluate states, so just return 0'''
        return 0

    def minimax_move(self, state):
        '''Don't perform any game-tree expansions, just pick a random move
            that's available in the list of successors'''
        assert state.player == self.player_id
        successors, actions = self.game.get_successors(state)
        # Take a random successor's action
        return random.choice(actions)

    def alpha_beta_move(self, state, agent):
        '''Just calls minimax_move'''
        return self.minimax_move(state, agentd)

def minimax_dfs(game, state, depth, horizon, eval_fn):
	def maxCalc(game, state, depth, horizon, evaluate):
		if (depth == horizon):
			return evaluate(state), 'z'
		f = []
		succ, act = game.get_successors(state)
		for (s, a) in zip(succ, act):
			b,c = evaluate(s), a
			x = b,c
			f.append(x)
			f.append(minCalc(game, state, depth+1, horizon, evaluate))
		f.sort()
		return f[-1]

	def minCalc(game, state, depth, horizon, evaluate):
		if (depth == horizon):
			return evaluate(state), 'z'
		f = []
		succ, act = game.get_successors(state)
		for (s, a) in zip(succ, act):
			b,c = evaluate(s), a
			x = b,c
			f.append(x)
			f.append(maxCalc(game, state, depth+1, horizon, evaluate))
		f.sort()
		return f[0]

	#def argmax(lst):
		#return lst[0].index(max(lst[0]))
	#a,s = argmax(max(game.get_successors(state), lambda ((a, s)): minCalc(game, state, depth, horizon, eval_fn)))
	#return a,s
	return minCalc(game, state, depth, horizon, eval_fn)

def alphabeta_minimax(game, state, depth, horizon, eval_fn):
	def maxCalc(game, state, alpha, beta, depth, horizon, evaluate):
		if (depth == horizon):
			return evaluate(state), 'z'
		f = []
		succ, act = game.get_successors(state)
		for (s, a) in zip(succ, act):
			b,c = evaluate(s), a
			x = b,c
			f.append(x)
			f.append(minCalc(game, state, alpha, beta, depth+1, horizon, evaluate))
		f.sort()
		temp = f[-1]
		y = temp[0]
		if (y >= beta):
			return temp
		alpha = max(alpha, y)
		return alpha, temp[1]

		'''if (depth == horizon):
			return evaluate(state), 'z'
		succ, act = game.get_successors(state)
		print act
		print 'meow'
		for (s, a) in zip(succ, act):
			alpha = max(alpha, minCalc(game, s, alpha, beta, depth+1, horizon, evaluate))
			x = alpha, a
			if(alpha >= beta):
				return x
		return x'''

	def minCalc(game, state, alpha, beta, depth, horizon, evaluate):
		if (depth == horizon):
			return evaluate(state), 'z'
		f = []
		succ, act = game.get_successors(state)
		for (s, a) in zip(succ, act):
			b,c = evaluate(s), a
			x = b,c
			f.append(x)
			f.append(maxCalc(game, state, alpha, beta, depth+1, horizon, evaluate))
		f.sort()
		temp = f[0]
		y = temp
		if (y <= alpha):
			return temp
		beta = min(beta, y)
		return beta, temp[1]

		'''if (depth == horizon):
			return evaluate(state), 'z'
		succ, act = game.get_successors(state)
		print act
		print 'woof'
		for (s, a) in zip(succ, act):
			beta = min(beta, maxCalc(game, s, alpha, beta, depth+1, horizon, evaluate))
			x = beta, a
			if(alpha >= beta):
				return x
		return x'''

	return minCalc(game, state, -100000000, 100000000, depth, horizon, eval_fn)

def findPos(grid, player_id):
	position = None
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if (grid[i][j] == str(player_id)):
				position = (i, j)
				break
	#assert position is not None, "Current player not found in the provided state"
	return position

def countCookie(grid, position):
	count = 0
	dirs = [(0, -1), (0, 1), (1, 0), (-1, 0), (0, 0)]
	acts = ['n', 's', 'e', 'w', 'z']
	dirs_acts = zip(dirs, acts)
	for d, a in dirs_acts:
		new_position = (position[0] + d[0], position[1] + d[1])
		if new_position[0] < 0 or new_position[0] >= len(grid) or new_position[1] < 0 or new_position[1] >= len(grid[0]):
			continue
		if grid[new_position[0]][new_position[1]] in ['c']:
			count+=1
	return count

class StudentPlayer(GamePlayer):

	def __init__(self, player_id, game):
		GamePlayer.__init__(self, player_id, game)

	def evaluate(self, state):
		playerCurrent = state.player
		otherPlayer = 0
		if (playerCurrent==0):
			otherPlayer = 1
		countCurrent = state.cookiecounts[playerCurrent] * 10
		otherCount = state.cookiecounts[otherPlayer] * 10
		posCurrent = findPos(state.grid, playerCurrent)
		otherPos = findPos(state.grid, otherPlayer)
		countCurrent += countCookie(state.grid, posCurrent)
		otherCount += countCookie(state.grid, otherPos)
		return countCurrent - otherCount + random.randint(0,3)
		raise NotImplementedError()

	def minimax_move(self, state):
		assert state.player == self.player_id
		# Experiment with the value of horizon
		horizon = 6
		val, action = minimax_dfs(self.game, state, 0, horizon, self.evaluate)
		return action

	def alpha_beta_move(self, state):
		assert state.player == self.player_id
		# Experiment with the value of horizon
		horizon = 6
		val, action = alphabeta_minimax(self.game, state, 0, 6, self.evaluate)
		return action
		raise NotImplementedError()

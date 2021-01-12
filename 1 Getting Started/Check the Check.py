def read_board():
	global board, white_king_pos, black_king_pos
	#recebe o tabuleiro
	board = [list(input()) for i in range(8)]
	input()
	#procura pelos reis retornando false caso não encontre-os
	is_empty = True
	for i in range(8):
		for j in range(8):
			if board[i][j] == 'K':
				white_king_pos = [i, j]
			if board[i][j] == 'k':
				black_king_pos = [i, j]
				is_empty = False
	return is_empty

is_in_board = lambda i, j: i >= 0 and i < 8 and j >= 0 and j < 8

is_opposite = lambda p1, p2: (p1.islower() and p2.isupper()) or (p1.isupper() and p2.islower())

directions = {'p': [(1, -1), (1, 1)],
			  'P': [(-1, -1), (-1, 1)],
			  'r': [(0, -1), (0, 1), (-1, 0), (1, 0)],
			  'n': [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, -2), (-1, 2)],
			  'b': [(1, -1), (1, 1), (-1, -1), (-1, 1)],
			  'q': [(1, -1), (1, 1), (-1, -1), (-1, 1), (0, -1), (0, 1), (-1, 0), (1, 0)],
			  'k': [(1, -1), (1, 1), (-1, -1), (-1, 1), (0, -1), (0, 1), (-1, 0), (1, 0)]}

def calc_legal_moves(i, j):
	global legal_moves
	legal_moves = [['.' for k in range(8)] for l in range(8)]
	p = board[i][j] #peça
	pk = p.lower() #chave para buscar em directions
	if p == 'P':
		pk = p
	#peças que se movem uma única casa
	if pk in ['p', 'P', 'k', 'n']:
		for x, y in directions[pk]:
			if is_in_board(i+x, j+y):
				if board[i+x][j+y] == '.' or is_opposite(board[i+x][j+y], p):
					legal_moves[i+x][j+y] = '*'
	#peças podem se mover mais de uma casa
	elif pk != '.':
		for x, y in directions[pk]:
			a, b = i+x, j+y
			while(is_in_board(a, b)):
				if board[a][b] == '.':
					legal_moves[a][b] = '*'
				else:
					if is_opposite(board[a][b], p):
						legal_moves[a][b] = '*'
					break
				a += x
				b += y

def check_the_check():
	for i in range(8):
		for j in range(8):
			calc_legal_moves(i, j)
			if legal_moves[white_king_pos[0]][white_king_pos[1]] == '*':
				return 1
			if legal_moves[black_king_pos[0]][black_king_pos[1]] == '*':
				return 2
	return 0
	
def main():
	game = 1
	while not read_board():
		resp = check_the_check()
		if resp == 1:
			print("Game #"+str(game)+": white king is in check.")
		if resp == 2:
			print("Game #"+str(game)+": black king is in check.")
		if resp == 0:
			print("Game #"+str(game)+": no king is in check.")
		game += 1

if __name__ == '__main__':
	main()
	




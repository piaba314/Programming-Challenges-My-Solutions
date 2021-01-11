def how_many_mines(i, j):
	count = 0
	for di in range(-1, 2):
		for dj in range(-1, 2):
			if i + di >= 0 and i + di < n and j + dj >= 0 and j + dj < m:
				if board[i+di][j+dj] == '*':
					count += 1
	return count

x = 1
while True:
	n, m = map(int, input().split())
	if n == 0 and m == 0:
		break
	
	if x > 1:
		print()
	
	board = [list(input()) for i in range(n)]
	
	print('Field #'+str(x)+':')
	for i in range(n):
		for j in range(m):
			if board[i][j] == '*':
				print('*', end="")
			else:
				print(how_many_mines(i, j), end="")
		print()
	x += 1
	

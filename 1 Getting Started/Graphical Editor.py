from collections import deque

image = []
n = 0
m = 0

def create_image(a, b):
	global image, n, m
	m = a
	n = b
	image = [['O' for i in range(m)] for j in range(n)]

def clear():
	global image
	image = [['O' for i in range(m)] for j in range(n)]

def color(x, y, c):
	image[y-1][x-1] = c

def draw_vertical_segment(x, y1, y2, c):
	if y1 > y2:
		y1, y2 = y2, y1
	for i in range(y1-1, y2):
		image[i][x-1] = c

def draw_horizontal_segment(x1, x2, y, c):
	if x1 > x2:
		x1, x2 = x2, x1
	for i in range(x1-1, x2):
		image[y-1][i] = c

def draw_rectangle(x1, y1, x2, y2, c):
	for i in range(x1-1, x2):
		for j in range(y1-1, y2):
			image[j][i] = c

def write_name(name):
	print(name)
	for i in range(n):
		for j in range(m):
			print(image[i][j], end='')
		print()

def get_neighbors(a, b):
	neighbors = []
	for i in range(-1, 2):
		for j in range(-1, 2):
			if i != 0 or j != 0:
				if a + i >= 0 and a + i < n and b + j >= 0 and b + j < m:
					neighbors.append((a+i, b+ j))
	return neighbors
	
def fill_region(x, y, c):
	q = deque()
	q.append((y-1, x-1))
	last_color = image[y-1][x-1]
	visited = [[0 for i in range(m)] for j in range(n)]
	while q:
		i, j = q.popleft()
		if image[i][j] == last_color and visited[i][j] == 0:
			image[i][j] = c
			visited[i][j] = 1
			q.extend(get_neighbors(i, j))
			
def main():
	while True:
		inp = input().split()
		if inp[0] == 'X':
			break
		
		if inp[0] == 'I':
			create_image(int(inp[1]), int(inp[2]))
		
		if inp[0] == 'C':
			clear()
		
		if inp[0] == 'L':
			color(int(inp[1]), int(inp[2]), inp[3])
		
		if inp[0] == 'V':
			draw_vertical_segment(int(inp[1]), int(inp[2]), int(inp[3]), inp[4])
		
		if inp[0] == 'H':
			draw_horizontal_segment(int(inp[1]), int(inp[2]), int(inp[3]), inp[4])
		
		if inp[0] == 'K':
			draw_rectangle(int(inp[1]), int(inp[2]), int(inp[3]), int(inp[4]), inp[5])
		
		if inp[0] == 'F':
			fill_region(int(inp[1]), int(inp[2]), inp[3])
		
		if inp[0] == 'S':
			write_name(inp[1])

if __name__ == '__main__':
	main()

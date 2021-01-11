def cycle_length(n):
	if n in memo:
		return memo[n]
	if n == 1:
		return 1
	if n%2 == 0:
		memo[n] = 1 + cycle_length(n//2)
		return memo[n]
	memo[n] = 1 + cycle_length(3*n+1)
	return memo[n]

def max_cycle_length(i, j):
	m = 0
	for k in range(i, j+1):
		cl = cycle_length(k)
		if cl > m:
			m = cl
	return m

def main():
	while True:
		try:
			x, y = map(int, input().split())
			i = min(x, y)
			j = max(x, y)
			print(x, y, max_cycle_length(i, j))
		except EOFError:
			break

if __name__ == '__main__':
	memo = {}
	main()
	
	

registers = [0 for i in range(10)]
RAM = [0 for i in range(1000)]

def load_instructions():
	pos = 0
	while True:
		try:
			inp = input()
			if inp == '':
				return
			RAM[pos] = int(inp)
			pos += 1
		except EOFError:
			return

def execute_instructions():
	quant = 0
	pos = 0
	while True:
		a = RAM[pos]//100
		b = (RAM[pos] - a*100)//10
		c = RAM[pos] - a*100 - b*10
		
		if RAM[pos] == 100:
			quant += 1
			break
		if a == 2:
			registers[b] = c
		if a == 3:
			registers[b] = (registers[b] + c)%1000
		if a == 4:
			registers[b] = (registers[b] * c)%1000
		if a == 5:
			registers[b] = registers[c]
		if a == 6:
			registers[b] = (registers[b] + registers[c])%1000
		if a == 7:
			registers[b] = (registers[b] * registers[c])%1000
		if a == 8:
			registers[b] = RAM[registers[c]]
		if a == 9:
			RAM[registers[c]] = registers[b]
		if a == 0:
			if registers[c] != 0:
				pos = registers[b]
				pos -= 1
		
		pos += 1
		quant += 1
	
	return quant

def main():
	global registers, RAM
	n = int(input())
	input()
	for i in range(n):
		registers = [0 for i in range(10)]
		RAM = [0 for i in range(1000)]
		load_instructions()
		print(execute_instructions())
		if i != n-1:
			print()

if __name__ == '__main__':
	main()

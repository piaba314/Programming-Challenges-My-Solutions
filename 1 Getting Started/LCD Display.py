digits = {'0': '1110111', '1': '0010010', '2': '1011101', '3': '1011011',
		  '4': '0111010', '5': '1101011', '6': '1101111', '7': '1010010',
		  '8': '1111111', '9': '1111011'}

def matrix_of_digits(s, number_string):
	matrix = [[0 for j in range((s+3)*len(number_string))] for i in range(2*s+3)]
	for i in range(len(number_string)):
		d = number_string[i]
		for j in range(s):
			matrix[0][(s+3)*i+1+j] = int(digits[d][0])
			matrix[1+j][(s+3)*i] = int(digits[d][1])
			matrix[1+j][(s+3)*i+s+1] = int(digits[d][2])
			matrix[s+1][(s+3)*i + 1 + j] = int(digits[d][3])
			matrix[s+2+j][(s+3)*i] = int(digits[d][4])
			matrix[s+2+j][(s+3)*i+s+1] = int(digits[d][5])
			matrix[2*s+2][(s+3)*i+1+j] = int(digits[d][6])
	return matrix

def print_number(s, number_string):
	matrix = matrix_of_digits(s, number_string)
	for i in range(len(matrix)):
		for j in range(len(matrix[0])-1):
			if i == 0 or i == s+1 or i == 2*s + 2:
				if matrix[i][j] == 1:
					print('-', end='')
				else:
					print(' ', end='')
			else:
				if matrix[i][j] == 1:
					print('|', end='')
				else:
					print(' ', end='')
		print()

ini = True
def main():
	global ini
	while True:
		s, n = input().split()
		if s == '0' and n == '0':
			break
			
		s = int(s)
		print_number(s, n)
		
		print()
		
if __name__ == '__main__':
	main()

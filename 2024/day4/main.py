import os


def check_xmas(data, pos: tuple):
	"""Checks if 'XMAS' is readable in any direction from the pos in data """
	to_find = ['M', 'A', 'S']
	count = 0
	for row in range(-1, 2):
		for col in range(-1, 2):
			if row == col == 0:
				continue
			broke = False
			for k in range(1, len(to_find) + 1):
				if  pos[0] + k * row < 0 \
					or pos[0] + k * row >= len(data) \
					or pos[1] + k * col < 0 \
					or pos[1] + k * col >=  len(data[0]):
					broke = True
					break
				if data[pos[0] + k * row][pos[1] + k * col] != to_find[k - 1]:
					broke = True
					break
			if not broke:
				count += 1
	# if count > 0:
	# 	print(f"Found {count} for {pos}")
	return count




if __name__ == "__main__":
	data = []

	with open(file='input.txt', mode='r') as f:
		for line in f:
			data.append(line.removesuffix('\n'))

	xmas_count = 0
	for row in range(len(data)):
		for col in range(len(data[row])):
			if data[row][col] == 'X':
				xmas_count += check_xmas(data, (row, col))

	print(f"XMAS count: {xmas_count}")


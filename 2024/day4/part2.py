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


def check_x_mas(data, pos: tuple):
	to_check = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
	to_find = ['M', 'S']
	count = 0

	if pos[0] <= 0 or pos[0] >= len(data) - 1 \
		or pos[1] <= 0 or pos[1] >= len(data[0]) - 1:
		return 0

	for k in range(2):
		if data[pos[0] + to_check[k][0]][pos[1] + to_check[k][1]] in to_find \
			and data[pos[0] + to_check[-k - 1][0]][pos[1] + to_check[-k - 1][1]] in to_find \
			and data[pos[0] + to_check[k][0]][pos[1] + to_check[k][1]] != data[pos[0] + to_check[-k - 1][0]][pos[1] + to_check[-k - 1][1]]:
			count += 1
		else:
			break

	return (count == 2)


if __name__ == "__main__":
	data = []

	with open(file='input.txt', mode='r') as f:
		for line in f:
			data.append(line.removesuffix('\n'))

	xmas_count = 0
	for row in range(len(data)):
		for col in range(len(data[row])):
			if data[row][col] == 'A':
				xmas_count += check_x_mas(data, (row, col))

	print(f"X-MAS count: {xmas_count}")


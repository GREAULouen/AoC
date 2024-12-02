import os


if __name__ == "__main__":
	left, right = [], []

	with open(file='input.txt', mode='r') as f:
		for line in f:
			left.append(int(line.split()[0]))
			right.append(int(line.split()[1]))

	d_right = {}
	for k in right:
		if k not in d_right:
			d_right[k] = 0
		d_right[k] += 1

	similarity_score = 0

	for k in left:
		if k not in d_right:
			continue
		similarity_score += k * d_right[k]

	print(similarity_score)


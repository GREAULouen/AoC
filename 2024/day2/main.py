import os


def is_safe(report):
	value = report[0]
	direction = report[1] - value
	for k in range(1, len(report)):
		if direction > 0 and \
			(report[k] <= value or report[k] > value + 3):
			return False
		if direction <= 0 and \
			(report[k] >= value or report[k] < value - 3):
			return False
		value = report[k]
	return True

if __name__ == "__main__":
	reports = []

	with open(file='input.txt', mode='r') as f:
		for line in f:
			levels = []
			for k in line.split():
				levels.append(int(k))
			reports.append(levels)

	nb_safe = 0

	for report in reports:
		if is_safe(report):
			nb_safe += 1
		else:
			print(report)
			for k in range(len(report)):
				dampened = report[:k] + report[k+1:]
				print(dampened)
				if is_safe(dampened):
					nb_safe += 1
					break

	print(nb_safe)

import re

def calculate_total_sum(file_path):
	pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
	total_sum = 0

	with open(file_path, 'r') as file:
		for line in file:
			matches = re.findall(pattern, line)
			for match in matches:
				num1, num2 = map(int, match)
				total_sum += num1 * num2

	return total_sum

if __name__ == "__main__":
	file_path = "input.txt"
	total_sum = calculate_total_sum(file_path)
	print(f"Total Sum: {total_sum}")
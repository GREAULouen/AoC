import re

def calculate_total_sum(file_path):
	# Multi-pattern regex
	pattern = re.compile(r"(mul\((\d{1,3}),(\d{1,3})\))|(do\(\))|(don't\(\))")

	total_sum = 0
	is_enabled = True

	with open(file_path, 'r') as file:
		for line in file:
			matches = re.finditer(pattern, line)
			for match in matches:
				if match.group(1):  # mul(x, y) matched
					if is_enabled:
						num1, num2 = int(match.group(2)), int(match.group(3))
						total_sum += num1 * num2
				elif match.group(4):  # do() matched
					is_enabled = True
				elif match.group(5):  # don't() matched
					is_enabled = False

	return total_sum

if __name__ == "__main__":
	file_path = "input.txt"
	total_sum = calculate_total_sum(file_path)
	print(f"Total Sum: {total_sum}")

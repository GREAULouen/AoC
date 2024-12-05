import os


def validate(pages: str, ordering, retrying = 0):
	produced = {}
	for page in pages:
		produced[page] = False

	for i in range(len(pages) - 1):
		for j in range(i + 1, len(pages)):
			if pages[i] in ordering and pages[j] in ordering[pages[i]] \
				and not produced[pages[j]]:
				pages[i], pages[j] = pages[j], pages[i]
				return validate(pages, ordering, 1)
			produced[pages[i]] = True

	return int(pages[len(pages) // 2]) * retrying


if __name__ == "__main__":

	content = []
	with open(file='input.txt', mode='r') as f:
		for line in f:
			content.append(line.strip('\n'))

	ordering = {}
	production = []

	for k in range(content.index('')):
		splt = content[k].split('|')
		if not splt[1] in ordering:
			ordering[splt[1]] = []
		ordering[splt[1]].append(splt[0])

	production = content[content.index('') + 1:]

	total = 0
	for update in production:
		total += validate(update.split(','), ordering)

	print(f"total: {total}")

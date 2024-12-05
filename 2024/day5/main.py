import os


def validate(update: str, ordering):
	pages = update.split(',')
	produced = {}
	for page in pages:
		produced[page] = False

	print(f"update: {update}")
	for i in range(len(pages) - 1):
		for j in range(i + 1, len(pages)):
			if pages[i] in ordering and pages[j] in ordering[pages[i]] \
				and not produced[pages[j]]:
				return 0
			produced[pages[i]] = True

	return int(pages[len(pages) // 2])


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
		total += validate(update, ordering)

	print(f"total: {total}")

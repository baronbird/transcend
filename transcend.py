# transcend.py #
# generate text network from a plain-text project gutenberg e-book

import sys, re

class Graph():
	def __init__(self):
		self.edges = set()
	
	def add_edge(self, first, second):
		forward = "{}\t{}".format(first, second)
		reverse = "{}\t{}".format(second, first)
		if forward not in self.edges and reverse not in self.edges:
			self.edges.add(forward)
	
	def output(self, filename):
		with open(filename, "w") as f:
			for edge in self.edges:
				f.write(edge + "\n")

def process(word):
	word_list = []

	word = word.lower()
	word = word.replace("_", "")
	word = re.sub("\[.*\]", "", word)

	curr = ""
	hyphen = False
	for c in word:
		if c in '"()\'.,?!:;':
			if len(curr) > 0:
				word_list.append(curr)
				curr = ""
			word_list.append(c)

		elif c is '-':
			if hyphen:
				if len(curr) > 1:
					word_list.append(curr[:-1])
				word_list.append("--")
				hyphen = False
				curr = ""
			else:
				hyphen = True
				curr += c

		else:
			curr += c

	if len(curr) > 0:
		word_list.append(curr)

	return word_list
	
if __name__ == "__main__":
	graph = Graph()
	infile = sys.argv[1]
	outfile = sys.argv[2]

	prev_word = None
	for line in io.open(infile, "r", encoding="utf-8"):
		for token in line.encode('utf-8').strip().split():
			word_list = process(token)
			for word in word_list:
				if prev_word != None:
					graph.add_edge(prev_word, word)
				prev_word = word

	graph.output(outfile)

# transcend.py #
# generate text network from a plain-text project gutenberg e-book

import sys, re, io
import argparse

class Graph():
    def __init__(self, number=False):
        self.edges = set()
        self.nodeMap = {}
        self.numNodes = 0
        self.nodes = set()
        self.number = number

    def add_edge(self, first, second):
        if first == second:
            return

        if self.number:
            if first not in self.nodes:
                self.nodes.add(first)
                self.numNodes = self.numNodes + 1
                self.nodeMap[first] = self.numNodes
            if second not in self.nodes:
                self.nodes.add(second)
                self.numNodes = self.numNodes + 1
                self.nodeMap[second] = self.numNodes

            first = self.nodeMap[first]
            second = self.nodeMap[second]



        forward = "{}\t{}".format(first, second)
        reverse = "{}\t{}".format(second, first)
        if forward not in self.edges and reverse not in self.edges:
            self.edges.add(forward)

    def output(self, filename):
        with open(filename, "w") as f:
            if self.number:
                f.write("{}\t{}\n".format(self.numNodes, len(self.edges)))
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

    parser = argparse.ArgumentParser(description='Generate network from text file')

    parser.add_argument('infile', metavar='INPUT_FILE', type=str)
    parser.add_argument('outfile', metavar='OUTPUT_FILE', type=str)
    parser.add_argument('--number', '-n', action='store_true')

    args = parser.parse_args()

    graph = Graph(args.number)

    prev_word = None
    for line in io.open(args.infile, "r", encoding="utf-8"):
        for token in line.encode('utf-8').strip().split():
            word_list = process(token)
            for word in word_list:
                if prev_word != None:
                    graph.add_edge(prev_word, word)
                prev_word = word

    graph.output(args.outfile)

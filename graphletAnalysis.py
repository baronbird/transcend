#!/usr/bin/env python2.7

# graphletAnalysis.py
# Sam Alptekin, Sam Berning, Joe Kimlinger

# Takes in the GDD Agreement matrix and ouputs a sorted csv of pairs of networks
# ranked from lowest GDD Agreement to highest

import pandas as pd
from operator import itemgetter
import os
import seaborn

if __name__ == "__main__":
    data = pd.read_csv("graphletCounts/gdda.txt", sep='\t', index_col=0)


    processed = set()
    dataToSort = []
    for column in data:
        for row in data.index:
            if row != column:
                if column + row not in processed:
                    dataToSort.append([column, row, data[column][row]])
                    processed.add(row + column)

    sortedData = sorted(dataToSort, key=itemgetter(2))
    for index in range(10):
        print os.path.basename(os.path.dirname(sortedData[index][0]))

    with open("graphletCounts/gddaPairs.csv", 'w') as f:
        for pair in sortedData:
            #sorry
            pair.append(os.path.basename(os.path.dirname(pair[0])) ==
            os.path.basename(os.path.dirname(pair[1])))

            f.write("{},{},{},{}\n".format(os.path.basename(pair[0]),
            os.path.basename(pair[1]), pair[2], pair[3]))


    trans = ['ralph-waldo-emerson', 'henry-david-thoreau', 'margaret-fuller']
    real = ['fyodor-dostoyevsky', 'leo-tolstoy', 'gustave-flaubert']
    roman = ['mary-shelley', 'walter-scott', 'samuel-taylor-coleridge']
    periods = [trans, real, roman]
    new_headers = []

    for period in periods:
        for author in period:
            for column in data:
                if author in column:
                    new_headers.append(column)


    heatmap_data = pd.DataFrame(columns=new_headers, index=new_headers)
    for pair in sortedData:
        heatmap_data[pair[0]][pair[1]] = pair[2]
        heatmap_data[pair[1]][pair[0]] = pair[2]

    heatmap_data.fillna(0, inplace=True)

    heatmap = seaborn.heatmap(heatmap_data)
    heatmap_image = heatmap.get_figure()
    heatmap_image.savefig("graphletCounts/heatmap.png")

    correct = 0
    for work in new_headers:
        for pair in sortedData:
            if pair[0] == work or pair[1] == work:
                if pair[3]:
                    correct += 1
                break
    print correct, "/", len(new_headers), "=", float(correct)/len(new_headers)

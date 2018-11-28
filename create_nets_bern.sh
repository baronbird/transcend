#!/bin/sh

for file in texts/henry-david-thoreau/*.txt; do
	filename="numberNetworks/henry-david-thoreau/$(basename $file | cut -f 1 -d '.')-net.txt"
	python transcend.py -n $file $filename
	echo "made $filename"
done
echo "finished thoreau"

for file in texts/mary-shelley/*.txt; do
	filename="numberNetworks/mary-shelley/$(basename $file | cut -f 1 -d '.')-net.txt"
	python transcend.py -n $file $filename
	echo "made $filename"
done
echo "finished shelley"

for file in texts/gustave-flaubert/*.txt; do
	filename="numberNetworks/gustave-flaubert/$(basename $file | cut -f 1 -d '.')-net.txt"
	python transcend.py -n $file $filename
	echo "made $filename"
done
echo "finished flaubert"

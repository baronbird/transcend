To generate number networks from texts run:

python transcend.py texts graphletCounts -n

To generate graphlet counts for all networks in graphletCounts/ run:

python runOrca.py graphletCounts

To generate comparisons for all networks and compute the gdd agreement run:

python networkComparison.py graphletCounts gdda 10

The files for the comparisons will appear in graphletCounts/ with all networks listed in the first row and column and their correlation score in the respective row/column cell
To do generate the same file for average clustering coefficient distance run:

python newtorkComparison.py graphletCounts clustering 10


'''
This script runs orca on every file in a specific subdirectory structure as follows:
	main_dir
	|
	|------ subdirectory
	|	|
	|	|----- networks
	|	|
	|------ another subdirectory
	|	|
	|	|----- more networks
	.
	.
	.

The resulting graphlt counts will be placed in the same structure with the same subdirectory names, but with the name of main_dir
specified by command line argument:

python runOrca.py main_dir output_dir
'''

import os
import glob
import sys

if len(sys.argv) != 3:
	print "Usage: {} INPUT_DIR OUTPUT_DIR".format(sys.argv[0])
	sys.exit(1)

for f in glob.glob('{}/*/*'.format(sys.argv[1])):
	out = f.replace('testNets', sys.argv[2])
	if not os.path.exists(os.path.dirname(out)):
		os.makedirs(os.path.dirname(out))
	os.system('./orca 5 {} {}'.format(f, out))

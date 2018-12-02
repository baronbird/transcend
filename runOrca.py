'''
This script runs orca on every file in a directory, searching subdirectories recursively for .txt files.
It will generate the ouput in the same directory structure as the input dir except that the root directory will have the name specified by the OUPUT_DIR command line argument

python runOrca.py main_dir output_dir
'''

import os
import glob
import sys

if len(sys.argv) != 3:
	print "Usage: {} INPUT_DIR OUTPUT_DIR".format(sys.argv[0])
	sys.exit(1)

for root, dirname, filename in os.walk(sys.argv[1]):
	out = root.replace(sys.argv[1], sys.argv[2]) + "/"
	print root
	if not os.path.exists(out):
		os.makedirs(out)
	for f in filename:
		os.system('./orca 4 {} {}'.format(root + "/" + f, out + f))

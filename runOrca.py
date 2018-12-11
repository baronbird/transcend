'''
This script runs orca on every file in a directory, searching subdirectories recursively for .txt files.
It will generate the graphlet counts with the .ndump2 extension

python runOrca.py input_dir
'''

import os
import glob
import sys

if len(sys.argv) != 2:
    print "Usage: {} INPUT_DIR".format(sys.argv[0])
    sys.exit(1)

for root, dirname, filename in os.walk(sys.argv[1]):
    for f in filename:
        if f[-4:] == '.txt':
            os.system('./orca 4 {} {}'.format(os.path.join(root, f), os.path.join(root, f[:-4] + '.ndump2')))

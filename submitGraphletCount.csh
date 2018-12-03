#!/bin/csh

# #$ -M jkimling@nd.edu	 # Email address for job notification
# #$ -m be		 # Send mail when job begins, ends and aborts
#$ -q long		# Specify queue

# If using a wildcard (ex: networks/*/*.gw), be sure to put quotes around argument when submitting script
#  	example: qsub submitGraphletCount.csh "graphletCounts/*/*/gw"

python count.py "$1"

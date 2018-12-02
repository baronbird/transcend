#!/bin/sh
for file in `ls $1`; do
	qsub submitGraphletCount.csh "$file"
done

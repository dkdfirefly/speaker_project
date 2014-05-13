#!/usr/bin/env sh

for i in `ls -1 *.0000*.txt`; do python ../../../../../code/src/extractFeatures.py $i ../../../../../code/output/featureSet.txt; done


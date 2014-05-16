#!/usr/bin/env sh
if [ -f featureSet.txt ];
then
  rm featureSet.txt
fi
if [ -f train.txt ];
then
  rm train.txt
fi
if [ -f test.txt ];
then
  rm test.txt
fi

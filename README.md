speaker_project
===============

# Directions for usage

# Start from the root folder
# Change to output folder and clean it
cd code/output/
sh ../src/clean.sh

# Change to directory having the pitch files and extract features
cd ../../data/gtzan-proc/genres/classical/pitches_lead/
../../../../../code/src/commands.sh

# Repeat this for all the song genres required
eg:
cd ../../pop/pitches_lead/
../../../../../code/src/commands.sh
cd ../../rock/pitches_lead/
../../../../../code/src/commands.sh

# Change directory to output folder
cd ../../../../../code/output/

#Break into training and testing data
# The last argument must be (10xnumber of genres extracted), say (10x3) for current setting
python ../src/separateTrainTest.py featureSet.txt 30

#For classification
# The last but one argument must be (10xnumber of genres extracted), say (10x3) for current setting
# The last argument must be the number of genres extracted, say 3 in the current setting
python ../src/classify.py train.txt test.txt 30 3

#For clustering
# The last but one argument must be (10xnumber of genres extracted), say (10x3) for current setting
# The last argument must be the number of genres extracted, say 3 in the current setting
python ../src/cluster.py featureSet.txt 30 3

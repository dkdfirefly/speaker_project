cd code/output

sh ../src/clean.sh

#combinedOrig.txt
#combinedSolo.txt
#mfccFeatures.txt
#pitchFeaturesOrig.txt
#pitchFeaturesSolo.txt
#reducedCombinedOrig.txt
#reducedCombinedSolo.txt
#reducedMFCCF.txt
#reducedPitchOrigF.txt
#reducedPitchSoloF.txt

echo ''
echo '######################################'
echo 'MFCC features for the entire dataset'
echo  '####################################'
sh ../src/clean.sh
python ../src/separateTrainTest.py mfccFeatures.txt 100
python ../src/classify.py train.txt test.txt 100 10
python ../src/cluster.py mfccFeatures.txt 100 10

echo ''
echo '######################################'
echo 'Pitch Features - Lead : for the entire dataset'
echo '###############################################'
sh ../src/clean.sh
python ../src/separateTrainTest.py pitchFeaturesSolo.txt 100
python ../src/classify.py train.txt test.txt 100 10
python ../src/cluster.py pitchFeaturesSolo.txt 100 10

echo ''
echo '######################################'
echo 'Pitch Features - Original : for the entire dataset'
echo '##################################################'
sh ../src/clean.sh
python ../src/separateTrainTest.py pitchFeaturesOrig.txt 100
python ../src/classify.py train.txt test.txt 100 10
python ../src/cluster.py pitchFeaturesOrig.txt 100 10

echo ''
echo '######################################'
echo 'Combined Features - Lead : for the entire dataset'
echo '##################################################'
sh ../src/clean.sh
python ../src/separateTrainTest.py combinedSolo.txt 100
python ../src/classify.py train.txt test.txt 100 10
python ../src/cluster.py combinedSolo.txt 100 10

echo ''
echo '######################################'
echo 'Combined Features - Original : for the entire dataset'
echo '##################################################'
sh ../src/clean.sh
python ../src/separateTrainTest.py combinedOrig.txt 100
python ../src/classify.py train.txt test.txt 100 10
python ../src/cluster.py combinedOrig.txt 100 10

echo ''
echo '######################################'
echo 'Reduced genres: classical, pop, rock - mfcc'
echo '#################################################'
sh ../src/clean.sh
python ../src/separateTrainTest.py reducedMFCCF.txt 30
python ../src/classify.py train.txt test.txt 30 3
python ../src/cluster.py reducedMFCCF.txt 30 3

echo ''
echo '######################################'
echo 'Reduced genres: classical, pop, rock - picth lead'
echo '#################################################'
sh ../src/clean.sh
python ../src/separateTrainTest.py reducedPitchSoloF.txt 30
python ../src/classify.py train.txt test.txt 30 3
python ../src/cluster.py reducedPitchSoloF.txt 30 3

echo ''
echo '######################################'
echo 'Reduced genres: classical, pop, rock - pitch orig'
echo '#################################################'
sh ../src/clean.sh
python ../src/separateTrainTest.py reducedPitchOrigF.txt 30
python ../src/classify.py train.txt test.txt 30 3
python ../src/cluster.py reducedPitchOrigF.txt 30 3

echo ''
echo '######################################'
echo 'Reduced genres: classical, pop, rock - combined lead'
echo '#################################################'
sh ../src/clean.sh
python ../src/separateTrainTest.py reducedCombinedSolo.txt 30
python ../src/classify.py train.txt test.txt 30 3
python ../src/cluster.py reducedCombinedSolo.txt 30 3

echo ''
echo '######################################'
echo 'Reduced genres: classical, pop, rock - combined orig'
echo '#################################################'
sh ../src/clean.sh
python ../src/separateTrainTest.py reducedCombinedOrig.txt 30
python ../src/classify.py train.txt test.txt 30 3
python ../src/cluster.py reducedCombinedOrig.txt 30 3


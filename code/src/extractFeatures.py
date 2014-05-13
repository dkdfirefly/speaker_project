import numpy as np
import scipy.stats
import sys

def main(argv):
  if len(argv) != 3:
    print 'Usage: python extractFeatures.py fileName outFile'
    sys.exit(1)

  f = open(argv[1], 'r')
  fout = open(argv[2], 'a')
  time = []
  F0 = []
  featureSet = []

  for line in f:
    lineSp = line.strip('\n').split()
    if lineSp[1] != '-1.000000000000000000e+02':
      time.append(float(lineSp[0]))
      F0.append(float(lineSp[1]))

  f.close()
  
  # Calculate features
  maxF0 = max(F0)
  featureSet.append(maxF0)

  minF0 = min(F0)
  featureSet.append(minF0)

  meanF0 = np.mean(F0)
  featureSet.append(meanF0)

  stdF0 = np.std(F0)
  featureSet.append(meanF0)

  skewF0 = scipy.stats.skew(F0)
  featureSet.append(skewF0)

  kurtF0 = scipy.stats.kurtosis(F0)
  featureSet.append(kurtF0)

  vib = []
  lenF0 = len(F0)
  for i in range(lenF0 - 1):
    vib.append(F0[i+1] - F0[i])

#  maxVib = max(vib)
#  featureSet.append(maxVib)

#  minVib = min(vib)
#  featureSet.append(minVib)

  meanVib = np.mean(vib)
  featureSet.append(meanVib)

  stdVib = np.std(vib)
  featureSet.append(meanVib)

#  skewVib = scipy.stats.skew(vib)
#  featureSet.append(skewVib)

#  kurtVib = scipy.stats.kurtosis(vib)
#  featureSet.append(kurtVib)

  fout.write(str(featureSet).strip('[').strip(']').replace(" ","") + '\n')
  fout.close()

  
"""
  Boilerplate for calling main function
"""
if __name__=='__main__':
  main(sys.argv)

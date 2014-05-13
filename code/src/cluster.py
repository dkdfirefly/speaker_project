import numpy as np
from sklearn import cluster
from sklearn import metrics
from sklearn import neighbors
from sklearn.naive_bayes import GaussianNB
from sklearn import svm
import sys
from time import time

def main(argv):
  if len(argv) != 4:
    print 'Usage: python cluster.py featureSet.txt <size> <n_classes>'
    print
    print 'Total samples for each class: size/n_classes'
    print 'All samples for a particular class must occur consecutively'
    print 'Use extractfeatures.py for right format'
    sys.exit(1)
  
  f = open(argv[1], 'r')
  size = int(argv[2])
  n_classes = int(argv[3])

  data = []
  pred = []
  labels = []

  samples_per_class = (size)/n_classes;
  j = samples_per_class
  index = 0
  for i in range(size + n_classes - 1):
    if j == 0:
      j = samples_per_class
      index = index + 1
      continue
    else:
      j = j-1
      labels.append(index)

  print
  print 'Clustering Task:'
  print '================'
  print '\tExpected Output: ' + str(labels)

#  labels = [0, 0, 0, 0, 0, 
#            1, 1, 1, 1, 1,
#            2, 2, 2, 2, 2,
#            0, 0, 0, 0, 0, 
#            1, 1, 1, 1, 1,
#            2, 2, 2, 2, 2]#,
#            3, 3, 3, 3, 3,
#            4, 4, 4, 4, 4,
#            5, 5, 5, 5, 5, 
#            6, 6, 6, 6, 6, 
#            7, 7, 7, 7, 7,
#            8, 8, 8, 8, 8,
#            9, 9, 9, 9, 9]

  for line in f:
    lineSp = line.strip('\n').split(',')
    floatSp = []
    for i in lineSp:
      floatSp.append(float(i))
    data.append(floatSp)
  dataNP = np.array(data)
  
  f.close()
  

#  for line in fPred:
#    lineSp = line.strip('\n').split(',')
#    floatSp = []
#    for i in lineSp:
#      floatSp.append(float(i))
#    pred.append(floatSp)
#  predNP = np.array(pred)

#  fPred.close()

  t0 = time()
  estimator = cluster.KMeans(n_clusters=n_classes)
  estimator.fit(dataNP) 
  print
  print 'KNN Clustering:'
  print '\tPredicted Output: ' + str(estimator.labels_)
  print('\tTime: %.2fs\n\tEstimator Inertia: %i\n\tHomgenity: %.3f\n\tCompleteness: %.3f\n\tV_measure: %.3f\n\tAdjusted_rand_score: %.3f\n\tAdjusted Mutual Info: %.3f'
          % ((time() - t0), estimator.inertia_,
          metrics.homogeneity_score(labels, estimator.labels_),
          metrics.completeness_score(labels, estimator.labels_),
          metrics.v_measure_score(labels, estimator.labels_),
          metrics.adjusted_rand_score(labels, estimator.labels_),
          metrics.adjusted_mutual_info_score(labels,  estimator.labels_)))

#  print 'KNN classifier:'
#  knn = neighbors.KNeighborsClassifier(n_neighbors = 10)
#  knn.fit(dataNP,labels)
#  print knn.predict(predNP)
#  print knn.score(predNP, labels)

#  print
#  print 'Linear SVC'
#  clf = svm.LinearSVC()
#  clf.fit(dataNP, labels)  
#  print clf.predict(predNP)
#  print clf.score(predNP, labels)

#  print
#  print 'Gaussian NB'
#  gnb = GaussianNB()
#  gnb.fit(dataNP,labels)
#  print gnb.predict(predNP)
#  print gnb.score(predNP, labels)

#  print
#  print 'SVC'
#  clf = svm.SVC()
#  clf.fit(dataNP, labels)
#  print clf.predict(predNP)
#  print clf.score(predNP, labels)


"""
  Boilerplate for calling main
"""
if __name__=='__main__':
  main(sys.argv)

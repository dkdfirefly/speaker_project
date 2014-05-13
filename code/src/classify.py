import numpy as np
from sklearn import cluster
from sklearn import metrics
from sklearn import neighbors
from sklearn.naive_bayes import GaussianNB
from sklearn import svm
import sys
from time import time

def main(argv):
  if len(argv) != 5:
    print 'Usage: python classify.py train.txt test.txt <size> <n_classes>'
    print
    print 'Total samples for each class: size/n_classes'
    print 'All samples for a particular class must occur consecutively'
    print 'Currently using a 50:50 split for train/test'
    print 'Use extractfeatures.py and generateDatasets.py for right format'
    sys.exit(1)
  
  f = open(argv[1], 'r')
  fPred = open(argv[2], 'r')
  size = int(argv[3])
  n_classes = int(argv[4])

  data = []
  pred = []
  labels = []

  samples_per_class = (size/2)/n_classes;
  j = samples_per_class
  index = 0
  for i in range(size/2 + n_classes - 1):
    if j == 0:
      j = samples_per_class
      index = index + 1
      continue
    else:
      j = j-1
      labels.append(index)

  print
  print 'Classification Task'
  print '==================='
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
  

  for line in fPred:
    lineSp = line.strip('\n').split(',')
    floatSp = []
    for i in lineSp:
      floatSp.append(float(i))
    pred.append(floatSp)
  predNP = np.array(pred)

  fPred.close()

#  t0 = time()
#  estimator = cluster.KMeans(n_clusters=3)
#  estimator.fit(dataNP) 
#  print estimator.labels_
#  print labels
#  print('%.2fs    %i   %.3f   %.3f   %.3f   %.3f   %.3f'
#          % ((time() - t0), estimator.inertia_,
#          metrics.homogeneity_score(labels, estimator.labels_),
#          metrics.completeness_score(labels, estimator.labels_),
#          metrics.v_measure_score(labels, estimator.labels_),
#          metrics.adjusted_rand_score(labels, estimator.labels_),
#          metrics.adjusted_mutual_info_score(labels,  estimator.labels_)))

  print
  print 'KNN classifier:'
  knn = neighbors.KNeighborsClassifier(n_neighbors = 10)
  knn.fit(dataNP,labels)
  print '\tPredicted Output: ' + str(knn.predict(predNP))
  print '\tAccuracy: ' + str(knn.score(predNP, labels))

  print
  print 'Linear SVC'
  clf = svm.LinearSVC()
  clf.fit(dataNP, labels)  
  print '\tPredicted Output: ' + str(clf.predict(predNP))
  print '\tAccuracy: ' + str(clf.score(predNP, labels))

  print
  print 'Gaussian NB'
  gnb = GaussianNB()
  gnb.fit(dataNP,labels)
  print '\tPredicted Output: ' + str(gnb.predict(predNP))
  print '\tAccuracy: ' + str(gnb.score(predNP, labels))

  print
  print 'SVC'
  clf = svm.SVC()
  clf.fit(dataNP, labels)
  print '\tPredicted Output: ' + str(clf.predict(predNP))
  print '\tAccuracy: ' + str(clf.score(predNP, labels))


"""
  Boilerplate for calling main
"""
if __name__=='__main__':
  main(sys.argv)

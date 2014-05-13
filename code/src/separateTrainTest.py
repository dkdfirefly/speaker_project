import sys

def main(argv):
  if len(argv) != 3:
    print 'Usage: python separateTrainTest.py fileName <size>'
    print
    print 'OutputFiles: train.txt, test.txt'
    sys.exit(1)

  f = open(argv[1], 'r')
  size = int(argv[2])
  fTrain = open('train.txt', 'w')
  fTest = open('test.txt', 'w')
  for i in range(size/2):
    test = f.readline()
    fTest.write(test)
    train = f.readline()
    fTrain.write(train)

  fTrain.close()
  fTest.close()

if __name__=='__main__':
  main(sys.argv)

from pprint import pprint
from knn import KNN
import csv


if __name__ == '__main__':
    dt = open('dataset/spambase.data').readlines()
    ln = dt[0].strip()

    for r in csv.reader(ln):
        print(r)

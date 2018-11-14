from pprint import pprint
from knn import KNN
from validator import Validator
import csv
import json


def load_dataset(path):
    dataset = []
    with open(path) as fl:
        reader = csv.reader(fl, delimiter=',')

        for row in reader:
            instance = []
            for i in range(len(row) - 1):
                instance.append(float(row[i]))

            instance.append(int(row[57]))
            dataset.append(instance)
    
    return dataset


if __name__ == '__main__':
    dataset = load_dataset('dataset/spambase.random.data')
    v = Validator(dataset)
    v.cross_validation(k=3)
    print(v.results)
    #v.calc_statis(json.loads(open('r.json').read()))

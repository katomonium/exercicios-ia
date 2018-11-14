from pprint import pprint
from knn import KNN
from validator import Validator
import csv
import json
import numpy as np
import matplotlib.pyplot as plt


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


def plot_results(results):
    n_groups = 6

    p = [x[0] for x in results]
    p.append(np.mean(p))

    r = [x[1] for x in results]
    r.append(np.mean(r))

    f1 = [x[2] for x in results]
    f1.append(np.mean(f1))
    
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.3
    opacity = 0.8

    rects1 = plt.bar(index, p, bar_width,
            alpha=opacity, label='p')

    rects2 = plt.bar(index + bar_width, r, bar_width,
            alpha=opacity, label='r')
    
    rects3 = plt.bar(index + 2 * bar_width, f1, bar_width,
            alpha=opacity, label='f1')
    
    plt.xticks(index + bar_width, ('0', '1', '2', '3', '4', 'A'))
    plt.legend()

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    dataset = load_dataset('dataset/spambase.random.data')
    v = Validator(dataset)
    v.cross_validation(k=(3, 5, 7))
    print(v.results)

    #r = [
    #    (0.738, 0.768, 0.753), 
    #    (0.785, 0.737, 0.760), 
    #    (0.751, 0.782, 0.767),
    #    (0.682, 0.703, 0.692),
    #    (0.786, 0.684, 0.731)
    #]

    #plot_results(r)

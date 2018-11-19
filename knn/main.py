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


def plot_results(results, ks):
    n_groups = 6

    for k in ks:
        p = [x[k][0] for x in results]
        p.append(np.mean(p))

        r = [x[k][1] for x in results]
        r.append(np.mean(r))

        f1 = [x[k][2] for x in results]
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
        plt.title('Spam/Not-Spam k={}'.format(k))
        plt.xlabel('Test group')
        plt.legend()

        plt.tight_layout()
        plt.savefig('spam_s_k{}'.format(k))

if __name__ == '__main__':
    dataset = load_dataset('dataset/spambase.random.data')
    ks = (3, 5, 7)

    v = Validator(dataset)
    v.cross_validation(ks)
    plot_results(v.results, ks)
    with open('matrix_s.json', 'w') as fl:
        fl.write(json.dumps(v.matrix, indent=4, sort_keys=True))

    # r = [{3: (0.8809523809523809, 0.5425219941348973, 0.6715063520871143), 5: (0.8819444444444444, 0.3724340175953079, 0.5237113402061856), 7: (0.8969072164948454, 0.25513196480938416, 0.39726027397260266)}, {3: (0.8914027149321267, 0.5038363171355499, 0.6437908496732027), 5: (0.9115646258503401, 0.34271099744245526, 0.49814126394052044), 7: (0.9298245614035088, 0.2710997442455243, 0.4198019801980198)}, {3: (0.9004739336492891, 0.5588235294117647, 0.689655172413793), 5: (0.9568345323741008, 0.3911764705882353, 0.5553235908141962), 7: (0.967032967032967, 0.25882352941176473, 0.40835266821345706)}, {3: (0.8390243902439024, 0.5165165165165165, 0.6394052044609666), 5: (0.8934426229508197, 0.32732732732732733, 0.4791208791208791), 7: (0.9047619047619048, 0.22822822822822822, 0.36450839328537166)}, {3: (0.8731707317073171, 0.4387254901960784, 0.5840130505709624), 5: (0.8978102189781022, 0.3014705882352941, 0.4513761467889908), 7: (0.8969072164948454, 0.21323529411764705, 0.3445544554455445)}]
    # plot_results(r, (3, 5, 7))

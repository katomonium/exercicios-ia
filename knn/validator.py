from knn import KNN
import sys
import json


def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))


def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s %s\r' % (bar, percents, '%', status))
    sys.stdout.flush()


class Validator:

    def __init__(self, dataset, n_chunks=5):
        self.dataset = dataset
        self.n_chunks = n_chunks
        self.chunks = list(split(dataset, n_chunks))
        self.results = []
        self.matrix = []

    def validate_test(self, knn, test, k, i):
        count = 0
        results = []
        for d in test:
            r = knn.classify(d, k)
            results.append((d[-1], r))
            count += 1
            progress(count, len(test), 'test_set {}'.format(i))

        print()
        return results

    def cross_validation(self, ks):
        for i in range(self.n_chunks):
            l = self.chunks[:i] + self.chunks[i+1:]
            training = [item for sublist in l for item in sublist]
            knn = KNN(training)

            test = self.chunks[i]
            results = self.validate_test(knn, test, ks, i)
            self.calc_statis(results, ks)
            

    def calc_statis(self, results, ks):
        resul = {}
        matrix = {}
        for k in ks:
            s = { 'tp': 0, 'fp': 0, 'tn': 0, 'fn': 0 }

            for r in results:
                if r[0]:
                    if r[1][k]:
                        s['tp'] += 1
                    else:
                        s['fn'] += 1
                else:
                    if r[1][k]:
                        s['fp'] += 1
                    else:
                        s['tn'] += 1

            try:
                p = s['tp'] / (s['tp'] + s['fp'])
            except ZeroDivisionError:
                p = 0.0
            
            try:
                r = s['tp'] / (s['fn'] + s['tp'])
            except ZeroDivisionError:
                r = 0.0
            
            try:
                f1 = 2 * (p * r) / (p + r)
            except ZeroDivisionError:
                f1 = 0.0

            resul[k] = (p, r, f1)
            matrix[k] = s

        self.matrix.append(matrix)
        self.results.append(resul)

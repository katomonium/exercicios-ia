import math

class KNN():

    def __init__(self, training_set):
        self.training = training_set

    def classify(self, test, k):
        n = self.calc_neighbors(test, k)
        c = self.calc_class(n)

        return c

    def distance(self, a, b):
        d = 0.0
        for i in range(len(a) - 1):
            d += math.pow(a[i] - b[i], 2)

        return math.sqrt(d)

    def calc_neighbors(self, test, ks):
        dist = []
        for i in self.training:
            d = self.distance(i, test)
            dist.append((d, i))

        dist.sort()
        n = {}
        for k in ks:
            n[k] = []

            for i in range(k):
                n[k].append(dist[i][1])

        return n

    def calc_class(self, neighbors):
        labels = {}

        for k in neighbors:
            labels[k] = {}
            for i in neighbors[k]:
                j = i[-1]
                if j in labels[k]:
                    labels[k][j] += 1
                else:
                    labels[k][j] = 1

        c = {}
        for k in labels:
            c[k] = []

            for i in labels[k]:
                c[k].append((labels[k][i], i))

            c[k].sort(key=lambda k: k[1], reverse=False)

        r = {}
        for k in c:
            r[k] = c[k][0][1]

        return r

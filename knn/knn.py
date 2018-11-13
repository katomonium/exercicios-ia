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

    def calc_neighbors(self, test, k):
        dist = []
        for i in self.training:
            d = self.distance(i, test)
            dist.append((d, i))

        dist.sort()
        n = []
        for i in range(k):
            n.append(dist[i][1])
        
        return n

    def calc_class(self, neighbors):
        labels = {}

        for i in neighbors:
            k = i[-1]
            if k in labels:
                labels[k] += 1
            else:
                labels[k] = 1

        l = []
        for k in labels:
            l.append((k, labels[k]))

        l.sort(key=lambda k: k[1], reverse=True)
        return l[0][0]

import numpy as np
import matplotlib.pyplot as plt

f = open('log', 'r')

lines = f.readlines()
f.close()

pops = []
for l in lines:
    if l[0] == '[':
        pops.append(l.strip())

for j in range(len(pops)):
    p = []
    for n in pops[j][1:-1].split(','):
        p.append(int(n))

    d = {}
    for i in range(-16, 16):
        d[i] = 0

    for i in p:
        d[i] += 1

    x = []
    y = []

    for k in d:
        x.append(k)
        y.append(d[k])

    plt.scatter(x, y, s=5, c=[(0,0,0)], alpha=0.5)
    plt.title('Population {:02d}'.format(j))
    plt.xlabel('x')
    plt.ylabel('y')
    name = 'pop{:02d}.png'.format(j)
    plt.savefig(name)
    print('saving {}'.format(name))
    plt.clf()

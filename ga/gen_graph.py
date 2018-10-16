import sys
import numpy as np
import matplotlib.pyplot as plt

f = open(sys.argv[1], 'r')

lines = f.readlines()
f.close()

pop_size = int(lines.pop(0))

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

    axes = plt.gca()
    axes.set_xlim([-17, 16])
    axes.set_ylim([0, pop_size+1])

    # plt.scatter(x, y, s=5, c=[(0,0,0)], alpha=0.5)
    plt.bar(x, y, 1, color='blue')
    plt.title('Population {:03d}'.format(j))
    plt.xlabel('x')
    plt.ylabel('qnt')
    name = 'pop{:03d}.png'.format(j)
    plt.savefig(name)
    print('saving {}'.format(name))
    plt.clf()

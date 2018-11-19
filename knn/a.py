import json
import numpy as np
from pprint import pprint

if __name__ == "__main__":
    with open('matrix_s.json') as fl:
        data = json.loads(fl.read())
    
    for k in (3, 5, 7):
        m = [x[str(k)] for x in data]

        for i in range(0, 5):
            print('confusion Matrix test set {} with k={}'.format(i, k))
            print('         Spam    ¬Spam')
            print('Spam      {:>3}       {:>3}'.format(m[i]['tp'], m[i]['fp']))
            print('¬Spam     {:>3}       {:>3}'.format(m[i]['fn'], m[i]['tn']))
            print()
        
        fn_a = np.average([x['fn'] for x in m])
        fp_a = np.average([x['fp'] for x in m])
        tn_a = np.average([x['tn'] for x in m])
        tp_a = np.average([x['tp'] for x in m])

        print('confusion Matrix average with k={}'.format(k))
        print('         Spam     ¬Spam')
        print('Spam     {:>3}    {:>3}'.format(tp_a, fp_a))
        print('¬Spam    {:>3}    {:>3}'.format(fn_a, tn_a))
        print('\n')
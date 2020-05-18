import numpy as np


class KamusReader:
    def __init__(self):
        pass

    def readKamus(self, filename):
        if (filename == 'indonesia'):
            container = np.array([['indonesia', 'sunda']])
        else:
            container = np.array([['sunda', 'indonesia']])
        f = open('../doc/' + filename + '.txt', 'r')
        text = f.readlines()
        for i in range(len(text)):
            line = text[i].strip('\n')
            a = line.split(' = ')
            container = np.append(container, [a], axis=0)
        f.close()
        return container

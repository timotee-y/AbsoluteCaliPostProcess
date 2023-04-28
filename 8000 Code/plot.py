import matplotlib.pyplot as plt
import numpy as np, codecs

for i in range (1, 32):
    try:
        filename = 'G' + str(i)
        # print(filename + '.txt')
        data = np.loadtxt('./Data/' + filename + '.txt')
        x = data[:, 0]
        y = data[:, 1]
        mean1 = np.mean(y)
        std1 = np.std(y)
        newx = []
        newy = []
        
        for i1 in range (0, len(x) - 1):
            if(np.abs(y[i1] - mean1) <= 3 * std1):
                newx.append(x[i1])
                newy.append(y[i1])
    
        tomean = str(round(np.mean(newy), 2))
        tostd = str(round(np.std(newy), 2))
        m = 'mean = ' + tomean + ' ns, '
        s = 'std = ' + tostd + ' ns'
        output = ('{}\t{}\t{}\t\n').format(filename, tomean, tostd)
        f = codecs.open('mean.txt', 'a+')
        f.write(output)
        f.close()

        plt.plot(newx, newy)
        plt.xlabel('TOW /s')
        plt.ylabel('Time Offset /ns')
        plt.title(filename)
        ax = plt.gca()
        plt.text(0.5, 0.92, m + s, bbox = dict(fc = 'white', ec = 'black'), transform = ax.transAxes)
        plt.savefig('./Plot/' + filename + '.png', dpi = 500)
        plt.close()
        print('{} plot done.'.format(filename))
    except:
        print('{} not found !!!'.format(filename + '.txt'))     
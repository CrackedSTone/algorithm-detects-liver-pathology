import numpy as np

class gradient:
    """This class implements the math of gradients"""

    # todo other types of gradients
    def __init__(self, array):
        self.base = array
        self.h, self.w = np.shape(array)

    def computeHorizontal(self):
        self.horizontal = np.zeros((self.h, self.w - 1))
        for i in range(self.h):
            for j in range(self.w - 1):
                self.horizontal[i][j] = abs(self.base[i][j] - self.base[i][j + 1])

    def computeVertical(self):
        self.vertical = np.zeros((self.h - 1, self.w))
        for i in range(self.h - 1):
            for j in range(self.w):
                self.vertical[i][j] = abs(self.base[i][j] - self.base[i + 1][j])

    def computeDiagonal135(self):
        self.diagonal135 = np.zeros((self.h - 1, self.w - 1))
        for i in range(self.h - 1):
            for j in range(self.w - 1):
                self.diagonal135[i][j] = abs(self.base[i][j] - self.base[i + 1][j + 1])

    def computeDiagonal45(self):
        self.diagonal45 = np.zeros((self.h - 1, self.w - 1))
        for i in range(self.h - 1):
            for j in range(self.w - 1):
                self.diagonal45[i][j] = abs(self.base[i + 1][j] - self.base[i][j + 1])

    def getHorizontal(self):
        return self.horizontal

    def getVertical(self):
        return self.vertical

    def getDiagonal135(self):
        return self.diagonal135

    def getDiagonal45(self):
        return self.diagonal45


"""
#test:
np.random.seed(1000)
A = np.around(np.random.random((5,3)),decimals=1)
B = gradient(A)
B.compute()
"""

# this code computes and plots gradients of the image
'''
dif = grds.gradient(gray)
plt.subplot(323)
dif.computeHorizontal()
plt.imshow(dif.getHorizontal(),cmap="inferno")
plt.title("Horizontal")
plt.subplot(324)
dif.computeVertical()
plt.imshow(dif.getVertical(),cmap="inferno")
plt.title("Vertical")
plt.subplot(325)
dif.computeDiagonal135()
plt.imshow(dif.getDiagonal135(),cmap="inferno")
plt.title("Diagonal135")
plt.subplot(326)
dif.computeDiagonal45()
plt.imshow(dif.getDiagonal45(),cmap="inferno")
plt.title("Diagonal45")
fig.tight_layout()
## save
#fig.savefig("tmp/p5.pdf")
'''
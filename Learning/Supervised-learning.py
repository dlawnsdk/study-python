import matplotlib.cm
from sklearn.datasets import make_classification
import matplotlib.pyplot as plt

X, y = make_classification(n_samples=50, n_features=2, n_redundant=0, random_state=0)
plt.scatter(X[:, 0], X[:, 1], c=y, marker=".", cmap=matplotlib.colormaps.get_cmap("bwr"), alpha=0.7)
plt.grid(True)
plt.show()

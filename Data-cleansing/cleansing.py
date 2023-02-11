import pandas as pd
import csv

# df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data", header=None)
# df.columns=["", "Alcohol", "Malic acid", "Ash", "Alcalinity of ash", "Magnesium", "Total phenols", "Flavanoids", "Nonflavanoid phenols", "Proanthocyanins", "Color intensity", "Hue", "OD280/0D315 of diluted wines", "Proline"]
# print(df)

# df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", header=None)
# df.columns=["sepal length", "sepal width", "petal length", "petal width", "class"]
# print(df)

with open("csv0.csv", "w") as csvfile:
    writer = csv.writer(csvfile, lineterminator="\n")

    writer.writerow(["city", "year", "season"])
    writer.writerow(["Nagano", 1998, "winter"])
    writer.writerow(["Sydney", 2000, "Summer"])

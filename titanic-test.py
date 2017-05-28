from sklearn import datasets, svm, metrics
# Standard scientific Python imports
import matplotlib.pyplot as plt
import pandas as pd

titanicdata = pd.read_csv("titanic-train.csv")
print(titanicdata)

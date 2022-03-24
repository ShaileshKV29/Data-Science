import pandas
import matplotlib.pyplot as plt

data = pandas.read_csv('Data-Visualization/Plots/test.csv')
print(data)

data.hist()
data.plot.bar()
data.plot.box()
data.plot.area()
plt.show()
plt.pie(data['DSA'])
plt.show()
plt.scatter(data["DSA"], data['CPP'])
plt.show()


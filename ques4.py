import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
salaries = np.random.normal(50000, 10000, 1000)

plt.hist(salaries, bins=30)
plt.title("Salary Distribution of Employees")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.show()

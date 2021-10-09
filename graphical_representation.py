import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
myfruits = ["Apples 35%", "Bananas 25%", "Cherries 25%", "Dates 15%"]
mycolors = ["black", "hotpink", "b", "#4CAF50"]

plt.pie(y, labels = myfruits, colors = mycolors)
plt.show() 

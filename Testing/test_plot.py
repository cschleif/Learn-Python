#%% Config
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#%% Test Plot
Year = [2012, 2014, 2016, 2020, 2021, 2022, 2018]
Profit = [80, 75.8, 74, 65, 99.5, 19, 33.6]

data_plot = pd.DataFrame({"Year":Year, "Profit":Profit})

sns.lineplot(x = "Year", y = "Profit", data=data_plot)
plt.show()
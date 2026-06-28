import pandas as pd, numpy as np
import matplotlib.pyplot as plt


# read th data
data = pd.read_csv("EDA report generator/datasets/iris.csv")

# Data Summary
dims = data.shape
print("DATA SUMMARY")
print(data.info())
d_types = {}
for d_type in data.dtypes:
    d_types[str(d_type)] = data.select_dtypes(str(d_type)).columns.tolist()
print(d_types)


# Histogram for numeric values
mosaic = np.array(d_types["float64"],dtype=str)     # converting the Y_columns to an mosaic compatible array 
mosaic =np.tile(mosaic,(2,1)) # a mosaic must be 2D

# creating a pyplot `fig_hist` figure using the subplot_mosaic function
fig_hist, axd  = plt.subplot_mosaic(mosaic,  layout="tight")

for column in d_types["float64"]:
    axes = axd[column]
    axes.hist(data[column])
    axes.set_title(column)


# Scatter plot for each pair of numeric coloumn
Y_columns = d_types["float64"].copy()       
Y_columns.pop()

mosaic = np.array(Y_columns,dtype=str)     # converting the numeric columns to an mosaic compatible array 
mosaic =np.tile(mosaic,(2,1)) # a mosaic must be 2D


fig_scatter, axd = plt.subplot_mosaic(mosaic, layout="tight")  # creating a pyplot `fig_scatter` figure using the subplot_mosaic function

for Y_column, ax in axd.items():
    for X_column in [column for column in d_types["float64"] if column != Y_column]:        # using for loop to polt data on multiple axes 
        ax.scatter(data[X_column], data[Y_column], label=f"{X_column}")
        ax.set_ylabel(Y_column, loc="top")
    ax.legend(loc=4)
    ax.grid(True)
plt.show()
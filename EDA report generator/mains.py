import pandas as pd, numpy as np
import matplotlib.pyplot as plt


# readind the data
data = pd.read_csv("EDA report generator/datasets/iris.csv")   # taking `irs.csv` as an example can be changed to other `.csv`
                                                                # Note: this program is only functional for `float64` and `str` values 
                                                                # though some tweaking here and there can make it operational for other values too 


'''Data Summary'''

print("DATA SUMMARY")
data.info()

# sorting different dtypes into a dictonary
d_types = {}
for d_type in data.dtypes:
    d_types[str(d_type)] = data.select_dtypes(str(d_type)).columns.tolist()
print(d_types)



'''Histogram for numeric values'''

mosaic = np.array(d_types["float64"],dtype=str)     # converting the Y_columns to an mosaic compatible array 
mosaic =np.tile(mosaic,(2,1)) # a mosaic must be 2D

# creating a pyplot `fig_hist` figure using the subplot_mosaic function
fig_hist, axd  = plt.subplot_mosaic(mosaic,  layout="tight")

for column in d_types["float64"]:
    axes = axd[column]
    axes.hist(data[column])
    axes.set_title(column)



'''Scatter plot for each pair of numeric coloumn'''

Y_columns = d_types["float64"].copy()       
Y_columns.pop()

mosaic = np.array(Y_columns,dtype=str)     # converting the numeric columns to an mosaic compatible array 
mosaic =np.tile(mosaic,(2,1)) # a mosaic must be 2D


fig_scatter, axd = plt.subplot_mosaic(mosaic, layout="tight")  # creating a pyplot `fig_scatter` figure using the subplot_mosaic function

for Y_column, ax in axd.items():
    for X_column in [column for column in d_types["float64"] if column != Y_column]:        # using for loop to polt data on multiple axes 
        ax.scatter(data[X_column], data[Y_column], label=X_column)
        ax.set_ylabel(Y_column, loc="top")
    ax.legend(loc=4)
    ax.grid(True)



'''Pie chart for every catogorial data'''

mosaic = np.array(d_types["str"],dtype=str)     # converting the str columns to an mosaic compatible array 
mosaic =np.tile(mosaic,(2,1)) # a mosaic must be 2D

fig_pie, axd = plt.subplot_mosaic(mosaic, layout="tight")   # creating a pyplot `fig_scatter` figure using the subplot_mosaic function

for title, ax in axd.items():                           # using for loop to polt data on multiple charts 
    temp_dict = data[title].value_counts().to_dict()        
    ax.pie(temp_dict.values(), labels=temp_dict.keys(), startangle=90)


'''Saving the plots in EDA report generator/Saves'''

fig_hist.savefig("EDA report generator/Saves/histogram.png")
fig_scatter.savefig("EDA report generator/Saves/scatterplot.png")
fig_pie.savefig("EDA report generator/Saves/piechart.png")
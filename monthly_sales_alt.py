# monthly_sales.py

import operator
import os
import pandas
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# utility function to convert float or integer to usd-formatted string (for printing), adapted from:
#  + https://github.com/s2t2/shopping-cart-screencast/blob/30c2a2873a796b8766e9b9ae57a2764725ccc793/shopping_cart.py#L56-L59
def to_usd(my_price):
    return "${0:,.2f}".format(my_price) #> $12,000.71

#
# INPUTS
#

csv_filename = "sales-201803.csv" # TODO: allow user to specify

# reference a file in the "data" directory, adapted from:
#  + https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/modules/os.md#file-operations
csv_filepath = os.path.join(os.path.dirname(__file__), "data", csv_filename)

# read csv file into a pandas dataframe object, adapted from:
#  + https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/packages/pandas.md
csv_data = pandas.read_csv(csv_filepath)

#
# CALCULATIONS
#

monthly_total = csv_data["sales price"].sum()

# get unique product names, adapted from:
#  + https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.ndarray.tolist.html
#  + https://stackoverflow.com/questions/1966207/converting-numpy-array-into-python-list-structure
product_names = csv_data["product"]
unique_product_names = product_names.unique()
unique_product_names = unique_product_names.tolist() # convert numpy.ndarray to list

top_sellers = []

for product_name in unique_product_names:
    # filering approach adapted from: https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/packages/pandas.md
    matching_rows = csv_data[csv_data["product"] == product_name]
    product_monthly_sales = matching_rows["sales price"].sum()
    top_sellers.append({"name": product_name, "monthly_sales": product_monthly_sales})

# sort the list of dictionaries to make sure they are looped through and charted in the right order, adapted from:
#   + https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/datatypes/lists.md#sorting
# sort in descending order, adapted from:
#  + https://www.programiz.com/python-programming/methods/built-in/sorted
#  + https://docs.python.org/3/howto/sorting.html
top_sellers = sorted(top_sellers, key=operator.itemgetter("monthly_sales"), reverse=True)

#
# OUTPUTS
#

print("-----------------------")
print("MONTH: March 2018") # TODO: get month and year

print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print(f"TOTAL MONTHLY SALES: {to_usd(monthly_total)}")

print("-----------------------")
print("TOP SELLING PRODUCTS:")

rank = 1
for d in top_sellers:
    print("  " + str(rank) + ") " + d["name"] + ": " + to_usd(d["monthly_sales"]))
    rank = rank + 1

print("-----------------------")
print("VISUALIZING THE DATA...")

# dataviz adapted from:
#  + https://georgetown-opim-py.slack.com/archives/CFZDKNKA4/p1549494877005200
#  + https://matplotlib.org/api/_as_gen/matplotlib.pyplot.title.html
#  + https://matplotlib.org/gallery/subplots_axes_and_figures/figure_title.html
#  + https://matplotlib.org/users/pyplot_tutorial.html
#  + https://matplotlib.org/gallery/lines_bars_and_markers/barh.html
#  + https://python-graph-gallery.com/2-horizontal-barplot/
#  + https://matplotlib.org/api/_as_gen/matplotlib.pyplot.margins.html
#  + https://stackoverflow.com/questions/6774086/why-is-my-xlabel-cut-off-in-my-matplotlib-plot
#  + https://matplotlib.org/gallery/pyplots/dollar_ticks.html
#  + https://stackoverflow.com/questions/38152356/matplotlib-dollar-sign-with-thousands-comma-tick-labels
#  + https://pbpython.com/effective-matplotlib.html#customizing-the-plot
#  + https://matplotlib.org/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots

chart_title = "Top Selling Products (March 2018)" #TODO: get month and year

sorted_products = []
sorted_sales = []

for d in top_sellers:
    sorted_products.append(d["name"])
    sorted_sales.append(d["monthly_sales"])

# reverse the order of both because we want to display top-sellers at the top:
sorted_products.reverse()
sorted_sales.reverse()

# this section needs to come before the chart construction
fig, ax = plt.subplots() # enables us to further customize the figure and/or the axes
usd_formatter = ticker.FormatStrFormatter('$%1.0f')
ax.xaxis.set_major_formatter(usd_formatter)

# chart construction
plt.barh(sorted_products, sorted_sales)
plt.title(chart_title)
plt.xlabel("Product")
plt.ylabel("Monthly Sales (USD)")

plt.tight_layout() # ensures all areas of the chart are visible by default (fixes labels getting cut off)
plt.show()

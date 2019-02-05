# monthly_sales.py

import os
import pandas
import plotly
from plotly import graph_objs

# utility function to convert float or integer to usd-formatted string (for printing)
# ... adapted from: https://github.com/s2t2/shopping-cart-screencast/blob/30c2a2873a796b8766e9b9ae57a2764725ccc793/shopping_cart.py#L56-L59
def to_usd(my_price):
    return "${0:,.2f}".format(my_price) #> $12,000.71

#
# INPUTS
#

csv_filename = "sales-201803.csv" # TODO: allow user to specify

# reference a file in the "data" directory
# ... adapted from: https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/modules/os.md#file-operations
csv_filepath = os.path.join(os.path.dirname(__file__), "data", csv_filename)

# read csv file into a pandas dataframe object
# ... this and other pandas operations adapted from: https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/packages/pandas.md
csv_data = pandas.read_csv(csv_filepath)

#
# CALCULATIONS
#

monthly_total = csv_data["sales price"].sum()

# google search for "pandas group by" leads to...
# ... https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html
product_totals = csv_data.groupby(["product"]).sum()

# google search for "pandas dataframe order rows" leads to ...
# ... http://pandas.pydata.org/pandas-docs/version/0.19/generated/pandas.DataFrame.sort.html
product_totals = product_totals.sort_values("sales price", ascending=False)

# google search for "pandas loop through each row in a dataframe" results in ...
# ... https://stackoverflow.com/questions/16476924/how-to-iterate-over-rows-in-a-dataframe-in-pandas
# ... http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iterrows.html

top_sellers = []
rank = 1
for i, row in product_totals.iterrows():
    d = {"rank": rank, "name": row.name, "monthly_sales": row["sales price"]}
    top_sellers.append(d)
    rank = rank + 1

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
for d in top_sellers:
    print("  " + str(d["rank"]) + ") " + d["name"] + ": " + to_usd(d["monthly_sales"]))

print("-----------------------")
print("VISUALIZING THE DATA...")

# adapted from:
# ... https://plot.ly/python/bar-charts/
# ... https://plot.ly/python/getting-started
# ... https://plot.ly/python/getting-started/#initialization-for-offline-plotting
# ... https://plot.ly/python/horizontal-bar-charts/
# ... https://plot.ly/python/axes/#reversed-axes

chart_filename = "top-sellers-201803.html" # TODO: parse selected csv file name
chart_filepath = os.path.join(os.path.dirname(__file__), "reports", chart_filename)
#image_filename = "top-sellers-201803.png" # TODO: parse selected csv file name
#image_filepath = os.path.join(os.path.dirname(__file__), "images", image_filename) # looks like the image just gets downloaded
#image_filename = "top-sellers-201803" # TODO: parse selected csv file name

sorted_product_names = ['giraffes', 'orangutans', 'monkeys'] # TODO: get from csv data
sorted_product_sales = [23, 20, 14] # TODO: get from csv data

data = [
    graph_objs.Bar(
        x=sorted_product_sales,
        y=sorted_product_names,
        orientation = "h" # horizontal bar orientation
    )
]

chart_title = "Top Selling Products (March 2018)" # TODO: get month and year

layout = graph_objs.Layout(
    title=chart_title,
    yaxis=dict(autorange="reversed") # make sure top sellers are on the top
)

chart_options = {"data": data, "layout": layout}

plotly.offline.plot(
    chart_options,
    filename=chart_filepath,
    #image="png",
    #image_filename=image_filename, # is it possible to specify a filepath?
    auto_open=True
)

# monthly_sales.py

import os
import pandas

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

# print(type(csv_data)) #> <class 'pandas.core.frame.DataFrame'>
# print(csv_data)
# print(list(csv_data.columns)) #> ['date', 'product', 'unit price', 'units sold', 'sales price']

#
# CALCULATIONS
#

monthly_total = csv_data["sales price"].sum()

top_sellers = [
    {"rank": 1, "name": "Button-Down Shirt", "monthly_sales": 6960.35},
    {"rank": 2, "name": "Super Soft Hoodie", "monthly_sales": 1875.00},
] # TODO: get from csv_data

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

# TODO: display bar chart of top sellers

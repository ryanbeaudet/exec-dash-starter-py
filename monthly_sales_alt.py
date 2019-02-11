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

#
# CALCULATIONS
#

monthly_total = csv_data["sales price"].sum()

top_sellers = [
    {"name": "Button-Down Shirt", "monthly_sales": 6960.34},
    {"name": "Super Soft Hoodie", "monthly_sales": 1875.0},
    {"name": "Khaki Pants", "monthly_sales": 1602.0},
    {"name": "Vintage Logo Tee", "monthly_sales": 941.05},
    {"name": "Brown Boots", "monthly_sales": 250.0},
    {"name": "Sticker Pack", "monthly_sales": 216.0},
    {"name": "Baseball Cap", "monthly_sales": 156.31}
] # TODO: get from CSV data instead
#
# breakpoint()

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

# TODO: make a chart
#
# adapted from code posted to matplotlib Slack channel: https://georgetown-opim-py.slack.com/archives/CFZDKNKA4/p1549494877005200
#
# import matplotlib.pyplot as plt
#
# bar_data = [
#     {"genre": "Thriller", "viewers": 123456},
#     {"genre": "Mystery", "viewers": 234567},
#     {"genre": "Sci-Fi", "viewers": 987654},
#     {"genre": "Fantasy", "viewers": 876543},
#     {"genre": "Documentary", "viewers": 283105},
#     {"genre": "Action", "viewers": 544099},
#     {"genre": "Romantic Comedy", "viewers": 121212}
# ]
#
# genres = []
# viewers = []
#
# for s in bar_data:
#   genres.append(s["genre"])
#   viewers.append(s["viewers"])
#
# plt.bar(genres, viewers)
# plt.ylabel("Viewers")
# plt.xlabel("Genre")
# plt.show()

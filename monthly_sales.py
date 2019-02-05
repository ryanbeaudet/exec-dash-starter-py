# monthly_sales.py

# utility function to convert float or integer to usd-formatted string (for printing)
# source: https://github.com/s2t2/shopping-cart-screencast/blob/30c2a2873a796b8766e9b9ae57a2764725ccc793/shopping_cart.py#L56-L59
def to_usd(my_price):
    return "${0:,.2f}".format(my_price) #> $12,000.71

#
# INPUTS
#

sales = [] # TODO: read csv file

#
# CALCULATIONS
#

monthly_total = 12000.71 # TODO: get from sales data

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
print("  1) Button-Down Shirt: $6,960.35")
print("  2) Super Soft Hoodie: $1,875.00")
print("  3) etc.") # TODO: get top sellers

print("-----------------------")
print("VISUALIZING THE DATA...")

# TODO: display bar chart of top sellers

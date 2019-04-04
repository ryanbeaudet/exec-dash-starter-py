
import operator
import os
import pandas
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

from app.utils import to_usd

# expects "sales_data" to be a pandas dataframe with headers: "product", "sales price", etc.
def top_selling_products(sales_data):
    product_names = sales_data["product"]
    unique_product_names = product_names.unique()
    unique_product_names = unique_product_names.tolist() # converts numpy.ndarray to list
    top_sellers = []
    for product_name in unique_product_names:
        matching_rows = sales_data[sales_data["product"] == product_name]
        product_monthly_sales = matching_rows["sales price"].sum()
        top_sellers.append({"name": product_name, "monthly_sales": product_monthly_sales})
    top_sellers = sorted(top_sellers, key=operator.itemgetter("monthly_sales"), reverse=True)
    return top_sellers

if __name__ == "__main__":

    # INPUTS

    csv_filename = "sales-201803.csv" # TODO: allow user to specify

    csv_filepath = os.path.join(os.path.dirname(__file__), "..", "data", csv_filename)

    csv_data = pandas.read_csv(csv_filepath)

    # CALCULATIONS

    monthly_total = csv_data["sales price"].sum()

    top_sellers = top_selling_products(csv_data)

    # OUTPUTS

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
    plt.ylabel("Product")
    plt.xlabel("Monthly Sales (USD)")

    plt.tight_layout() # ensures all areas of the chart are visible by default (fixes labels getting cut off)
    plt.show()

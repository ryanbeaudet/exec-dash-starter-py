
import os
import pandas
import plotly
from plotly import graph_objs

from app.utils import to_usd

def top_selling_products(sales_data):
    return [1,2,3]

if __name__ == "__main__":

    # INPUTS

    csv_filename = "sales-201803.csv" # TODO: allow user to specify

    csv_filepath = os.path.join(os.path.dirname(__file__), "..", "data", csv_filename)

    csv_data = pandas.read_csv(csv_filepath)

    # CALCULATIONS

    monthly_total = csv_data["sales price"].sum()

    product_totals = csv_data.groupby(["product"]).sum()

    product_totals = product_totals.sort_values("sales price", ascending=False)

    top_sellers = []
    rank = 1
    for i, row in product_totals.iterrows():
        d = {"rank": rank, "name": row.name, "monthly_sales": row["sales price"]}
        top_sellers.append(d)
        rank = rank + 1

    breakpoint() # what do we expect here?
    #> [{'rank': 1, 'name': 'Button-Down Shirt', 'monthly_sales': 6960.3499999999985}, {'rank': 2, 'name': 'Super Soft Hoodie', 'monthly_sales': 1875.0}, {'rank': 3, 'name': 'Khaki Pants', 'monthly_sales': 1602.0}, {'rank': 4, 'name': 'Vintage Logo Tee', 'monthly_sales': 941.0500000000001}, {'rank': 5, 'name': 'Brown Boots', 'monthly_sales': 250.0}, {'rank': 6, 'name': 'Sticker Pack', 'monthly_sales': 216.0}, {'rank': 7, 'name': 'Baseball Cap', 'monthly_sales': 156.31}]

    # OUTPUTS

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

    sorted_product_names = [d["name"] for d in top_sellers] # list comprehension for mapping purposes!
    sorted_product_sales = [d["monthly_sales"] for d in top_sellers] # list comprehension for mapping purposes!
    sorted_bar_labels = [to_usd(d["monthly_sales"]) for d in top_sellers] # list comprehension for mapping purposes!

    data = [
        graph_objs.Bar(
            x=sorted_product_sales,
            y=sorted_product_names,
            orientation="h", # orients bars horizontally
            text=sorted_bar_labels, # display bar label (USD-formatted string version of the product sales)
            textposition= "auto", # I prefer "outside", but it causes the label on the biggest bar to get cut off
            hoverinfo="text" # prevents duplication of sales price in hover text
        )
    ]

    chart_title = "Top Selling Products (March 2018)" # TODO: get month and year

    layout = graph_objs.Layout(
        title=chart_title,
        xaxis=dict(tickformat="$"), # thought it might be possible to format USD here... # "${:,.0f}" # "${0:,.2f}" # ",.2f" # "$$$$$$$" # "${0:,.2f}" # ".2%"
        yaxis=dict(autorange="reversed"), # ensures top sellers are on the top
        margin=graph_objs.layout.Margin(l=150, pad=20) # ensures we can see the full product names
    )

    chart_options = {"data": data, "layout": layout}

    chart_filename = "top-sellers-201803.html" # TODO: parse selected csv file name
    chart_filepath = os.path.join(os.path.dirname(__file__), "..", "reports", chart_filename)

    plotly.offline.plot(
        chart_options,
        filename=chart_filepath,
        #image="png",
        #image_filename="top-sellers-201803", # prefer to download image file into this repo, but download location seems to not be customizable
        auto_open=True
    )

    print("-----------------------")
    print("SAVED REPORT TO: " + chart_filepath)

# exec-dash-starter-py

A starter repository for the "Executive Dashboard" project.

## Prerequisites

  + Anaconda 3.7
  + Python 3.7
  + Pip

## Installation

Fork this [starter project repository](https://github.com/prof-rossetti/exec-dash-starter-py) under your own control, then clone or download the resulting repository onto your computer. Then navigate there from the command line:

```sh
cd exec-dash-starter-py
```

Use Anaconda to create and activate a new virtual environment, perhaps called "dashboard-env". From inside the virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
```

## Usage

Process monthly sales data to generate a report of business insights:

```sh
python monthly_sales.py

# see also this alternative approach:
python monthly_sales_alt.py
```

Sample information outputs:

```py
#> -----------------------
#> MONTH: March 2018
#> -----------------------
#> CRUNCHING THE DATA...
#> -----------------------
#> TOTAL MONTHLY SALES: $12,000.71
#> -----------------------
#> TOP SELLING PRODUCTS:
#>   1) Button-Down Shirt: $6,960.35
#>   2) Super Soft Hoodie: $1,875.00
#>   3) Khaki Pants: $1,602.00
#>   4) Vintage Logo Tee: $941.05
#>   5) Brown Boots: $250.00
#>   6) Sticker Pack: $216.00
#>   7) Baseball Cap: $156.31
#> -----------------------
#> VISUALIZING THE DATA...
#> -----------------------
#> SAVED REPORT TO: reports/top-sellers-201803.html
```

Example chart:

![example bar chart of top-selling products](/images/top-sellers-201803.png)

Alternative chart:

![example bar chart of top-selling products](/images/top-sellers-201803-alt.png)

## Testing

From within the virtual environment, install the `pytest` package (first time only):

```sh
pip install pytest
```

Run tests:

```sh
pytest --disable-pytest-warnings # suppresses warnings thrown by matplotlib during testing
```

## [License](/LICENSE.md)

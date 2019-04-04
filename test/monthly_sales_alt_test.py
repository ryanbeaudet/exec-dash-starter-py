

from app.monthly_sales_alt import to_usd, top_selling_products

def test_to_usd():
    # it should apply USD formatting
    assert to_usd(4.50) == "$4.50"

    # it should display two decimal places
    assert to_usd(4.5) == "$4.50"

    # it should round to two places
    assert to_usd(4.55555) == "$4.56"

    # it should display thousands separators
    assert to_usd(1234567890.5555555) == "$1,234,567,890.56"

def test_top_selling_products():
    # it should return a list of names and sales totals, sorted by sales ascending with top sellers first:
    expected_result = [
        {'name': 'Button-Down Shirt', 'monthly_sales': 6960.35},
        {'name': 'Super Soft Hoodie', 'monthly_sales': 1875.0},
        {'name': 'Khaki Pants', 'monthly_sales': 1602.0},
        {'name': 'Vintage Logo Tee', 'monthly_sales': 941.0500000000001},
        {'name': 'Brown Boots', 'monthly_sales': 250.0},
        {'name': 'Sticker Pack', 'monthly_sales': 216.0},
        {'name': 'Baseball Cap', 'monthly_sales': 156.31}
    ]
    assert top_selling_products() == expected_result

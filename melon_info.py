"""Print out all the melons in our inventory."""
melon_info = {
    'Honeydew': [True, 0.99],
    'Crenshaw': [False, 2.00],
    'Crane': [False, 2.50],
    'Casaba': [False, 2.50],
    'Cantaloupe': [False, 0.99]
}


def print_melon(melon_info):
    """Print each melon with corresponding attribute information."""
    for name, attributes in melon_info.items():
    	seedless, price = attributes
    	print(name.upper(), seedless, price)
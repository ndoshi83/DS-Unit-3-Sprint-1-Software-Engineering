# Import required libraries
from random import randint, sample, uniform
from acme import Product

# Create list of adjectives and nouns
adj = ['Awesome','Shiny','Impressive','Portable','Improved']
nns = ['Anvil','Catapult','Disguise','MouseTrap','Rocket']

# Create function to create product inventory
def generate_products(num_products = 30):
    # Create blank list of products
    products = []
    
    for i in range(num_products):
        # Create name using adjectives and nouns
        a = sample(adj, 1)
        n = sample(nns, 1)
        prod_name = str(a[0]),' ',str(n[0])

        # Create price and weight 
        prod_price = randint(5,100)
        prod_weight = randint(5, 100)

        # Create flammability
        prod_flammability = uniform(0.0, 2.5)

        # Append created product to product list
        products.append(Product(prod_name, prod_price, prod_weight, prod_flammability))

    # Return generated product list
    return products

# Create function for inventory summary report
def inventory_report(products):
    # Print title of the report
    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    # Determine unique names
    unique_names = {prod.name for prod in products}
    # Print unique name count
    print('Unique product names:', len(unique_names))
    # Determine average price
    prices = list(prod.price for prod in products)
    # Print average price
    print('Average price:', sum(prices)/len(prices))
    # Determine average weight
    weights = list(prod.weight for prod in products)
    # Print average price
    print('Average weight:', sum(weights)/len(weights))
    # Determine average flammability
    flams = list(prod.flammability for prod in products)
    # Print average price
    print('Average flammability:', sum(flams)/len(flams))

# Testing code
if __name__ == '__main__':
    inventory_report(generate_products())
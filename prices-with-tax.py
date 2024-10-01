# 1. Define the function to calculate price including 19% VAT
def price_with_tax(article_price):
    vat_rate = 0.19
    total_price = article_price + (article_price * vat_rate)
    return total_price

# 2. Call the function for article_price = 99.99 and article_price = 1.99 and print the results
print("Total price for 99.99 Euro article:", price_with_tax(99.99))
print("Total price for 1.99 Euro article:", price_with_tax(1.99))


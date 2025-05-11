total_stocks = 0
prices = []

def calculate_average(stocks, total_prices):
    average_price = sum(total_prices) / stocks
    return average_price


while True:
    total_stock_batch_price = 0 # Resets average stock batch price
    stock = input("Enter number of stocks ('done' to stop): ")
    if stock == "done":
        print(f"Your average stocks price is : ${calculate_average(total_stocks, prices):.2f}")       
        break
    else:
        price = float(input("Enter the stock price: "))
        total_stock_batch_price = int(stock) * price
        total_stocks += int(stock)
        prices.append(total_stock_batch_price)




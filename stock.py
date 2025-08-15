stock_prices = {"AAPL": 180.00, "TSLA": 250.50, "MSFT": 320.75, "GOOG": 135.25, "AMZN": 145.10}
user_portfolio = {}
print("Welcome to the stock portfolio tracker!")
print("available stocks:AAPL,TSLA,MSFT,GOOG,AMZN")
while True:
    stock_name = input("enter a stock ticker(eg,AAPL) or type 'done' to finish:").upper()
    if stock_name == "DONE":
        break
    if stock_name in stock_prices:
        try:
            quantity = int(input(f"enter the quantity for{stock_name}:"))
            user_portfolio[stock_name] = quantity
            print(f"added{quantity} shares of{stock_name} to your portfolio.")
        except ValueError:
            print("invalid quantity. Please enter a whole number")
    else:
        print("stock not found. Plese try again!")
total_investment = 0
print("\n---your portfolio summary---")
for stock,quantity in user_portfolio.items():
    price = stock_prices[stock]
    value = price*quantity
    total_investment += value
    print(f"stock:{stock},quantity:{quantity},price:${price:.2f},value.${value:.2f}")
print("-" * 30)
print(f"total portfolio value:${total_investment:.2f}")
try:
    with open("portfolio_summary.txt","w") as file:
        file.write("---your portfolio summary ---\n")
        for stock,quantity in user_portfolio.items():
            price=stock_prices[stock]
            value = price*quantity
            file.write(f"stock:{stock},quantity:{quantity}, price:${price:.2f}, value:${value:.2f}\n")
        file.write("-" * 30 + "\n")
        file.write(f"total portfolio value:${total_investment:.2f}\n")
    print("\nResults have been successfully saved to 'portfolio_summary.txt'.")
except IOError:
    print("\nError: could not write to file.")

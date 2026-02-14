# Stock Portfolio Tracker

# Predefined stock prices (Hardcoded Dictionary)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320
}

portfolio = {}
total_investment = 0

print("📊 Welcome to Stock Portfolio Tracker")
print("Available Stocks and Prices:")

for stock, price in stock_prices.items():
    print(f"{stock} : ₹{price}")

print("\nType 'done' to finish.\n")

while True:
    stock_name = input("Enter stock name: ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Stock not available. Please choose from the list.\n")
        continue

    quantity = int(input("Enter quantity: "))

    # Save in portfolio dictionary
    portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

# Calculate total investment
for stock, quantity in portfolio.items():
    investment = stock_prices[stock] * quantity
    total_investment += investment
    print(f"{stock} ({quantity} shares) = ₹{investment}")

print("\n------------------------------")
print(f"Total Investment Value = ₹{total_investment}")
print("------------------------------")

# Optional: Save to file
save = input("Do you want to save the result to a file? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        for stock, quantity in portfolio.items():
            file.write(f"{stock} ({quantity} shares)\n")
        file.write(f"\nTotal Investment Value = ₹{total_investment}")
    print("Result saved to portfolio.txt")

print("Thank you for using Stock Portfolio Tracker!")

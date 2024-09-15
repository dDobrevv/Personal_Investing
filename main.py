# Imports

# Asking for input

#ticker_symbol = input("Please enter a Stock Ticker: ") # Да добавя още, че инпута, трябва да е с главни букви САМО, но може евентуално да вземе инпута и да го трянсформира с главни букви...

# Calculations

# Output
#print(ticker_symbol)


#######################################################
# Website Scraper
import yfinance as yf

# Get ticker symbol from user input
ticker_symbol = input("Enter a stock ticker symbol: ")

# Create a Ticker object for the given symbol
ticker = yf.Ticker(ticker_symbol)

# Get detailed information about the stock
info = ticker.info

# Print the company name
print(f"Company Name: {info['longName']}")

# Print the current price
print(f"Current Price: {info['currentPrice']}")

# Print the 52-week high and low
print(f"52-Week High: {info['fiftyTwoWeekHigh']}")
print(f"52-Week Low: {info['fiftyTwoWeekLow']}")

# Print the market cap
print(f"Market Cap: {info['marketCap']}")

# Print the sector and industry
print(f"Sector: {info['sector']}")
print(f"Industry: {info['industry']}")

# Print the dividend yield
print(f"Dividend Yield: {info['dividendYield']}")

# Print the price-to-earnings ratio
print(f"Price-to-Earnings Ratio: {info['trailingPE']}")

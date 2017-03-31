import quandl

quandl.ApiConfig.api_key = "6jkjXtsDx-zYybXseD-5"
company = input("Enter Stock Symbol: ")

closingQuote = quandl.get("WIKI/" + company, rows=1)

print(closingQuote)

import quandl

quandl.ApiConfig.api_key = "##############" <-Your key
company = input("Enter Stock Symbol: ")

closingQuote = quandl.get("WIKI/" + company, rows=1)

print(closingQuote)

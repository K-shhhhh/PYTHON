# Q. FROM A GIVEN ARRAY [PRICE] AND EACH ELEMENT REPRESENTING THE PRICE OF STOCK THAT DAY, FIND MAXIMUM PROFIT AND IF NO PROFIT THEN RETURN 0

# LOGIC : ASSUMING EVERY DAY AS SELLING DAY AND THEN CHECKING DIFFERENCE IN PRICES FOR NEXT DAY AND UPDATING VALUES

n = int(input("Enter Number of days : "))
prices = []
for element in range(n):
    element = int(input(f"Enter stock price on. day {element + 1} : "))
    prices.append(element)

print(prices)

maxprofit = 0
bestbuy = prices[0]
for i in range(1,n):
    if prices[i] > bestbuy:
        maxprofit = max(maxprofit, prices[i] - bestbuy)
    bestbuy = min(bestbuy,prices[i])
print(f"maximum profit = {maxprofit}")
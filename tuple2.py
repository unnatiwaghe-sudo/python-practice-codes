prices = tuple(map(int, input("Enter prices separated by space: ").split()))

print("Total number of items sold:", len(prices))
print("Cheapest item price:", min(prices))
print("Costliest item price:", max(prices))
print("Prices in ascending order:", tuple(sorted(prices)))

costliest = max(prices)
count_costliest = prices.count(costliest)
print("Number of costliest items sold:", count_costliest)

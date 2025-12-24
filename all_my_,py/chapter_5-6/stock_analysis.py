
stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]







def price_at(x):
    return stock_prices[x-1]

print(price_at(8))



def max_price(a, b): 
  start = min(a, b)
  end = max(a, b)
  prices_in_range = [price_at(day) for day in range(start, end + 1)]
  max_price_value = max(prices_in_range)
  return max_price_value

print((max_price(1,9)))

def min_price(a,b):
  start = min(a,b)
  end = max(a,b)
  prices_in_range = [price_at(day) for day in range(start, end + 1)]
  min_price_value = min(prices_in_range)
  return min_price_value
  
print((min_price(1,9)))
  

  










  
  
    
    


  








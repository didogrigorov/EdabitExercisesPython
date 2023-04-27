def profit(info):
    real_win = info["sell_price"] - info["cost_price"]
    total = real_win * info["inventory"]
    return round(total)


print(profit({
  "cost_price": 32.67,
  "sell_price": 45.00,
  "inventory": 1200
}))
# Input
lily_age = int(input())
washer_price = float(input())
single_toy_price = int(input())

# Actions
toys_cnt = 0
total_money_saved = 0

# For loop will simulate Lily's life
for curr_age in range(1, lily_age + 1):
    if curr_age % 2 != 0:
        # Odd age
        toys_cnt += 1
    else:
        # Even age, 2 -> 10, 4 -> 20, 6 -> 30, 8 -> 40
        # Here we subtract 1 because her brother takes 1 lev every time
        money_given = (curr_age * 5) - 1
        total_money_saved += money_given

# At the end we sell our toys and add the sum to the money saved
toys_money = toys_cnt * single_toy_price
total_money_saved += toys_money

# Output
if total_money_saved >= washer_price:
    money_left = total_money_saved - washer_price
    print(f'Yes! {money_left:.2f}')
else:
    money_more_needed = washer_price - total_money_saved
    print(f'No! {money_more_needed:.2f}')
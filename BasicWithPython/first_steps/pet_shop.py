dog_food_count = int(input())
cat_food_count = int(input())
dog_food_total_price = dog_food_count * 2.5 #1 packet -> 2.50
cat_food_total_price = cat_food_count * 4.00 #1packet -> 4.00
total = cat_food_total_price + dog_food_total_price
print(f"{total} lv.")
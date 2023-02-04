square_metres = float(input())
price_without_discount = square_metres * 7.61 #1 square metre -> 7.61
discount = price_without_discount * 0.18
total_price = price_without_discount - discount
#•	"The final price is: {крайна цена на услугата} lv."
#"The discount is: {отстъпка} lv."
print(f"The final price is: {total_price} lv.")
print(f"The discount is: {discount} lv.")
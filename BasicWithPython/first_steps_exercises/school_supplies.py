# •	Брой пакети химикали - цяло число в интервала [0...100]
# •	Брой пакети маркери - цяло число в интервала [0...100]
# •	Литри препарат за почистване на дъска - цяло число в интервала [0…50]
# •	Процент намаление - цяло число в интервала [0...100]
count_pen = int(input())
count_markers = int(input())
preparation_liters = int(input())
discount = int(input())
# •	Пакет химикали - 5.80 лв.
# •	Пакет маркери - 7.20 лв.
# •	Препарат - 1.20 лв (за литър
total_pen = count_pen * 5.80
total_markers = count_markers * 7.20
total_preparation = preparation_liters * 1.20
total_price_without_discount = total_pen + total_markers + total_preparation
total_price = total_price_without_discount - (total_price_without_discount * (discount / 100))
print(total_price)

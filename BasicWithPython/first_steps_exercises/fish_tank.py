# 1.	Дължина в см – цяло число в интервала [10 … 500]
# 2.	Широчина в см – цяло число в интервала [10 … 300]
# 3.	Височина в см – цяло число в интервала [10… 200]
# 4.	Процент  – реално число в интервала [0.000 … 100.000]
length = int(input())
width = int(input())
height = int(input())
percent = float(input())
volume = length * width * height
volume_in_liters = volume / 1000
occupied_space = percent / 100
needed_liters = volume_in_liters * (1 - occupied_space)
print(needed_liters)

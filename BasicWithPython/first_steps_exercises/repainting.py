# 1.	Необходимо количество найлон (в кв.м.) - цяло число в интервала [1... 100]
# 2.	Необходимо количество боя (в литри) - цяло число в интервала [1…100]
# 3.	Количество разредител (в литри) - цяло число в интервала [1…30]
# 4.	Часовете, за които майсторите ще свършат работата - цяло число в интервала [1…9]
nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())
# •	Предпазен найлон - 1.50 лв. за кв. метър
# •	Боя - 14.50 лв. за литър
# •	Разредител за боя - 5.00 лв. за литър
more_paint = paint * (10/100)
total_paint = (paint + more_paint) * 14.50
total_nylon = (nylon + 2) * 1.50
total_thinner = thinner * 5.00
bags = 0.40
total_materials = total_nylon + total_paint + total_thinner + bags
sum_for_workers = (total_materials * 30/100) * hours
total_sum = total_materials + sum_for_workers
print(total_sum)
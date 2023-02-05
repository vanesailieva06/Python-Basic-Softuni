# 1.	Брой страници в текущата книга – цяло число в интервала [1…1000]
# 2.	Страници, които прочита за 1 час – цяло число в интервала [1…1000]
# 3.	Броят на дните, за които трябва да прочете книгата – цяло число в интервала [1…1000]
pages = int(input())
pages_for_one_hour = int(input())
days_to_read = int(input())

total_time = pages // pages_for_one_hour
needed_hours = total_time // days_to_read

print(needed_hours)

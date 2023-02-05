# 1.	Депозирана сума – реално число в интервала [100.00 … 10000.00]
# 2.	Срок на депозита (в месеци) – цяло число в интервала [1…12]
# 3.	Годишен лихвен процент – реално число в интервала [0.00 …100.00]
deposit_sum = float(input())
deposit_term = int(input())
interest_percent = float(input())

#сума = депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)
interest = deposit_sum * interest_percent / 100
total_sum = deposit_sum + deposit_term * (interest / 12)

print(total_sum)

year_tax = int(input())
# •	Баскетболни кецове – цената им е 40% по-малка от таксата за една година
# •	Баскетболен екип – цената му е 20% по-евтина от тази на кецовете
# •	Баскетболна топка – цената ѝ е 1 / 4 от цената на баскетболния екип
# •	Баскетболни аксесоари – цената им е 1 / 5 от цената на баскетболната топка
basketball_trainers = year_tax - (year_tax * 0.4)
basketball_equipment = basketball_trainers - (basketball_trainers * 0.2)
ball = 1 /4 * basketball_equipment
basketball_accessories = 1 / 5 * ball
total_cost = year_tax + basketball_accessories + ball + basketball_trainers + basketball_equipment
print(total_cost)

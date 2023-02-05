chicken_menus = int(input())
fish_menus = int(input())
vegetarian_menus = int(input())
# •	Пилешко меню –  10.35 лв.
# •	Меню с риба – 12.40 лв.
# •	Вегетарианско меню  – 8.15 лв.
total_chicken_menu = chicken_menus * 10.35
total_fish_menu = fish_menus * 12.40
total_vegetarian_menu = vegetarian_menus * 8.15
total_menus_price = total_fish_menu + total_chicken_menu + total_vegetarian_menu
dessert = total_menus_price * 20/100
delivery = 2.50
total_price = total_menus_price + delivery + dessert
print(total_price)

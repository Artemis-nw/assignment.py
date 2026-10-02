number_of_posters = int(input("Enter the number of posters: "))
student = input("Are you a student? (yes/no): ")
money = int(input("Enter the money you have: "))
if student == "yes" and number_of_posters >= 6:
    price_per_poster = 7
elif student == "yes" and number_of_posters < 6:
    price_per_poster = 9
elif student == "no" and number_of_posters >= 6:
    price_per_poster = 9
else:
    price_per_poster = 11
total_cost = number_of_posters * price_per_poster
print(f"Price per poster: {price_per_poster}")
print(f"Total cost: {total_cost}")
if money > total_cost:
    money_left = money - total_cost
    print(f"Money left: {money_left}")
elif money == total_cost:
    print("Exactly enough money")
else:
    more_money_needed = total_cost - money
    print(f"More money needed: {more_money_needed}")

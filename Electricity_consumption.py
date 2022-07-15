delivery_company  = str(input("Доставчик: "))

if delivery_company == "EVN":
    day = 0.14433
    night = 0.05812
elif delivery_company  == "ЧЕЗ":
    day = 0.14666
    night = 0.06245
elif delivery_company  == "Енерго Про":
    day = 0.14778
    night = 0.05787
else:
    print("Нещо обърка доставчика пич.")

consume_12h = int(input("Въведи дни на консумация: \n"
                        "(всеки ден се смята за 24 часа - 12ч дневна и 12ч нощна тарифа): ")) * 12
kilo_watts = int(input("Вата: ")) / 1000
kW_h = consume_12h * kilo_watts
daily = kW_h * day
nightly = kW_h * night

totall = daily + nightly
print(f"{totall:.2f} лева")
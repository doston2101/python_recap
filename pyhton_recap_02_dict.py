savdo = {
    "Toshkent": {
        "Laptop": {"price": 5000000, "quantity": 12},
        "Phone": {"price": 3000000, "quantity": 20},
        "Monitor": {"price": 1500000, "quantity": 15}
    },

    "Samarqand": {
        "Laptop": {"price": 5000000, "quantity": 8},
        "Phone": {"price": 3000000, "quantity": 25},
        "Tablet": {"price": 2000000, "quantity": 10}
    },

    "Buxoro": {
        "Laptop": {"price": 5000000, "quantity": 5},
        "Monitor": {"price": 1500000, "quantity": 20},
        "Tablet": {"price": 2000000, "quantity": 7}
    },

    "Andijon": {
        "Phone": {"price": 3000000, "quantity": 18},
        "Monitor": {"price": 1500000, "quantity": 12},
        "Tablet": {"price": 2000000, "quantity": 15}
    }
}

# Vazifalar
# 1-qism. Dictionary bilan ishlash

# 1. Barcha filial nomlarini chiqar.
print(list(savdo.keys()))
print('------------------')

# 2. Toshkent filialidagi barcha mahsulotlarni chiqar.
print(savdo.get("Toshkent",{}))
print('------------------')

# 3. Samarqand filialidagi Laptop miqdorini chiqar.

print(savdo.get("Samarqand", {}).
      get("Laptop", {}).
      get('quantity',"0" ))
print('------------------')

# 4. Buxoro filialiga Keyboard mahsulotini qo‘sh:
#    - price = 500000
#    - quantity = 10

savdo["Buxoro"]["Keyboard"] = {
    'price' : 500000,
    'quantity' : 10
}
print(savdo.get("Buxoro", {})
      .get("Keyboard", {}))
print('------------------')

#5. Andijondagi Phone miqdorini 18 dan 25 ga o‘zgartir.
savdo["Andijon"]["Phone"]["quantity"] = 24
print(savdo.get("Andijon", {})
      .get("Phone", {})
      .get("quantity",""))
print('------------------')

# 2-usul update metodi bilan
savdo["Andijon"]["Phone"].update({"quantity": 25})
print(f'2 usul :')
print(savdo.get("Andijon", {})
      .get("Phone", {})
      .get("quantity", {}))
print('------------------')

# 6. Toshkentdagi Monitor mahsulotini uchir.

del savdo["Toshkent"]['Monitor']
print(savdo.get("Toshkent", {}))

# 2 usul pop metodi bilan
savdo["Toshkent"].pop("Monitor")
print(savdo.get("Toshkent", {}))

print('------------------')

# 7. get() orqali Namangan filiali mavjudligini xavfsiz tekshir.
print(savdo.get("Namangan", {}))

# 2-qism. Revenue Calculation (Tushumni hisoblash — Расчёт выручки)

# 1. Har bir mahsulotning tushumini hisobla.
print(f'Toshkent')

savdo["Toshkent"]["Laptop"]["revenue"] =(
    savdo["Toshkent"]["Laptop"]["price"]*
    savdo["Toshkent"]["Laptop"]["quantity"])

savdo["Toshkent"]["Phone"]["revenue"] = (
    savdo["Toshkent"]["Phone"]["price"]*
    savdo["Toshkent"]["Phone"]["quantity"]
)

savdo["Toshkent"]["Monitor"]["revenue"] = (
    savdo["Toshkent"]["Monitor"]["price"]*
    savdo["Toshkent"]["Monitor"]["quantity"]
)

print(f'Samarqand')
savdo["Samarqand"]["Laptop"]["revenue"] =(
    savdo["Samarqand"]["Laptop"]["price"]*
    savdo["Samarqand"]["Laptop"]["quantity"]
    )
savdo["Samarqand"]["Phone"]["revenue"] = (
    savdo["Samarqand"]["Phone"]["price"]*
    savdo["Samarqand"]["Phone"]["quantity"]
)
savdo["Samarqand"]["Tablet"]["revenue"] = (
    savdo["Samarqand"]["Tablet"]["price"]*
    savdo["Samarqand"]["Tablet"]["quantity"]
)

print(f'Buxoro')
savdo["Buxoro"]["Laptop"]["revenue"] =(
    savdo["Buxoro"]["Laptop"]["price"]*
    savdo["Buxoro"]["Laptop"]["quantity"]
)
savdo["Buxoro"]["Monitor"]["revenue"] =(
    savdo["Buxoro"]["Monitor"]["price"]*
    savdo["Buxoro"]["Monitor"]["quantity"]
)
savdo["Buxoro"]["Tablet"]["revenue"] =(
    savdo["Buxoro"]["Tablet"]["price"]*
    savdo["Buxoro"]["Tablet"]["quantity"]
)

print(f'Andijon')
savdo["Andijon"]["Phone"]["revenue"] =(
    savdo["Andijon"]["Phone"]["price"]*
    savdo["Andijon"]["Phone"]["quantity"]
)
savdo["Andijon"]["Monitor"]["revenue"] =(
    savdo["Andijon"]["Monitor"]["price"]*
    savdo["Andijon"]["Monitor"]["quantity"]
)
savdo["Andijon"]["Tablet"]["revenue"] =(
    savdo["Andijon"]["Tablet"]["price"]*
    savdo["Andijon"]["Tablet"]["quantity"]
)
print(savdo)
print('-------------------------------------------------')

# 2. Hisoblangan tushumni mahsulotning ichki
# Dictionary'siga revenue nomi bilan qo‘sh.

print(savdo)
print('-------------------------------------------------')

# 3. Har bir filialning umumiy tushumini alohida hisobla.

total_revenue_toshken = (
    savdo["Toshkent"]["Laptop"]["revenue"]+
    savdo["Toshkent"]["Phone"]["revenue"]+
    savdo["Toshkent"]["Monitor"]["revenue"]
    )

total_revenue_samarqand = (
    savdo["Samarqand"]["Laptop"]["revenue"]+
    savdo["Samarqand"]["Phone"]["revenue"]+
    savdo["Samarqand"]["Tablet"]["revenue"]
    )

total_revenue_buxoro = (
    savdo["Buxoro"]["Laptop"]["revenue"]+
    savdo["Buxoro"]["Monitor"]["revenue"]+
    savdo["Buxoro"]["Tablet"]["revenue"]
)
total_revenue_andijon = (
    savdo["Andijon"]["Phone"]["revenue"]+
    savdo["Andijon"]["Monitor"]["revenue"]+
    savdo["Andijon"]["Tablet"]["revenue"]
)
print(total_revenue_andijon)
print(f'/*/*/*/*/*/*/*')
print(f'Toshkent: {total_revenue_toshken}''\n'
      f'Samarqand: {total_revenue_samarqand}''\n'
      f'Buxoro: {total_revenue_buxoro}''\n'
      f'Andijon: {total_revenue_andijon}')
print('-------------------------------------------------')
# 3-qism. Total Revenue (Umumiy tushum — Общая выручка)
# 1. Barcha filiallar tushumini qo‘sh.

total_revenue_sum = (total_revenue_toshken+
                     total_revenue_samarqand+
                     total_revenue_buxoro+
                     total_revenue_andijon)
print(f'barcha filyallar buyicha tushum summasi :{total_revenue_sum}')
print('-------------------------------------------------')

# 2. Kompaniyaning umumiy tushumini total_revenue o‘zgaruvchisida saqla.

print(f'barcha filyallar buyicha tushum summasi :{total_revenue_sum}')
print('-------------------------------------------------')

# 3. Eng ko‘p tushum keltirgan filialni aniqlashga tayyorla.

branch_revenue = {
    "Toshkent": total_revenue_toshken,
    "Samarqand": total_revenue_samarqand,
    "Buxoro": total_revenue_buxoro,
    "Andijon":total_revenue_andijon
}

max_revenue = max(branch_revenue.values())
print(max_revenue)

print('-------------------------------------')
# 4-qism. Revenue Share (Tushumdagi ulush — Доля в выручке)

# 1. Har bir filialning umumiy tushumdagi foiz ulushini hisobla.
share_toshkent = (total_revenue_toshken/total_revenue_sum) * 100
share_samarqand = (total_revenue_samarqand/total_revenue_sum) * 100
share_buxoro = (total_revenue_buxoro/total_revenue_sum) * 100
share_andijon = (total_revenue_andijon/total_revenue_sum) * 100
print(f'Toshken : {share_toshkent:.2f}%''\n'
      f'Samarqand: {share_samarqand:.2f}%''\n'
      f'Buxoro : {share_buxoro:.2f}%''\n'
      f'Andijon: {share_andijon:.2f}%')
# 2. Natijani branch_share nomi bilan saqla.

# 3. Barcha filiallar ulushini qo‘shganda taxminan 100% chiqishini tekshir.

print(f"barchasini 100% chiqagligini aniqlash: {share_toshkent +
                                                share_samarqand+
                                                share_buxoro+
                                                share_andijon}")

# 5-qism. Average Revenue (O‘rtacha tushum — Средняя выручка)
# 1. Kompaniyaning o‘rtacha filial tushumini hisobla.

total_revenue_count = (total_revenue_toshken,
                       total_revenue_samarqand,
                       total_revenue_buxoro,
                       total_revenue_andijon)

avg_revenue = total_revenue_sum/ len(total_revenue_count)
print(f'Kompaniyaning o‘rtacha filial tushumi: {avg_revenue}')

# 2. Har bir filialning o‘rtacha mahsulot tushumini hisobla.

avg_product_revenue = {}

avg_product_revenue["Toshkent"] = (total_revenue_toshken/
                                   len(savdo["Toshkent"]))
avg_product_revenue["Samarqand"] = (total_revenue_samarqand/
                                    len(savdo["Samarqand"]))
avg_product_revenue["Buxoro"] = (total_revenue_buxoro/
                                 len(savdo["Buxoro"]))
avg_product_revenue["Andijon"] = (total_revenue_andijon/
                                  len(savdo["Andijon"]))
print(f'Har bir filialning o‘rtacha mahsulot tushumi :{avg_product_revenue}')



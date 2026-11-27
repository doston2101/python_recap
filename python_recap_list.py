# """str_recap_01"""
#
# 1-daraja: 7/10 — Savdo ma'lumotlari
# Qiyinlik 7/10
# 1-topshiriq. Do‘kon daromadini hisoblash
#
# Do‘konda quyidagi mahsulotlar sotilgan:
# Mahsulot	Soni	Narxi
# Noutbuk	12	5 500 000
# Telefon	25	2 800 000
# Monitor	18	1 500 000
#
# Vazifalar:
# 1. Har bir mahsulotning umumiy tushumini hisobla.
# 2. Uchala mahsulotning jami tushumini top.
# 3. O‘rtacha tushumni hisobla.
# 4. Natijalarni int yoki float formatida chiqar.
# 5. Har bir o‘zgaruvchining type() qiymatini tekshir.
#from numpy.ma.core import count

#1
# product_01, product_02, product_03 =  "Noutbok", "telefon" , "Manitor"
# son_1, son_2, son_3 = 12, 25, 18
# narx_01, narx_02 , narx_03 = 5_500_000 , 2_800_000, 1_500_000
# #1
# sum_01 = son_1* narx_01
# sum_02 = son_2* narx_02
# sum_03 = son_3* narx_03
#
# #2
#
# total_revenue = sum_01 + sum_02 + sum_03
# print(total_revenue)
#
# #3
# avg_revenue = total_revenue / 3
# print(avg_revenue)
#
# #4
# print(type(total_revenue))
# print(type(avg_revenue))

#-------------------------#

# 2-topshiriq. Xodimlar ish haqi tahlili
#
# Kompaniyada uchta xodim bor:
# - Ali — 7 500 000 so‘m
# - Vali — 9 200 000 so‘m
# - Salim — 6 800 000 so‘m
# Vazifalar:
# 1. Jami ish haqi fondini hisobla.
# 2. O‘rtacha ish haqini top.
# 3. Eng yuqori va eng past maosh orasidagi farqni hisobla.
# 4. Har bir xodimning maoshini matn ko‘rinishida ham chiqar.

# Ali   = 7_500_000
# Vali  = 9_200_000
# Salim = 6_800_000
#
# total_revenue = Ali + Vali + Salim
# print(total_revenue)
#
# avg_total_revenue = total_revenue / 3
# print(avg_total_revenue)
#
# max_salary= max(Ali, Vali, Salim)
# print(max_salary)
#
# min_salary = min(Ali, Vali, Salim)
# print(min_salary)
#
# print(f"Ali salary: ", str(Ali))
# print(f"Vali salary: ", str(Vali))
# print(f"Salim: ", str(Salim))
#
# -------------------------
#
# Vazifalar:
# 1. Har bir savdo yozuvini ; orqali ajrating.
# 2. Hudud va mahsulot nomlarini tozalang.
# 3. Mahsulot narxi va sonini matematik hisoblash uchun tayyorlang.
# 4. Har bir savdo uchun tushumni hisoblang.
# 5. Barcha savdolarning umumiy tushumini toping.
# 6. Har bir hudud bo‘yicha tushumni aniqlang.
# 7. Eng ko‘p tushum keltirgan hududni toping.

#
# total_sales = [
#     "2026-01-01; Toshkent; Laptop; 5000000; 3",
#     "2026-01-02; Samarqand; Phone; 3000000; 5",
#     "2026-01-03; Buxoro; Tablet; 2000000; 4",
#     "2026-01-04; Toshkent; Monitor; 1500000; 6",
#     "2026-01-05; Samarqand; Laptop; 5000000; 2"
# ]
#
# result_sales : list = []
# print(total_sales)
# #1
# for i in range(len(total_sales)) :
#     result_sales.append(total_sales[i].split(";"))
#     print (result_sales[i])
#
# print("{:-^50}".format('#'))
#
# #2
# for i in range(len(result_sales)):
#     for j in range(len(result_sales[i])):
#         result_sales[i][j] = result_sales[i][j].strip()
#
# print("{:-^50}".format('#'))
# print(result_sales)
#
# #3
# for i in range(len(result_sales)):
#     result_sales[i][3] = int(result_sales[i][3])
#     result_sales[i][4] = int(result_sales[i][4])
#     print(result_sales[i])
#
# print("{:-^50}".format('#'))
# #4
# total_sales_product : dict={}
# for i in  range(len(result_sales)):
#     product = result_sales[i][2]
#     price = result_sales[i][3]
#     quantity = result_sales[i][4]
#
#     sum_sales_product= price * quantity
#
#     if product in total_sales_product:
#         total_sales_product[product] += sum_sales_product
#     else:
#         total_sales_product[product] = sum_sales_product
#
# def init
#
# print("{:-^50}".format('#'))
# print(total_sales_product)
#
# #5
# sum_sales_product = 0
# for i,j in total_sales_product.items():
#     sum_sales_product+=int(j)
#
# print("{:-^50}".format('#'))
# print(sum_sales_product)

#6
# Hisobot quyidagilarni ko‘rsatishi kerak:
# 1. Jami ma'lumotlar soni.
# 2. Haqiqiy savdolar soni.
# 3. Savdo bo‘lmagan kunlar soni.
# 4. Noto‘g‘ri (manfiy) ma'lumotlar soni.
# 5. Umumiy tushum.
# 6. O‘rtacha savdo qiymati.
# 7. Eng katta savdo.
# 8. Eng kichik musbat savdo.
# 9. 5 000 000 dan yuqori savdolar soni.
# 10. Umumiy tushumning nechta foizi eng katta 3 ta savdoga to‘g‘ri kelishi.
# Cheklovlar:
# - for va while ishlatish mumkin.
# - if, elif, else, break, continue ishlatish mumkin.
# - sum(), max(), min() tayyor funksiyalaridan foydalanma.
# - Barcha hisob-kitoblarni o‘zing bajar.


sales = [
    2500000, 4000000, 0, 6500000,
    3000000, -500000, 8000000, 4500000,
    0, 9000000, 5500000, 2000000,
    7500000, 1000000, 6000000
]
#
# print("{:-^50}".format('#'))
# print (len(sales))
# count_numbers = 0
# for i in range (len(sales)) :
#      count_numbers += 1
# print(count_numbers)
#
# count_numbers_02 = count(sales)
# print(count_numbers_02)
#
# print("{:-^50}".format('#'))
#
# count_numbers_03 = 0
# for i in range(len(sales)):
#     if sales[i] <=  0  :
#         continue
#     else :
#         count_numbers_03 += 1
#
# print(count_numbers_03)
#
# print("{:-^50}".format('#'))
# 3. Savdo bo‘lmagan kunlar soni.
#
# count_numbers_04 = 0
# sale_01 = []
# for sale in range(len(sales)):
#     if not sales[sale] <= 0 :
#         sale_01.append(sales[sale])
#         count_numbers_04 +=1
#     else :
#         continue
# print (count_numbers_04 , '\n' , sale_01)

# print("{:-^50}".format('#'))
# 4. Noto‘g‘ri (manfiy) ma'lumotlar soni.

#
# print (sales)
# sales_count_04 = 0
# sales_02 = []
# for sale in range(len(sales)):
#     if sales[sale] < 0 :
#         sales_count_04 += 1
#         sales_02.append(sales[sale])
#     else :
#         continue
#

# print(sales_count_04 ,'\n', sales_02)
# print("{:-^50}".format('#'))
#
# sum_sales_01 = 0
# for i in range(len(sales)) :
#     sum_sales_01 += sales[i]
#
# print(sum_sales_01)
#

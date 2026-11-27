# # 9/10 — Filiallar bo‘yicha moliyaviy tahlil
# # Kompaniyaning uchta filiali mavjud:
# # Branch (Filial — Филиал)	Revenue (Tushum — Выручка)	Expenses (Xarajatlar — Расходы)
# # Toshkent	                80 000 000	                50 000 000
# # Samarqand	                60 000 000	                35 000 000
# # Buxoro	                40 000 000	                25 000 000
# #
# # Vazifalar:
# # 1. Har bir filial tushumini o‘zgaruvchida saqla.
# # 2. Har bir filial xarajatini o‘zgaruvchida saqla.
# # 3. Har bir filial foydasini hisobla.
# # 4. Umumiy tushumni hisobla.
# # 5. Umumiy xarajatni hisobla.
# # 6. Kompaniyaning sof foydasini hisobla.
# # 7. Har bir filialning umumiy tushumdagi foiz ulushini hisobla.
# # 8. Umumiy foyda marjasini hisobla.
#
# #1
# Tashkent_revenue =  80_000_000
# Samarkand_revenue = 60_000_000
# Buxoro_revenue = 40_000_000
#
# #2
# Tashkent_expenses  = 50_000_000
# Samarkand_expenses = 35_000_000
# Buxoro_expenses = 25_000_000
#
# print('--------------------------------------------')
#
# #3
# Branch_profit_Tashkent = Tashkent_revenue - Tashkent_expenses
# Branch_profit_Samarkand = Samarkand_revenue - Samarkand_expenses
# Branch_profit_Buxoro = Buxoro_revenue - Buxoro_expenses
#
# print(f'Toshkent filyalining sof foydasi :{Branch_profit_Tashkent}''\n'
#       f'Samarkand filyalining sof foydasi :{Branch_profit_Samarkand}''\n'
#       f'Buxoro  filyalining sof foydasi :{Branch_profit_Buxoro}')
#
# print('--------------------------------------------')
#
# #4
# total_revenue = (Tashkent_revenue +
#                  Samarkand_revenue +
#                  Buxoro_revenue)
# print(f'Umumiy tushum :{total_revenue}')
#
# print('--------------------------------------------')
#
# #5
# total_expenses = (Tashkent_expenses +
#                   Samarkand_expenses +
#                   Buxoro_expenses)
# print(f'Umumiy harajat :{total_expenses}')
#
# print('--------------------------------------------')
#
# #6
# tota_profit = (Branch_profit_Tashkent +
#                Branch_profit_Samarkand +
#                Branch_profit_Buxoro)
# print(f'Kompaniyaning sof foydasi :{tota_profit}')
# print('--------------------------------------------')
#
# #7
# share_Tashkent = (Tashkent_revenue / total_revenue) * 100
# share_Samarkand = (Samarkand_revenue / total_revenue) * 100
# share_Buxoro = (Buxoro_revenue / total_revenue) * 100
# print(f'Toshkent filyalining umumiy tushumdagi foiz ulushi :{round(share_Tashkent,2)}%''\n'
#       f'Samarkand filyalining umumiy tushumdagi foiz ulushi :{round(share_Samarkand,2)}%''\n'
#       f'Buxoro  filyalining umumiy tushumdagi foiz ulushi :{round(share_Buxoro, 2)}%')
#
# print('--------------------------------------------')
#
# #8
# profit_margin = (tota_profit / total_revenue) * 100
# print(f'Kompaniyaning mumiy foyda marjasi :{round(profit_margin, 2)}%')
#
# print('--------------------------------------------')
#
from jsonschema.validators import extend
from prometheus_client.decorator import append
#
# print("{:-^50}".format('#'))

# 9/10 — Kompaniya ma’lumotlarini tozalash va tahlil qilish
# Quyidagi xom ma’lumotlar (Raw Data — Xom ma’lumotlar — Необработанные данные) berilgan:
# sale_1 = "   TOSHKENT ; laptop ; 5000000 ; 3   "
# sale_2 = " SAMARKAND ; PHONE ; 3000000 ; 5 "
# sale_3 = "   BUXORO ; monitor COMPUTER ; 1500000 ; 4 "
#
# Vazifalar:
# 1. Har bir savdo yozuvini split(";") bilan ajrat.
# 2. Har bir bo‘lakning boshidagi va oxiridagi bo‘sh joylarni strip() bilan tozala.
# 3. Shahar nomlarini title() orqali to‘g‘rila.
# 4. Mahsulot nomlarini ham title() orqali to‘g‘rila.
# 5. Narx va miqdorlarni int() orqali songa aylantir.
# 6. Har bir mahsulot uchun tushumni hisobla.
# 7. Barcha savdolarning umumiy tushumini hisobla.
# 8. Natijalarni tartibli ko‘rinishda chiqar.

# sale_1 = "   TOSHKENT ; laptop ; 5000000 ; 3   "
# sale_2 = " SAMARKAND ; PHONE ; 3000000 ; 5 "
# sale_3 = "   BUXORO ; monitor COMPUTER ; 1500000 ; 4 "
#
# print('---------------------------------------------------------')
# #2
# new_sal_1 = sale_1.strip()
# new_sal_2 = sale_2.strip()
# new_sal_3 = sale_3.strip()
# print(f'yangi list_1 bush joylar olibtshlangan : {new_sal_1}''\n'
#       f'yangi list_2 bush joylar olibtshlangan : {new_sal_2}''\n'
#       f'yangi list_3 bush joylar olibtshlangan : {new_sal_3}')
# print('---------------------------------------------------------')
# #1
# new_sal_1 = new_sal_1.split(';')
# new_sal_2 = new_sal_2.split(';')
# new_sal_3 = new_sal_3.split(';')
# print(f'yangi list_1 split(";") bilan ajratilgan: {new_sal_1}''\n'
#       f'yangi list_2 split(";") bilan ajratilgan: {new_sal_2}''\n'
#       f'yangi list_3 split(";") bilan ajratilgan: {new_sal_3}')
#
# print('---------------------------------------------------------')
# #3, 4
# new_sal_1[0], new_sal_1[1] = new_sal_1[0].title().strip(), new_sal_1[1].title().strip()
# new_sal_2[0], new_sal_2[1] = new_sal_2[0].title().strip(), new_sal_2[1].title().strip()
# new_sal_3[0], new_sal_3[1] = new_sal_3[0].title().strip(), new_sal_3[1].title().strip()
#
# print(f"yangi list_1 Shaxar va Maxsulot nomi tug'irlandi : {new_sal_1}"'\n'
#       f"yangi list_2 Shaxar va Maxsulot nomi tug'irlandi : {new_sal_2}"'\n'
#       f"yangi list_3 Shaxar va Maxsulot nomi tug'irlandi : {new_sal_3}")
#
# print('---------------------------------------------------------')
#
# #5
# new_sal_1[2], new_sal_1[3] = int(new_sal_1[2]), int(new_sal_1[3])
# new_sal_2[2], new_sal_2[3] = int(new_sal_2[2]), int(new_sal_2[3])
# new_sal_3[2], new_sal_3[3] = int(new_sal_3[2]), int(new_sal_3[3])
# print (f'yangi list_1 indexlar int ga uzgartirildi : {new_sal_1}''\n'
#        f'yangi list_2 indexlar int ga uzgartirildi : {new_sal_2}''\n'
#        f'yangi list_3 indexlar int ga uzgartirildi : {new_sal_3}')
#
# print('---------------------------------------------------------')
#
# #6
# laptop = int(new_sal_1[2]) * int(new_sal_1[3])
# phone = int(new_sal_2[2]) * int(new_sal_2[3])
# monitor_computer = int(new_sal_3[2]) * int(new_sal_3[3])
#
# print(f'laptop uchun tushum :{laptop} ml \n '
#       f'phone uchun tushum :{phone} ml\n'
#       f'monitor computer tushum :{monitor_computer} ml')
#
# print('---------------------------------------------------------')
#
# #7
# total_sales = laptop + phone + monitor_computer
# print(f'Umumiy tushum  :{total_sales} ml')

print('---------------------------------------------------------')
#
# Vazifalar:
# 1. Ikkinchi mahsulot nomini chiqar.
# 2. Ikkinchi mahsulot narxini chiqar.
# 3. "Tablet" mahsulotini  bilan qo‘sh.
# 4. 2500000 narxini  yordamida narxlar ro‘yxatiga ikkinchi o‘ringa joylashtir.
# 5. Har ikkala listning elementlari sonini chiqar.
# 9/10 — Kompaniya mahsulotlarini boshqarish
# Kompaniyaning dastlabki ma’lumotlari:

# mahsulotlar = ["Laptop", "Phone", "Monitor"]
# narxlar = [5000000, 3000000, 1500000]
#
# #1
# print(mahsulotlar[1])
#
# print('---------------------------------------------------------')
#
# #2
# print(narxlar[1])
#
# print('---------------------------------------------------------')
#
# #3
#
# mahsulotlar.append('Tablle')
# print(mahsulotlar)
#
# print('---------------------------------------------------------')
#
# #4
#
# narxlar.insert(1, 2500000)
# print(narxlar)
#
# print('---------------------------------------------------------')
#
# #5
# print(len(mahsulotlar))
# print(len(narxlar))
#
# print('---------------------------------------------------------')
#
# #6
#
# mahsulotlar.remove('Laptop')
# print(mahsulotlar)
#
# print('---------------------------------------------------------')
#
# #7
#
# narxlar.pop(1)
# print(narxlar)
#
print("___________________________________________________")

#
# kunlik_tushum = [
#     12000000, 15000000, 9000000, 18000000, 20000000,
#     11000000, 25000000, 22000000, 17000000, 30000000,
#     14000000, 19000000, 21000000, 16000000, 28000000,
#     13000000, 24000000, 26000000, 18000000, 32000000,
#     15000000, 27000000, 29000000, 20000000, 35000000,
#     17000000, 30000000, 31000000, 23000000, 40000000
# ]

# 1. Davrlar bo‘yicha ajratish — Slicing (Срез)
# - Birinchi 10 kunlik tushumni birinchi_10_kun listiga ajrat.
# - Keyingi 10 kunlik tushumni ikkinchi_10_kun listiga ajrat.
# - Oxirgi 10 kunlik tushumni oxirgi_10_kun listiga ajrat.
#
# birinchi_10_kun = kunlik_tushum[0:10]
# print(f'1 - kvartal: {birinchi_10_kun}')
# print(len(birinchi_10_kun))
#
# ikkinchi_10_kun = kunlik_tushum[10:20]
# print(f'2 - kvartal: {ikkinchi_10_kun}')
# print(len(ikkinchi_10_kun))
#
# oxirginchi_10_kun = kunlik_tushum[20:30]
# print(f'3 - kvartal: {oxirginchi_10_kun}')
# print(len(oxirginchi_10_kun))

# print("{:-^50}".format('#'))
#
# 2. Qisqa davrlarni ajratish
# - Dastlabki 5 kunlik tushumni ajrat.
# - Oxirgi 5 kunlik tushumni ajrat.
# - 10-kundan 20-kungacha bo‘lgan tushumlarni ajrat.
#
# brichi_besh_kun = kunlik_tushum[0:5]
# print(f'brichi besh kun : {brichi_besh_kun}')
#
# oxirgi_besh_kun = kunlik_tushum[-5:]
# print(oxirgi_besh_kun)
#
# _10_dan_20_oraliq_kun = kunlik_tushum[9:20]
# print(_10_dan_20_oraliq_kun)

# print("{:-^50}".format('#'))

# 3. Negative Index (Manfiy indeks — Отрицательный индекс)
# - Oxirgi kundagi tushumni chiqar.
# - Oxiridan ikkinchi kundagi tushumni chiqar.
# - Oxirgi 7 kunlik tushumni ajrat.

# oxirgi_kun = kunlik_tushum[-1:]
# print(f'ohirgi kun :{oxirgi_kun}')
#
# oxirgi_2_kun = kunlik_tushum[-2:-1]
# print(f'ohirgi 2 - kun :{oxirgi_2_kun}')
#
# oxirgi_7_kun = kunlik_tushum[-7:]
# print(f'ohirgi 7 kunlik :{oxirgi_7_kun}')

# print("{:-^50}".format('#'))

# 4. Step (Qadam — Шаг) bilan ishlash
# - Faqat juft tartibdagi kunlar tushumini ajrat.
# - Har uchinchi kun tushumini ajrat.
# - Har to‘rtinchi kun tushumini ajrat.

# juft_index = kunlik_tushum[1::2]
# print(juft_index)
#
# xar_3_kun = kunlik_tushum[2::3]
# print(xar_3_kun)

# print("{:-^50}".format('#'))

# 5. Reverse (Teskari tartib — Обратный порядок)
# - Barcha 30 kunlik tushumni teskari tartibda chiqar.
# - Birinchi 10 kunlik tushumni teskari tartibda chiqar.
# - Oxirgi 10 kunlik tushumni teskari tartibda chiqar.

# teskari_tartib = kunlik_tushum [::-1]
# print(f'teskari tartibda: {teskari_tartib}')
#
# teskari_tartib_10_kun = kunlik_tushum [:10][::-1]
# print(f'teskari tartibda brichi 10 kunlik: {teskari_tartib_10_kun}')
#
# teskari_oxirgi_10_kun = kunlik_tushum [-10:][::-1]
# print(f'teskari tartibda ihirgi 10 kunlik: {teskari_oxirgi_10_kun}')

# print("{:-^50}".format('#'))

# 6. Copy (Nusxa — Копия)
# - kunlik_tushum[:] orqali butun listning nusxasini yarat.
# - Nusxaning birinchi elementini 99999999 ga o‘zgartir.
# - Asl list va nusxani alohida chiqar.
# - Asl list o‘zgargan yoki o‘zgarmaganini tekshir.
#
#
# kunlik_tushum_copy = kunlik_tushum[:]
#
# kunlik_tushum_copy = kunlik_tushum[0] = 99999999
# print(f'Alamashtrilagan: {kunlik_tushum_copy}')
#
# kunlik_tushum_copy.pop(0)
# kunlik_tushum_copy.insert(0, 99999999)
# print(f'Alamashtrilagan: {kunlik_tushum_copy}')
#
# print(f'nusxasi: {kunlik_tushum_copy}')
# print(f'orginal: {kunlik_tushum}')
# print("{:-^50}".format('#'))

# toshkent = [
#     "Laptop", "Phone", "Monitor", "Laptop", "Tablet",
#     "Phone", "Laptop", "Keyboard", "Monitor", "Phone"
# ]
#
# samarqand = [
#     "Phone", "Laptop", "Mouse", "Tablet", "Phone",
#     "Monitor", "Laptop", "Mouse", "Keyboard", "Phone"
# ]
#
# buxoro = [
#     "Monitor", "Laptop", "Phone", "Tablet", "Laptop",
#     "Mouse", "Phone", "Monitor", "Keyboard", "Laptop"
# ]

#
# 2. Topshiriqlar
# 1-qism. extend() — Ro‘yxatni kengaytirish (Расширение списка)
# 1. Uchta filialning mahsulotlarini barcha_savdolar nomli bitta
# ro‘yxatga birlashtir.
# 2. Har bir filial ro‘yxati o‘z holicha saqlanib qolishi kerak.
# 3. Umumiy savdolar sonini len() bilan aniqlab chiqar.
# 4. Har bir filialda nechta mahsulot sotilganini alohida chiqar.


# barcha_savdolar =  []
# barcha_savdolar.extend(toshkent + samarqand + buxoro)
# print(barcha_savdolar)
#
# print(len(barcha_savdolar))
# print(f'Toshkent: {len(toshkent)},''\n'
#       f'Samarand: {len(samarqand)},''\n'
#       f'Buxoro: {len(buxoro)}')

print('-----------------------------------------')
# 2-qism. count() — Takrorlanish sonini aniqlash (Подсчёт повторений)
# barcha_savdolar ro‘yxatidan foydalanib:
# 1. Laptop necha marta sotilgan?
# 2. Phone necha marta sotilgan?
# 3. Monitor necha marta sotilgan?
# 4. Tablet necha marta sotilgan?
# 5. Mouse necha marta sotilgan?
# 6. Keyboard necha marta sotilgan?

# # brichi usul
# print(f'Laptop :{barcha_savdolar.count('Laptop')}''\n'
#       f'Phone :{barcha_savdolar.count('Phone')}''\n'
#       f'Monitor :{barcha_savdolar.count('Monitor')}''\n'
#       f'Tablet :{barcha_savdolar.count('Tablet')}''\n'
#       f'Mouse :{barcha_savdolar.count('Mouse')}''\n'
#       f'Keyboard :{barcha_savdolar.count('Keyboard')}'
#       )

# # 2 usul
#
# from collections import Counter
#
# barcha_savdolar = Counter(toshkent)
# print(barcha_savdolar)


# print('-----------------------------------------')
#
# 3-qism. index() — Birinchi uchrashgan indeksni topish (Поиск первого индекса)
# 1. Laptop birinchi marta qaysi indeksda uchragan?
# 2. Phone birinchi marta qaysi indeksda uchragan?
# 3. Monitor birinchi marta qaysi indeksda uchragan?
# 4. Keyboard birinchi marta qaysi indeksda uchragan?
#
# print(f'Laptop  : {barcha_savdolar.index('Laptop')}''\n'
#       f'Phone   : {barcha_savdolar.index('Phone')}''\n'
#       f'Monitor : {barcha_savdolar.index('Monitor')}''\n'
#       f'Tablet  : {barcha_savdolar.index('Tablet')}''\n'
#       f'Mouse   : {barcha_savdolar.index('Mouse')}''\n'
#       f'Keyboard: {barcha_savdolar.index('Keyboard')}'
#       )

# print('-----------------------------------------')
#
# 4-qism. sort() — Saralash (Сортировка)
# 1. barcha_savdolar ro‘yxatini alifbo tartibida sarala.
# 2. Uni teskari alifbo tartibida sarala.
# 3. mahsulot_narxlari ro‘yxatini kichikdan kattaga sarala.
# 4. Narxlarni kattadan kichikka sarala.

# barcha_savdolar.sort()
# print(barcha_savdolar)
#
# barcha_savdolar.sort(reverse=True)
# print(barcha_savdolar)
#
#
# mahsulot_narxlari = [
#     5000000, 3000000, 1500000, 2000000,
#     500000, 300000
# ]
#
# mahsulot_narxlari.sort()
# print(mahsulot_narxlari)
#
# mahsulot_narxlari.sort(reverse=True)
# print(mahsulot_narxlari)


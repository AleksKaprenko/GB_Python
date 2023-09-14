# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.

# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова k и выводит его. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, 
# либо только русские буквы.

# Пример:
# k = 'ноiутбук'
# 12
# import re

# dictionary_eng = {1:"A E I O U L N S T R", 
#             2: "D G", 3:"B C M P", 4:"F H V W Y", 5:"K",8:"J X",10:"Q Z"}
# dictionary_ru = {1:"А, В, Е, И, Н, О, Р, С, Т а е", 
#             2: "Д, К, Л, М, П, У", 3:"Б, Г, Ё, Ь, Я", 4:"Й, Ы", 5:", З, Х, Ц, Ч",8:"Ш, Э, Ю",10:"Ф, Щ, Ъ"}

# k='ноутбук'
# k=k.upper()
# sum = 0
# for i in k:
#     if ord(i) <123: # код последней буквы англ. алфавита Unicode z = 122
#         for t in dictionary_eng:
#             sp = dictionary_eng[t]
#             sp = re.split(" |;|,|\n", sp)
#             if i in sp:
#                 sum += t
#     elif 1040 <= ord(i) <= 1105: # для букв русск алфавита Unicode
#         for n in dictionary_ru:
#             sp1 = dictionary_ru[n]
#             sp1 = re.split(" |;|,|\n", sp1)
#             if i in sp1:
#                 sum += n
# print(sum)

# Вариант 2

list_letters = {1:"AEIOULNSTRАВЕИНОРСТ",
                2:"DGДКЛМПУ",
                3:"BCMPБГЁЬЯ",
                4:"FHVWYЙЫ",
                5:"KЖЗХЦЧ",
                8:"JXШЭЮ",
                10:"QZФЩЪ"}

# word = input("Введите слово: ").upper()
k='ноутбук'
k=k.upper()
sum = 0
for i in k:
    for key, values in list_letters.items():
        if i in values:
            sum += key
print(sum)
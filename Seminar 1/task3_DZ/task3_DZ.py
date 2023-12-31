# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета с номером n 
# и выводит на экран yes или no.

# Пример:
# n = 385916 -> yes
# n = 123456 -> no

n = 123456
if len(str(n))==6:
    part1 = n//1000
    part2 = n%1000
    part1_sum = part2_sum =0
    while part1>0 :
        part1_sum += part1%10
        part2_sum += part2%10
        part1//=10
        part2//=10
    # if part1_sum == part2_sum:
    #     print(f"yes: {part1_sum} = {part2_sum}")
    # else: print("no")
    print(['no' , 'yes'][part1_sum==part2_sum])
else: print("Кол-во цифр билета отлично от 6")


# Катя узнала, что ей для сна надо X минут. В отличие от Коли, 
# Катя ложится спать после полуночи в H часов и M минут. 
# Помогите Кате определить, на какое время ей поставить будильник, 
# чтобы он прозвенел ровно через X минут после того, как она ляжет спать.

# На стандартный ввод, каждое в своей строке, подаются значения X, H и M.
#  Гарантируется, что Катя должна проснуться в тот же день, что и заснуть. 
#  Программа должна выводить время, на которое нужно поставить будильник: 
#  в первой строке часы, во второй — минуты.
# Sample Input 1:

# 480
# 1
# 2
# Sample Output 1:

# 9
# 2
# Sample Input 2:

# 475
# 1
# 55
# Sample Output 2:

# 9
# 50

#
X = int(input())# Подаем на ввод число Х минут которые Катя должна проспать
H = int(input())# Подаем на ввод число Н ( во сколько часов ложиться спать)
M = int(input())# Подаем на ввод число М ( во сколько минут ложиться спать)
print((H * 60 + M + X) // 60)# Использую функцию целочисленного деления находим час на который надо поставить будильник
print((H * 60 + M + X) % 60)# Использую функцию нахождения остатка от деления находим минуту на которую надо поставить будильник




# x = int(input()) #475 /7 /55  or 480 / 8 / 0
# h = int(input()) #1   /60
# m = int(input()) #55 or 2
#
# print(x // 60 + h + ((m + (x % 60)) // 60) )  #9
# print(((m + (x % 60)) % 60) )		         #50




#
# a,b,c=(int(input()) for i in range(3))
# print('%s\n%s' % ((a+c)//60+b, (a+c)%60))



#
# time = int(input())
# hours = int(input())
# mins = int(input())
# time += hours*60 + mins
# print (time//60)
# print (time%60)



#
# x = int(input()) + 60 * int(input()) + int(input());
# print(x // 60);
# print(x % 60);
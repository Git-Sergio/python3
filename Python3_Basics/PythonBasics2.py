
if 5 > 3:
    print('5 is greater than 3')

num = 0
if num > 0:
    print('This is a positive num')
elif num == 0:
    print('Num is zero')
else:
    print('This is a negative num')

num = [1,2,3,4,5]
for val in num:
    print(val)

num = [1,2,3,4,5]
sum = 0
for val in num:
    sum = sum + val
print('Total is ', sum)  # 15


fruits = ['apple', 'orangee', 'grapes']
for val in fruits:
    print(val)
else:
    print('No fruits left')

print('Enter a number : ')
num = int(input())
sum = 0
i = 1
while i<num:
    sum=sum+i
    i=i+1
print('Total is :', sum)   #45



























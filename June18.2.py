money = 100.00
people = 3

print(type(money))
print(type(people))

each = money / people
print(type(each))

print('$', money, 'split 3 ways is $', each)
print(f'${money: .2f} split 3 ways is ${each: .2f}')
print('Done!')

each = money // people
print(type(each))

print('$', money, 'split 3 ways is $', each)

print(7/2)
print(7//2)

num = 2**256
print('2.0 to the power of 256 is', num)



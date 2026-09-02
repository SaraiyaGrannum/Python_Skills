# data type - ints, floats, doubles, strings

name = input("what is your name? ")

print("hello " + name , ".")

print('Per the cleveland Clinic, you should eat 2400 calories each day. ')

calories_today = int(input("how many calories have you eaten so far today? "))

# calories_today = int(calories_today

calories_remaining = 2400 - calories_today

print('You can eat another' , calories_remaining , 'calories today.')

print(name, type(name))
print(calories_today, type(calories_today))

players = {
  'Messi': 10,
'Ronaldo': 7
}
print(players)
print(type(players))
print(players['Messi'])
print(type(players['Messi']))

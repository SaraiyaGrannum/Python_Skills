import math
import random

die1 = random.randint(1, 6)
die2 = random.randint(1, 6)

print("Die 1: " , die1)
print("Die 2: " + str(die2))
print()

answer = die1 + die2
print("Sum: " + str(answer))

answer_2 = die1 * die2
print("Product: " + str(answer_2))
print("Product % Sum:" , answer_2 % answer)
print()

print("Square Root of Product:", math.sqrt(answer_2))
print("Ceiling of Square Root:", math.ceil(answer_2))
print()

multiplier = round(random.uniform(0.5, 2.0), 2)
print("Bonus Multiplier:", multiplier)

final_answer = round(multiplier * answer)

print("Final Score:", final_answer)

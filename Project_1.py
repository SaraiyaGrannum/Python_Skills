import math
import random

print("--- Wander Combat ---")

active_skill = random.randint(500, 2000)
print(f"Active skill is: {active_skill}")

crit_damage = active_skill * 1.56
print(f"Critical damage is: {crit_damage}")

final_damage = math.ceil(crit_damage)
print(f"Final damage is: {final_damage}")

resonance = final_damage % 3
print(f"Resonance is: {resonance}")

if resonance == 0:
 print("Stellacrum match! Core shield broken! The wander is vulnerable!")
else:
 print("Attack landed, but the shield is not broken!")


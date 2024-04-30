from DiamondTrap import King


Joffrey = King("Joffrey")
print(Joffrey.__dict__)
Joffrey.set_eyes("blue")
Joffrey.set_hairs("light")
print(Joffrey.get_eyes())
print(Joffrey.get_hairs())
print(Joffrey.__dict__)

print("\n-------------------------------\n")

Tommen = King("Tommen")
print(Tommen.__dict__)
Tommen.eyes = "blue"
Tommen.hairs = "blond"
print(Tommen.eyes)
print(Tommen.hairs)
print(Tommen.__dict__)

import random
character = "+-/*!&amp;amp;amp;$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password = ""
Indication = int(input("Coloque la longitud de la contraseña"))
for _ in range(Indication):
    password += random.choice(character)
print(password)

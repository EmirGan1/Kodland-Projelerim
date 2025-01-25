import random
olasi = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
parolauzunluk = int(input("Parolaninizin  uzunlugu ne olsun"))
parola = ""
for i in range(parolauzunluk):
    parola += random.choice(olasi)
print("Oluşturulan parola:",parola)



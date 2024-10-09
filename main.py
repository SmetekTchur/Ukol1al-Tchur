import random
# Vytvoření pole
array = [5, 87, 47, 69, 71, 35, 79, 25, 15] 
# Výměna čísla v poli
array [5] = 34
print (array)
# První, prostřední a poslední hodnota
prvni = array[0]
prostredek = array[len(array) // 2]
posledni = array[-1]
# Výpis hodnot
print("První hodnota:", prvni)
print("Prostřední hodnota:", prostredek)
print("Poslední hodnota:", posledni)
# 7 indexová hodnota pole
print(array [6])
# Délka pole
print (len(array))
# Najdi minimální a maximální hodnotu
minimalni = min(array)
maximalni = max(array)
# Výpis hodnot
print("Minimální hodnota:", minimalni)
print("Maximální hodnota:", maximalni)
#Druhé pole
arrayh =  [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]
print (arrayh)
# Všechny čísla z arraye dohromady
print (sum(arrayh))
# Součet 1 a 5 indexového čísla z pole č.2
cislo = 0
cislo2 = 4
soucet = arrayh [cislo] + arrayh[cislo2]
print (soucet)
# Náhodné promíchání čísel v poli BONUS
arrays = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]
random.shuffle (arrays)
print(arrays)

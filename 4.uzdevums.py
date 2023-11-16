skaitlis =int(input("Ievadi skaitli faktoriāla aprēķināšanai: "))

faktorials= 1

for i in range (1, skaitlis +1):
    faktorials *=i

print(f"Faktoriāls no tava izvēlētā {skaitlis} ir: {faktorials}")

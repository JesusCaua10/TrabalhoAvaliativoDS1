vr_num = int(input("Diga um numero para ver sua tabuada: "))
print(f"tabuada do {vr_num}")
for num in range(1,10):
    res = vr_num * num
    print(f"{vr_num} x {num} = {res} ")

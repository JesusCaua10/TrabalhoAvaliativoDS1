vr_num = int(input("Diga um numero para ver sua tabuada: "))
print(f"Essa é a tabuada do {vr_num}")
for num in range(1,11):
    vr_res = vr_num * num
    print(f"{vr_num} x {num} = {vr_res} ")

vr_nome = input("Diga seu nome: ")
vr_disciplina = input("Diga uma disciplina: ")
vr_nota1 = int(input("Diga sua primeira nota: "))
vr_nota2 = int(input("Diga sua segunda nota: "))
vr_média = (vr_nota1 + vr_nota2)/2
if vr_média >= 6 :
    print(f"{vr_nome} está aprovado na disciplina de {vr_disciplina}")
else :
    print(f"{vr_nome} está reprovado na disciplina de {vr_disciplina}")
vr_hora = int(input("Diga uma hora entre 0 e 23: "))
if 0 <= vr_hora < 12 :
  print("Está de manhã")
elif 12 <= vr_hora < 18 :
  print("Está de tarde")
elif 18 <= vr_hora < 24 :
  print("Está de noite")
else :
  print("Valor inválido")

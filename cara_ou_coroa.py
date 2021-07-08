import random

partidas = int(input("Quantas partidas deseja jogar? "))
ganhou = 0 
perdeu = 0


for i in range(partidas):


  escolha = int(input("cara(0) ou coroa(1) ?"))
  rand = round(random.random() * 100)

  if ((rand % 2) == 0):
    print("cara")
    if escolha == 0:
      ganhou += 1
      print("Ganhou")
    else:
      perdeu += 1
      print("Perdeu")

  else:
    print("coroa")
    if escolha != 0:
      ganhou += 1
      print("Ganhou")
    else:
      perdeu += 1
      print("Perdeu")
   
print ("Relatorio das partidas: ", "\nGanhou: ", ganhou, "\nPerdeu: ", perdeu)

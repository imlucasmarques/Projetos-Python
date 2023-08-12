print("Seja muito bem vindo ao quiz do Lucas!")
answer_user = input("Quer começar? (sim ou não) ")

if answer_user != "sim": 
    quit()

score = 0

print("Começando...")

print("Quem desenvolveu o jogo Grand Theft Auto (GTA)? \n (A)Rockstar Games \n (B)Ubisoft \n (C)Activision \n (D)EA \n")
answer_1 = input("Resposta: ")

if answer_1 == "A":
    print("Correto!")
    score = score + 1
else: 
    print("Incorreto!")


print("Qual é o nome do protagonista do jogo GTA San Andreas? \n (A)Carlos John \n (B)Carl Johnson \n (C)Carl Jaqueline \n (D)Carlos Johnson \n")
answer_2 = input("Resposta: ")

if answer_2 == "B":
    print("Correto!")
    score = score + 1
else: 
    print("Incorreto!")

print(f"Quiz acabou... Pontuação: {score}/2")

import random

print("Seja muito bem vindo ao Guess Number do Lucas!")
choice_number = input("digite o número teto do desafio: ")

if choice_number.isdigit(): # verifica se a string só contém números
    choice_number = int(choice_number)  
else:
    print("Erro: valor informado não é numérico. Favor, execute novamente e informe um número!")
    quit()

random_number = random.randint(0, choice_number)

n_choices = 0

while True: 
    answer_user = input("Adivinhe o número: ")

    if answer_user.isdigit():
        answer_user = int(answer_user)
    else: 
        print("Erro: valor informado não é numérico. Favor, informe um número!")
        continue

    n_choices = n_choices + 1
    if answer_user == random_number:
        print("Acertou!")
        break
    elif answer_user > random_number:
        print("Chutou alto, o número randomico é menor que isso...")
    else:
        print("Chutou baixo, o número randomico é maior que isso...")


print("Número de tentativas: " + str(n_choices))
import random
nomes = str(input("Digite o seu nome. Se for mais de um colocar todos juntos. Também pode ser apelido: "))
sobrenome = str(input("Digite o seu sobrenome. Colocar todos juntos: "))
simbolos = ['@','#','$','%','^','&','*']
simb_aleat1 = random.choice(simbolos)
simb_aleat2 = random.choice(simbolos)
simb_aleat3 = random.choice(simbolos)
nums_aleat = random.randint(1,8000)
nums_aleat2 = random.randint(1,8000)
print(f"Sua senha é: {simb_aleat1}{nomes}{nums_aleat}{simb_aleat1}{sobrenome}{simb_aleat2}{nums_aleat2}{simb_aleat3}")

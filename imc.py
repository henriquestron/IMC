
print('-='*30)
print('Faça agora, o calculo do seu IMC (Índice de Massa Corporal).')
print('-='*30)

print('Por Favor...')
peso = float(input('Digite o seu peso em Kg: '))
altura = float(input('Digite a sua altura: '))
imc = round(peso/(altura * altura),2)
if(imc <= 18.5):
    print('Você está abaixo do peso!')
elif(imc >= 18.9 and imc < 24.9):
    print('Seu peso está normal!')
elif(imc >= 25.0 and imc < 29.9):
    print('Sobrepeso!')
elif(imc >= 30.0 and imc < 34.9):
    print('Obesidade Grau I!')
elif(imc >= 35.0 and imc < 39.9):
    print('Obesidade Grau II!')
elif(imc > 40):
    print('Obesidade Grau III!')
print(f'Seu Indice de Massa Corporal é {imc}')
r = int(input('Dê uma nota pro programa: '))
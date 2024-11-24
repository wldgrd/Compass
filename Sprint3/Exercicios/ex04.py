'''Escreva um código Python para imprimir todos os números primos entre 1 até 100. 
Lembre-se que você deverá desenvolver o cálculo que identifica se um número é primo ou não.
Importante: Aplique a função range().'''

def eh_primo(n):
    if (n==0 or n==1):
        return False
    else:
        for i in range(2,n):
            if n%i == 0:
                return False
    return True 

for i in range(100):
    if eh_primo(i):
        print(i)

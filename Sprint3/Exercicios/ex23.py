'''Crie uma classe  Calculo  que contenha um método que aceita dois parâmetros, X e Y, e retorne a soma dos dois. 
Nessa mesma classe, implemente um método de subtração, que aceita dois parâmetros, X e Y, e retorne a subtração dos dois (resultados negativos são permitidos).

Utilize os valores abaixo para testar seu exercício:
x = 4 
y = 5
imprima:

Somando: 4+5 = 9
Subtraindo: 4-5 = -1'''

class Calculo:

    def soma(self,x,y):
        return x + y 

    def sub(self,x,y):
        return x - y 

calculo = Calculo()

x=4
y=5

print('Somando: {}+{} = {}'.format(x,y,calculo.soma(x,y)))
print('Subtraindo: {}+{} = {}'.format(x,y,calculo.sub(x,y)))

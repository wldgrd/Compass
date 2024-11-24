# Instruções

- Uma ou mais seções para descrever o que estiver aprendendo (resumo), de maneira estruturada.

- Breve conteúdo de cada pasta relacionada a sprint.

# Resumo

## **Linguagem Python**  
Nessa Sprint aprendemos conceitos gerais como a noção de algorítmo e as estruturas de dados, bem como a instalação e configuração do Python, Jupyter e VSCode.

Dentro do conteúdo estão os seguintes tópicos:  
**Tipos Básicos**  
    - int
    - float
    - boolean
    - string
    - lista
    - dicionários  

**Variáveis**  
    - Espaços reservados na memória para guardar determinado valor  

**Comentários**  
Pequenos trechos de texto usados para ajudar a interpretar o código  
    - Comentários de uma única linha usando #  
    - Comentários de múltiplas linhas usando '''comentário'''  

# **Operadores**  
**Aritméticos:**  
    Usados para efetuar operações.  
    - Soma +  
    - Subtração -  
    - Multiplicação *  
    - Divisão /  
    - Parte inteira da divisão //  
    - Módulo ou resto da divisão %  
    - Potência **  
    <br>- **Relacionais:**  
    Usados para efetuar comparações.    
    - Maior >  
    - Menor <  
    - Maior ou igual >=  
    - Menor ou igual <=  
    - Diferente != 
    - Igualdade ==  

<br>**-Lógicos:**  
    - and (A and B retorna True apenas quando A e B são verdadeiros)
    - or (A or B retorna True quando um ou outro é verdadeiro)  
    - xor (retorna True quando apenas um é verdadeiro)  
    - not (negação -> not True retorna False, not False retorna True)  

<br>**Membro:**  
    Verifica se algo está na estrutura.

```python
texto = 'esse texto é um teste'

's' in texto --> True
'm' in texto --> True
'w' in texto --> False
'esse' in texto --> True

#Quando aplicado sobre uma string, o operador in analisa cada um dos caracteres.

lista = ['Welder', 33, "Valinhos", "Casado"]

'W' in lista --> False
'Welder' in lista --> True
33 in lista --> True
'33' in lista --> False

#Quando aplicado sobre uma lista, o operador in analisa o dado como um todo para uma dada posição. 
``` 

**Identidade:**  
    Verifica se uma coisa é outra, ou seja, se elas apontam para o mesmo espaço de memória.
``` python
x = 3
y = x
z = 3

x is y --> True
y is z --> True
x is not z --> False
```  
**Conversão de tipos**  
Para executar determinadas operações, precisamos que os tipos estejam corretamente ajustados.  
Por exemplo:

```python
5 + 3 --> 8

5 + '3' --> TypeError: unsupported operand type(s) for +: 'int' and 'str'

5 + int('3') --> 8 #Converte o conteúdo da string para inteiro e efetua a soma

'5' + '3' --> '53' #Converte o número para string e concatena as duas strings
```

**Estruturas de controle:**  
    - if /else (executa um bloco de código caso uma determinada condição ocorra, caso contrário executa o segundo bloco)

```python
if nome in lista: 
    print(nome)
else:
    print('O nome não está na lista.)
```
-for é um laço de repetição
```python
for i in range(10):
    print(i)
# o código vai printar os números de 0 a 9

lista = [1, 'Texto', 2, 'Palavra']
for conteudo in lista:
    print(conteudo)
# o código vai printar cada um dos elementos da lista 
```
-While também é um laço de repetição que funciona enquanto algo é verdade
```python
while num != -1:
    num = int(input('Digite um número: '))
#executa o bloco de código enquanto o número for diferente de -1.
```
**Comprehension:**  
Sintaxe muito poderosa para criação de listas.
```python
lista = []
for num in range(1,21):
    if num % 2 == 0:
        lista.append(num)`
# Retorna a lista [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# A mesma lista pode ser obtida usando a sintaxe de comprehension:

lista = [num for num in range(1,21) if num%2 == 0]

# De modo geral: lista = [expressão for item in list if condicional]
```

**Unpacking:**  

Podemos passar múltiplos parâmetros para uma função através dessa técnica.
```python
def soma_n(*numeros): #usamos o operador * para representar o unpacking
    soma = 0
    for n in numeros:
        soma += n
    return soma

soma_n(1,1) --> 2
soma_n(1,2,3) --> 6

def teste(*parametros):
    for parametro in parametros:
        print(parametro)

teste(1,2,3)
-->1
   2
   3

parametros = [1,2,3]
teste(*parametros) #com uso do operador *
-->1
   2
   3

teste(parametros) #sem uso do operador *
--> [1, 2, 3]
```


# Links
[📜**Certificados**](/Sprint3/Certificados/certificado_AWS%20Course%20Completion%20Certificate.pdf)  
[🕵️‍♂️**Evidências** ]()  
[💪**Exercícios**](/Exercicios/)  
[🖳**Desafio**]()  
[🖳**Desafio - Parte 1 - Preparação de Ambiente**]()  
[🖳**Desafio - Parte 2 - Desenvolvimento**]()



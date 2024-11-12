#Escreva um programa que lê o conteúdo do arquivo texto arquivo_texto.txt e imprime o seu conteúdo.

texto = open('feedbacks.txt')
for palavra in texto:
    print(palavra)
#Escreva um programa que lê o conteúdo do arquivo texto arquivo_texto.txt e imprime o seu conteúdo.

texto = open('arquivo_texto.txt')
for palavra in texto:
    print(palavra, end = '')
texto.close()
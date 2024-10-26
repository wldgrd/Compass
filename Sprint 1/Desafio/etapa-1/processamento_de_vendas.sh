#!/bin/bash

# O script possui alguns checkpoints para facilitar o debug. Cada checkpoint tem nome chk1, chk2, etc 
cd /home/welder/Documents
echo "chk1: iniciando o script em $(date +"%Y-%m-%d às %H:%M:%S")"

mkdir -p vendas #Cria o diretório vendas (na primeira execução)
echo "chk2: aqui criou o diretório vendas" 

cp dados_de_vendas.csv vendas/ #copia o arquivo dados_de_vendas.csv para o diretório vendas
echo "chk3: copiado o arquivo csv para vendas"

data_do_sistema=$(date +%Y%m%d) #extrai a data do sistema e salva o valor na variável data_do_sistema no formato YYYYMMDD
#o símbolo $ serve para referenciar variáveis ou substituição de comando e, neste caso, está servindo como substituição

#--------------------Manipulação dos arquivos e diretórios------------------------#

mkdir -p vendas/backup/ #cria o diretório backup dentro do diretório vendas (na primeira execução)
echo "chk4: criado o diretório backup"

cp vendas/dados_de_vendas.csv vendas/backup/ #copia o arquivo dados_de_vendas.csv do diretório vendas para o diretório backup
echo "chk5: arquivo csv copiado para backup"

mv vendas/backup/dados_de_vendas.csv vendas/backup/dados-$data_do_sistema.csv #renomeia o arquivo dados_de_vendas.csv da pasta backup p/  dados-YYYYMMDD.csv
echo "chk6: arquivo csv renomeado"

mv vendas/backup/dados-$data_do_sistema.csv vendas/backup/backup-dados-$data_do_sistema.csv #renomeia o arquivo do diretório backup para backup-dados-YYYYMMDD
echo "chk7: arquivo csv renomeado para backup"

echo $(date +%Y/%m/%d\ %H:%M) > vendas/backup/relatorio-$data_do_sistema.txt #cria o arquivo relatório e acrescenta a data e a hora do sistema
echo "chk8: relatório criado"

#Separando as informações do csv e pegando o campo data
awk -F, 'NR==2 {print "O primeiro registro foi feito em: " $5} END {print "O último registro foi feito em: " $5}' vendas/dados_de_vendas.csv >> vendas/backup/relatorio-$data_do_sistema.txt
echo "chk9: acrescentadas as datas do primeiro e último registros no relatório"

#Contando a quantidade total de itens diferentes vendidos
awk -F, 'NR>1 {itens[$2]} END {print "Quantidade de itens diferentes vendidos: " length(itens)}' vendas/dados_de_vendas.csv >> vendas/backup/relatorio-$data_do_sistema.txt
echo "chk10: contagem dos itens distintos realizada"

#Exibindo dez itens e o cabeçalho do arquivo de backup e adicionando no relatório.txt
head -n 11 vendas/backup/backup-dados-$data_do_sistema.csv >> vendas/backup/relatorio-$data_do_sistema.txt
echo "chk11: lista de itens adicionada ao relatorio"

#Comprimindo o arquivo de backup para formato .zip
zip vendas/backup/backup-dados-$data_do_sistema.zip vendas/backup/backup-dados-$data_do_sistema.csv
echo "chk12: arquivo de backup compactado em formato .zip"

#Removendo os arquivos backup-dados-YYYYMMDD.csv e dados_de_vendas.csv
rm vendas/backup/backup-dados-$data_do_sistema.csv
rm vendas/dados_de_vendas.csv
echo "chk13: removidos os arquivos utilizados nas manipulações"

echo "chk14: finalizando o script em $(date +"%Y-%m-%d às %H:%M:%S")"
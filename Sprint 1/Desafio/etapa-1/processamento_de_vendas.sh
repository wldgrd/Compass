#!/bin/bash

#set -e

export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/snap/bin
export DIRARQ=/tmp/weeelder/ecommerce
echo "inicindo o script"

#Criando o diretório vendas (na primeira execução)
mkdir -p $DIRARQ/vendas
echo "aqui criou o diretorio" 

#copiando o arquivo dados_de_vendas.csv para o diretório vendas
cp $DIRARQ/dados_de_vendas.csv $DIRARQ/vendas/

#extraindo a data do sistema e salvando o valor na variável data_do_sistema no 
#formato YYYYMMDD
#o símbolo $ serve para referenciar variáveis ou substituição de comando
#neste caso está servindo como substituição

data_do_sistema=$(date +%Y%m%d)

#criando o diretório backup dentro do diretório vendas (na primeira execução)
mkdir -p $DIRARQ/vendas/backup/

#copiando o arquivo dados_de_vendas.csv do diretório vendas para o diretório backup
cp $DIRARQ/vendas/dados_de_vendas.csv $DIRARQ/vendas/backup/

#renomeando o arquivo dados_de_vendas.csv da pasta backup no formato solicitado
#dados-YYYYMMDD.csv
mv $DIRARQ/vendas/backup/dados_de_vendas.csv $DIRARQ/vendas/backup/dados-$data_do_sistema.csv

#renomeando o arquivo do diretório backup para backup-dados-YYYYMMDD
mv $DIRARQ/vendas/backup/dados-$data_do_sistema.csv $DIRARQ/vendas/backup/backup-dados-$data_do_sistema.csv

#criando o relatório
echo $(date +%Y/%m/%d\ %H:%M) > $DIRARQ/vendas/backup/relatorio-$data_do_sistema.txt

#echo "aqui gerou o relatorio"

#Separando as informações do csv e pegando o campo data
awk -F, 'NR==2 {print "O primeiro registro foi feito em: " $5} END {print "O último registro foi feito em: " $5}' $DIRARQ/vendas/dados_de_vendas.csv >> $DIRARQ/vendas/backup/relatorio-$data_do_sistema.txt

#Contando a quantidade total de itens diferentes vendidos
awk -F, 'NR>1 {itens[$2]=1} END {print "Quantidade de itens diferentes vendidos: " length(itens)}' $DIRARQ/vendas/dados_de_vendas.csv >> $DIRARQ/vendas/backup/relatorio-$data_do_sistema.txt



#Exibindo as dez primeiras linhas do arquivo de backup e adicionando no relatório.txt
#echo "Pré-visualização do arquivo backup:" >> $DIRARQ/vendas/backup/relatorio-$data_do_sistema.txt
head -n 11 $DIRARQ/vendas/backup/backup-dados-$data_do_sistema.csv >> $DIRARQ/vendas/backup/relatorio-$data_do_sistema.txt

#Comprimindo o arquivo de backup para formato .zip
zip $DIRARQ/vendas/backup/backup-dados-$data_do_sistema.zip $DIRARQ/vendas/backup/backup-dados-$data_do_sistema.csv

echo aqui zipou

#Removendo os arquivos backup-dados-YYYYMMDD.csv e dados_de_vendas.csv
rm $DIRARQ/vendas/backup/backup-dados-$data_do_sistema.csv
rm $DIRARQ/vendas/dados_de_vendas.csv

echo "fim do script"

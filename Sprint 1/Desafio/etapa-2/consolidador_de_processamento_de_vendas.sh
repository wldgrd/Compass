#!/bin/bash
echo "Relatório Final" > relatorio_final.txt

#for relatorio in vendas/backup/relatorio-$data_do_sistema.txt; do
#	cat  "$relatorio" >> relatorio_final.txt
#	echo -e "\n" >> relatorio_final.txt
#done

cat vendas/backup/relatorio-*.txt > relatorio_final.txt 

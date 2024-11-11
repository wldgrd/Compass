#!/bin/bash
echo "Relatório Final" > relatorio_final.txt # Cria o arquivo relatorio_final.txt e escreve Relatório Final dentro dele

cat vendas/backup/relatorio-*.txt > relatorio_final.txt # Pega todos os arquivos cujo nome começa com relatorio- e que possuem a extensão .txt e os adiciona ao arquivo relatorio final.

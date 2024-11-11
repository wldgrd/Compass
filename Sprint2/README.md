# Resumo

**- SQL Para Análise de Dados:**  

Nesse curso aprendemos sobre a anatomia básica do SQL e suas principais cláusulas **SELECT**, **FROM**, **WHERE**, bem como comandos de ordenação como o **ORDER BY**, que por default possui o parâmetro **ASC** omitido e o **ORDER BY DESC** para ordenar dados em ordem decrescente, **LIMIT** para restringir a consulta a um número limitado de linhas. Por exemplo:  

```
SELECT
    coluna1,
    coluna2
FROM tabela
WHERE coluna1 = condição
ORDER BY coluna2 DESC
LIMIT 10
```

Aprendemos também sobre os operadores e seus variados tipos como **aritméticos, comparação, e lógicos.** Por exemplo:    

```
SELECT
    (coluna1/valor) AS coluna_renomeada1,
    coluna2,
    coluna3
FROM tabela
WHERE (coluna1 > condição) AND (coluna1 <> coluna2)
ORDER BY coluna3
LIMIT 10
```

Na parte de **funções de agregação** aprendemos como calcular o valor máximo (**MAX**), mínimo (**MIN**), contagem (**COUNT**), soma (**SUM**) e média (**AVG**), além do **GROUP BY** e do **HAVING**, sendo que este último funciona de modo muito semelhante à cláusula **WHERE**, porém é para ser usado após agrupamento e permite que sua condição envolva funções agregadas, coisa que não é permitida na cláusula **WHERE**.

```
SELECT
    MIN(coluna1) AS minimo_valor,
    MAX(coluna2) AS maior_valor,
    COUNT(coluna3) AS contagem_valores,
    SUM(coluna4) AS soma_dos_valores,
    AVG(coluna5) AS valor_medio,
    coluna6
FROM tabela
WHERE coluna1 = condição1
GROUP BY coluna6
HAVING condição2
ORDER BY coluna6 DESC
LIMIT 10
```

Na parte de **JOIN**, aprendemos como unir as tabelas necessárias para executar consultas a partir dos **LEFT JOIN, RIGHT JOIN, INNER JOIN, FULL JOIN**, que unem as tabelas de acordo com uma tabela referência.  

**LEFT JOIN:**  
- Une as tabelas tomando como referência a tabela da esquerda (primeira tabela declarada), isto é, copia a tabela da esquerda, busca os valores em que há a correspondência na tabela da direita e retorna **null** quando não há correspondência.

```
FROM tabela1 LEFT JOIN tabela2 ON tabela1.coluna = tabela2.coluna 
```
**RIGHT JOIN:**
- Une as tabelas tomando como referência a tabela da direita (segunda tabela declarada), isto é, copia a tabela da direita, busca os valores em que há a correspondência na tabela da esquerda e retorna **null** quando não há correspondência.  

```
FROM tabela1 RIGHT JOIN tabela2 ON tabela1.coluna = tabela2.coluna 
```  

**INNER JOIN:**  
- Une as tabelas retornando apenas os valores que possuem correspondência em ambas (interseção).  
```
FROM tabela1 INNER JOIN tabela2 ON tabela1.coluna = tabela2.coluna 
```  

**FULL JOIN:**  
- Une as tabelas inteiras, sem repetição, porém retorna **null** nas linhas onde não há correspondência entre as tabelas.
```
FROM tabela1 FULL JOIN tabela2 ON tabela1.coluna = tabela2.coluna 
```  

Na parte de uniões aprendemos dois modos de unir tabelas com repetição (**UNION ALL**) e sem repetição (**UNION**)

```
FROM tabela1 UNION ALL tabela2
```

```
FROM tabela1 UNION tabela2
```

Além disso, também aprendemos a fazer subqueries para auxiliar as consultas e preparar tabelas ou colunas prévias. As subqueries devem ser pensadas de acordo com a cláusula na qual serão executadas, pois subqueries na cláusula SELECT têm propósito diferente das subqueries na cláusula FROM, por exemplo.  

Aprendemos também como tratar dados (inserção, deleção, atualização), tratamento de strings, datas, conversão de unidades e construção de funções.

Por fim, aprendemos a criar e modificar a própria estrutura de tabelas (CREATE TABLE, DROP TABLE, UPDATE , ALTER TABLE), sendo também importante saber como popular as tabelas após criadas com suas respectivas condições de restrição, chaves primárias e secundárias para estabelecer as ligações corretas.


**AWS Skill Builder - AWS Partner: Sales Accreditation (Business):**  

Nesse curso aprendemos conceitos básicos de computação na nuvem e serviços da AWS, proposta de valor da AWS, possíveis objeções dos clientes e como vender com a AWS.

- **Modelos de implantação de computação em nuvem:**  
    - Software como serviço (SaaS)
    - Plataforma como serviço (PaaS)
    - Infraestrutura como serviço (IaaS)
    - Nuvem
    - On-premises
    - Híbrido  

- **Categorias de serviço:**  
    - Computação
    - Armazenamento
    - Banco de Dados
    - Segurança
    - Gerenciamento
    - Redes  

- **AWS Cloud Values**  
    - Economia de custos
    - Produtividade da equipe
    - Resiliência operacional
    - Agilidade empresarial  



# Links

[📜**Certificados**](/Sprint2/certificados/)  
[🕵️‍♂️**Evidências** ](/Sprint2/evidencias/README.md)  
[💪**Exercícios**](/Sprint2/Exercicios/)  
[🖳**Desafio - Parte 1 - Modelo Relacional**](/Sprint2/Desafio/etapa-1/)  
[🖳**Desafio - Parte 2 - Modelo Dimensional**](/Sprint2/Desafio/etapa-2/)

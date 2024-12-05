# 4.2 ETAPA 2
É possível reutilizar containers? Em caso positivo, apresente o comando necessário para 
reiniciar um dos containers parados em seu ambiente Docker? Não sendo possível reutilizar,
justifique sua resposta.
# -----------------------------------------  

Sim, é possivel reutilizar os containers Docker que foram parados.  

Para listar os containers que já foram executados na máquina, executa o comando: 

```bash
docker ps -a
```
Como resposta você obterá uma lista dos containers já rodados em sua máquina, como mostra a figura a seguir.

![docker ps -a ](../../Evidencias/dockerps-a_carguru.png)

Através da lista podemos obter o ID e o nome do container e então reutilizá-lo através do comando:

```bash
docker start <containerID>
```
ou ainda :
```bash
docker start <NomeDoContainer>
```  

É interessante ressaltar que os comandos servem tanto para o ID, quanto para o nome do container, mas também servem para parte do ID.

| **CONTAINER ID**   | **IMAGE**     | **COMMAND**               | **CREATED**          | **STATUS**                       | **PORTS** | **NAMES**         |
|----------------|-----------|-----------------------|------------------|------------------------------ |-------|---------------|
| 4e90b90161ec   | carguru   | "python carguru.py"   | 25 minutes ago   | Exited (0) About a minute ago |       | sharp_carver  |  

A tabela acima ilustra a primeira linha de resposta ao comando docker ps -a da figura anterior.  
Para iniciarmos o container, podemos executar os comandos:
```bash
docker start 4e90b90161ec
```
```bash
docker start sharp_carver
```

Ou ainda usando apenas parte do ID, por exemplo:
```bash
docker start 4e9
```

Abaixo segue figura ilustrando a execução com parte do ID e usando o terminal iterativo através da flag -ai.

```bash
docker start -ai 4e9
```
![start com parte do ID](../../Evidencias/start_parte_ID.png)


# Observações gerais  

Apesar de ser possível reutilizar containers, há situações em que a prática é mais ou menos recomendada.  
A arquitetura de construção Docker permite que possamos tratar os containers como descartáveis, pois isso pode ajudar a eliminar quaisquer inconsistências ou resíduos que estiverem no projeto a ser executado.  
Por outro lado, reutilizar containers pode ser uma forma de economia de tempo caso o ambiente seja estável e se você deseja manter as configurações utilizadas anteriormente.  
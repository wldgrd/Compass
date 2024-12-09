# Resumo
# Para rodar um container:

**docker run <nome_do_container>** --> executa e para

**docker run -it <nome_do_container>** --> executa e mantém aberto 'modo de iteração'

**docker ps** ou **docker container ls** -->  exibe quais containers estão sendo executados no momento

utilizando a flag -a, temos também todos os containers já executados na máquina: **docker ps -a** ou **docker container ls -a**


# Container != VM:	
- container é uma aplicação que serve para determinado fim,**não possui sistema operacional**, seu tamanho é de alguns MBs  
- **VM** possui S.O. próprio, tamanho de GBs, pode executar diversas funções  
- Containers acabam gastando menos recursos para serem executados, por causa do seu uso específico  
- VMs gastam mais recursos, porém podem exercer mais funções  

# Executar container no background  

- quando iniciamos um container que persiste, **ele fica ocupando o terminal**  
- podemos executar em background, para não ficar com várias abas de terminal aberto  
- comando: **docker run -d \<container>** 

# Expondo portas  
- Os containers de docker não têm conexão com nada de fora deles  
- Por isso, precisamos expor portas, a flag é **-p** e podemos fazer assim: **-p 80:80**  
- **docker run -d -p 80:80 \<container>** --> modo background e expõe a porta 80  
- **docker stop \<container>** serve para parar  container    

# Parando Containers  
- **docker stop \<nomeDoContainer>**

# Reiniciando Containers  

- **docker start \<id>**  
- lembre-se que o **run** sempre cria um container novo  

# Definindo Nome do Container  

- usamos a flag **--name**  
- se não colocamos, recebemos um **nome aleatório**, que pode ser um problema para uma aplicação profissional  
- a flag **run** é inserida junto do **comando run**  
- docker run -d -p 80:80 --name nginx_app nginx  

# Verificando os logs  

- Podemos verificar **o que aconteceu com um container**
- **docker logs \<id>**

# Removendo Container  

- Podemos **remover um container da máquina** que estamos executando o docker  
- Comando: **docker rm \<id>**  
- se o container estiver rodando ainda, podemos utilizar a **flag -f** (force)  
- O container removido não é mais listado em docker ps -a  

# Criando uma imagem  

- Para criar uma imagem você precisará de um arquivo **Dockerfile** em uma pasta que ficará o projeto  
- Este arquivo precisará de algumas instruções para ser executado  
- **FROM**: imagem base  
- **WORKDIR**: diretório da aplicação  
- **EXPOSE**: porta da aplicação  
- **COPY**: quais arquivos precisam ser copiados  
- **CMD**: define o comando padrão que sera executado quando o container for iniciado.

# Links
[📜**Certificados**](/Sprint4/Certificados/)  
[🕵️‍♂️**Evidências** ](/Sprint4/Evidencias/)  
[💪**Exercícios**](/Sprint4/Exercicios/)  
[🖳**Desafio**](/Sprint4/Desafio/README.md)  
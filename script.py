#Aula de GIT

#Comandos
## git init - inicializa o git em determinada pasta/local
## git status - verifica os arquivos da pasta
## git add "nome do arquivo.txt" - adiciona o arquivo no git
## git add . - adiciona todos os arquivos da pasta no git
## git commit -m "commit inicial" - adiciona uma nova versão do projeto * uma boa prática é commitar inicial
## git remote origin *link do repositório no github* - adiciona o link do repositório que você quer
## git push - sobe o projeto para o github
## git reflog - mostra as versões do projeto // a versão mais atual é sempre a do topo
## git reset --hard *id da versão* - retorna uma versão do projeto
## git branch - mostra quais branchs estão disponíveis
## git branch *nome da branch* - adiciona uma nova branch
## git checkout *nome da branch* - altera para a branch que você quer
## git merge *nome da branch que será puxada* - junta as alterações de uma branch em outra // atenção, você tem que estar dentro da branch que SERÁ ATUALIZADA, ou seja, ir para a branch principal, e depois dar o comando
##

#Branchs
## São ramificações do projeto durante o processo de desenvolvimento

#Merge
## É a junção de uma branch paralela para a branch principal
## Sempre que eu entrar na branch principal, antes de fazer o merge, é preciso puxar as atualizações que estão no servidor, para a minha máquina
## para ter certeza que estou unindo os códigos nas versões mais atuais possíveis.
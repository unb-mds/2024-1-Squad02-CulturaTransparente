# Documento de Arquitetura
Esse é o documento em que detalhamos a arquitetura do nosso software, explicando tecnologias e funcionalidades.

## Introdução
O projeto Cultura Transparente tem o objetivo de exibir aos usuários do site como o dinheiro do estado do Rio de Janeiro vem sendo gasto nas diferentes formas culturais.

### Diagrama de Arquitetura
Para acessar o nosso diagrama, clique [aqui](https://miro.com/app/board/uXjVKXbbl50=/#tpicker-content)!

### Tecnologias
O Software consiste em algumas camadas com tecnologias diferentes, abaixo apresentamos cada uma delas.
#### Camada de apresentação
A camada de apresentação, ou o front-end, é responsável por interagir com o usuário e exibir os dados que ele deseja através das análises feitas sobre os arquivos coletados pelo Scrapper.
As tecnologias usadas nessa camada são JavaScript, NodeJs e o framework React.

#### Coleta e análise de dados
A coleta de dados funciona usando um web-scrapping que baixa os arquivos diretamente dos sites dos diários oficiais dos municípios do Rio de Janeiro usando as tecnologias e bibliotecas
do Python. Após o download, ocorre a análise de dados dos arquivos baixados usando REGEX, em Python também.

#### Aplicação
Nós utilizaremos o Docker para que todos possam rodar o projeto com as dependências corretas e em sistemas operacionais diferentes, tendo em vista que
não é sempre que todos tem o mesmo versionamento de uma dependência ou outra, e a tecnologia do Docker permite evitar esse problemas e por isso estaremos utilizando.

# Feiras API


** Sistema de cadastro de Feiras **

## Funcionalidades

* Importa registro de feiras da Prefeitura de São Paulo através de script;
* Cadastra feiras
* Edita feiras
* Apaga feiras
* Busca feiras por nome

Este projeto foi inicialmente desenvolvido como a microframework Flask (http://flask.pocoo.org/)
A interface exibida foi contruida com javascript, JQuery, e os componentes JEasyUI (https://www.jeasyui.com/)

## Importar dados

Faça o download do o arquivo CSV fornecido pela Prefeitura de São Paulo em: http://www.prefeitura.sp.gov.br/cidade/secretarias/upload/chamadas/feiras_livres_1429113213.zip
Execute o script ImportCsvScript.py
selecione o arquivo CSV e clique em OK

## Como usar

Execute o aplicativo e em seguida navegue até o endereço http://127.0.0.1/home/ utilizando um navegador web de sua preferência

### Inserir

Para inserir, clique em Nova Feira, preencha todos os dados requiridos e clique em Salvar

### Editar

Para editar, selecione na grade o registro desejado, clique no botão Editar Feira, modifique os dados desejados e clique em Salvar

### Apagar

Para apagar, selecione na grade o registro desejado, clique no botão Apagar Feira, em seguida clique em OK

### Buscar feira por nome

Para buscar um registro, preencha o campo de texto ao lado do botão Pesquisar Nome com o nome da feira desejada,
em seguida, clique no botão Pesquisar Nome. A grade irá exibir todas as feiras que contenham o nome digitado na sua descrição.

### Atualizar

Retorna a grade ao seu estado original

# Aplicação CRUD

Esta é uma aplicação simples de CRUD (Criar, Ler, Atualizar, Deletar) usando Python, Flask para a interface web e JSON para armazenamento de dados.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:


```
Crud_python_frontendHtmlCss_json/
├── data/
│ └── persons.json # Arquivo JSON onde os dados das pessoas são armazenados
├── src/
│ ├── crud_logic.py # Módulo com a lógica de CRUD
│ ├── app.py # Módulo com o servidor Flask
│ ├── templates/
│ │ └── index.html # Página HTML para a interface
│ └── static/
│ ├── css/
│ │ └── styles.css # Arquivo CSS para estilização
├── README.md # Arquivo de documentação do projeto
└── main.py # Arquivo principal para iniciar a aplicação
```


### `data/persons.json`
Arquivo JSON que armazena os dados das pessoas. Se não existir, será criado automaticamente ao iniciar a aplicação.

### `src/crud_logic.py`
Módulo que contém a lógica de CRUD para gerenciar pessoas. Funções principais:
- `get_persons()`: Retorna a lista de pessoas.
- `add_person(name, phone, email)`: Adiciona uma nova pessoa.
- `update_person(person_id, name, phone, email)`: Atualiza uma pessoa existente.
- `delete_person(person_id)`: Deleta uma pessoa.
- `search_person(query)`: Busca pessoas pelo nome.
- `create_empty_json()`: Cria um arquivo JSON vazio se não existir.

### `src/app.py`
Módulo que contém a lógica do servidor Flask e rotas para o CRUD.

### `src/templates/index.html`
Página HTML que exibe a interface da aplicação CRUD.

### `src/static/css/styles.css`
Arquivo CSS para estilização da página HTML.

## Funcionalidades

- **Adicionar Pessoa**: Adicione uma nova pessoa com nome, telefone e email.
- **Buscar Pessoa**: Busque pessoas pelo nome.
- **Atualizar Pessoa**: Atualize os detalhes de uma pessoa existente.
- **Deletar Pessoa**: Delete uma pessoa.
- **Exibir Lista de Pessoas**: Veja a lista de todas as pessoas cadastradas.
- **Criação Automática de Arquivo JSON**: Se o arquivo `persons.json` não existir, ele será criado automaticamente com uma lista vazia.

## Exemplo de Uso

### Adicionar uma Pessoa

- Preencha os campos "Nome", "Telefone" e "Email".
- Clique no botão "Adicionar".

### Buscar uma Pessoa

- Digite o nome da pessoa no campo "Nome".
- Clique no botão "Buscar".

### Atualizar uma Pessoa

- Selecione uma pessoa da lista exibida.
- Os campos serão preenchidos com os dados da pessoa selecionada.
- Modifique os campos conforme necessário.
- Clique no botão "Atualizar".

### Deletar uma Pessoa

- Selecione uma pessoa da lista exibida.
- Clique no botão "Deletar".
- Confirme a exclusão na janela de diálogo que aparecer.

### Exibir Lista de Pessoas

- Todas as pessoas cadastradas são exibidas na lista.

## Como Executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Instale as dependências necessárias com o comando:
    ```bash
    pip install flask
    ```
3. Execute o arquivo `main.py` para iniciar a aplicação:
    ```bash
    python main.py
    ```

A aplicação estará disponível em `http://127.0.0.1:5000/`, onde você pode interagir com a interface CRUD na web.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests para melhorias e correções.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para obter mais informações.
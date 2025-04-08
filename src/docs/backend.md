

## Database (database.py)

O módulo `database.py` contém a configuração do banco de dados e a definição dos modelos utilizando SQLAlchemy.

### Classe `Base`

Base para declaração dos modelos SQL Alchemy.

### Classe `Atendimentos`

Define o modelo de dados para os atendimentos.

| Campo     | Tipo    | Descrição                              |
|-----------|---------|----------------------------------------|
| id        | Integer | Identificador único (Primary Key)      |
| motivo    | String  | Motivo do atendimento (até 200 caracteres) |
| canal     | String  | Canal de atendimento (até 50 caracteres) |
| origem    | String  | Origem do atendimento (até 50 caracteres) |
| gravidade | Integer | Nível de gravidade (1-5)               |

#### Classe `Database_config`

Responsável pela configuração e criação da conexão com o banco de dados SQLite.

Métodos principais:
- `_database_path()`: Retorna o caminho para o arquivo do banco de dados
- `_database_url()`: Constrói a URL de conexão para o SQLite
- `_get_engine()`: Cria e retorna uma instância do engine de banco de dados

### CRUD (crud.py)

O módulo `crud.py` implementa operações de CRUD (Create, Read, Update, Delete) para gerenciar atendimentos.

#### Classe `CRUD`

Fornece métodos para interação com o banco de dados:

| Método                | Descrição                                  |
|-----------------------|--------------------------------------------|
| `create_service()`    | Cria um novo registro de atendimento       |
| `update_service()`    | Atualiza um atendimento existente pelo ID  |
| `delete_service()`    | Remove um atendimento pelo ID              |
| `read_a_service()`    | Busca um atendimento específico pelo ID    |
| `read_all_services()` | Retorna todos os atendimentos cadastrados  |

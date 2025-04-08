
## Personalizando o Banco de Dados

O banco de dados SQLite é configurado no arquivo `database.py`. Para utilizar outro banco de dados, modifique o método `_database_url()` na classe `Database_config`.

## Estendendo o Modelo de Dados

Para adicionar novos campos ao modelo `Atendimentos`:

1. Atualize a classe `Atendimentos` em `database.py`
2. Modifique os métodos correspondentes em `crud.py` se necessário
3. Atualize a interface do usuário em `app.py` para incluir os novos campos
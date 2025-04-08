## Visão Geral

O Sistema de Gerenciamento de Atendimentos é uma aplicação web que permite registrar, visualizar, atualizar e excluir atendimentos. A aplicação utiliza Streamlit para a interface de usuário e SQLAlchemy para interação com o banco de dados de sua escolha.

## Estrutura do Projeto

```
src/
├── backend/
│   ├── __init__.py
│   ├── crud.py      # Operações CRUD para gerenciamento de atendimentos
│   └── database.py  # Configuração do banco de dados e definição do modelo
├── frontend/
│   ├── __init__.py
│   └── app.py       # Interface Streamlit para a aplicação
└── main.py          # Ponto de entrada da aplicação
```

## Fluxo de Dados

1. O usuário interage com a interface Streamlit
2. As requisições são processadas pela classe `AtendimentoApp`
3. A classe `CRUD` é responsável pelas operações no banco de dados
4. Os dados são armazenados/recuperados da tabela `atendimentos` no banco de dados escolhido.

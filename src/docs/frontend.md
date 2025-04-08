
## App (app.py)

O módulo `app.py` contém a interface de usuário implementada com Streamlit.

### Classe `AtendimentoApp`

Implementa a interface para todas as operações CRUD de atendimentos.

Métodos principais:

| Método             | Descrição                                        |
|--------------------|-------------------------------------------------|
| `run()`            | Inicia a aplicação e controla o fluxo principal |
| `view_page()`      | Página para visualizar atendimentos             |
| `create_page()`    | Página para criar novos atendimentos            |
| `update_page()`    | Página para atualizar atendimentos existentes   |
| `delete_page()`    | Página para excluir atendimentos                |
| `display_form()`   | Exibe formulário para entrada de dados          |
| `mostrar_tabela()` | Exibe dados em formato de tabela                |

### Main (main.py)

O arquivo `main.py` é o ponto de entrada da aplicação, instanciando a aplicação Streamlit e iniciando sua execução.
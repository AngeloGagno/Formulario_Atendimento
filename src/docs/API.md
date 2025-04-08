## API Interna

### Backend API

#### CRUD

```python
# Criar um novo atendimento
CRUD().create_service(motivo='Descrição', canal='Email', origem='Site', gravidade=3)

# Atualizar um atendimento existente
CRUD().update_service(id=1, motivo='Nova descrição')

# Excluir um atendimento
CRUD().delete_service(id=1)

# Buscar um atendimento específico
atendimento = CRUD().read_a_service(id=1)

# Listar todos os atendimentos
atendimentos = CRUD().read_all_services()
```

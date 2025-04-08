
## Erro ao iniciar o container Docker
- Verifique se as portas necessárias estão disponíveis
- Certifique-se de que o arquivo docker-compose.yml está configurado corretamente

## Erro de conexão com o banco de dados
- Verifique se o diretório onde o SQLite armazena o arquivo possui permissões de escrita
- Certifique-se de que o contêiner tem acesso ao volume onde o banco de dados está armazenado
- Verifique a string de conexão do banco e se o IP da máquina utilizada está autorizado pela provedora do banco.
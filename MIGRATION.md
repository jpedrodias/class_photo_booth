# Migração Manual da Base de Dados - Redis Queue

## Objetivo
Adicionar suporte para tracking de tarefas de email assíncronas usando Redis Queue.

## Comando SQL Necessário

Execute o seguinte comando na sua base de dados:

```sql
ALTER TABLE pre_users ADD COLUMN email_job_id VARCHAR(36);
```

## Detalhes da Migração

### Campo Adicionado
- **Tabela**: `pre_users`
- **Campo**: `email_job_id`
- **Tipo**: `VARCHAR(36)`
- **Nullable**: Sim (para compatibilidade com dados existentes)
- **Propósito**: Armazenar o ID das tarefas RQ para tracking do envio de emails

### Como Executar

#### Para SQLite (desenvolvimento local):
```bash
# Conectar à base de dados SQLite
sqlite3 flaskapp/instance/database.sqlite

# Executar a migração
ALTER TABLE pre_users ADD COLUMN email_job_id VARCHAR(36);

# Verificar se foi adicionada
.schema pre_users

# Sair
.quit
```

#### Para PostgreSQL (produção):
```bash
# Conectar à base de dados
psql -h localhost -U seu_usuario -d sua_base_dados

# Executar a migração
ALTER TABLE pre_users ADD COLUMN email_job_id VARCHAR(36);

# Verificar se foi adicionada
\d pre_users

# Sair
\q
```

#### Usando Adminer (interface web):
1. Acesse `http://localhost:8081`
2. Faça login na base de dados
3. Selecione a tabela `pre_users`
4. Vá para "SQL command"
5. Execute: `ALTER TABLE pre_users ADD COLUMN email_job_id VARCHAR(36);`

## Verificação da Migração

Depois de executar o SQL, pode verificar se a migração foi bem-sucedida conectando-se à base de dados e verificando a estrutura da tabela `pre_users`.

### Para SQLite:
```bash
sqlite3 flaskapp/instance/database.sqlite
.schema pre_users
.quit
```

### Para PostgreSQL:
```bash
psql -h localhost -U seu_usuario -d sua_base_dados
\d pre_users
\q
```

Deve ver o campo `email_job_id VARCHAR(36)` na estrutura da tabela.

## Compatibilidade

- **Dados existentes**: Não são afetados (campo é nullable)
- **Versões anteriores**: Continuam a funcionar sem problemas
- **Rollback**: Se necessário, use `ALTER TABLE pre_users DROP COLUMN email_job_id;`

## Próximos Passos

Depois da migração:
1. Execute `docker-compose up` para iniciar a aplicação
2. O worker RQ será iniciado automaticamente em background
3. Os novos registos terão tracking de email automático
4. Use as APIs `/api/job_status/<job_id>` e `/api/email_jobs` para monitorização

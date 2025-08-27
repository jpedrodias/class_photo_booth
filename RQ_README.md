# Redis Queue - Envio Assíncrono de Emails

## Visão Geral

Foi implementado um sistema de filas com Redis Queue (RQ) para tornar todas as operações de envio de email assíncronas. Isto melhora significativamente a experiência do utilizador, pois as operações não ficam bloqueadas a aguardar o envio de emails.

## Alterações Realizadas

### 1. Dependências Adicionadas
- **rq**: Biblioteca Redis Queue para Python
- Adicionada ao `requirements.txt`

### 2. Novos Arquivos Criados

#### `tasks.py`
Contém as tarefas assíncronas para envio de emails:
- `send_verification_email()`: Envio de email de verificação
- `send_password_reset_email()`: Envio de email de recuperação de password
- `send_account_updated_email()`: Envio de email de notificação de conta atualizada

#### `worker.py`
Script do worker RQ que processa as tarefas em background.

#### `migrate_db.py`
Script para migração da base de dados (adiciona campo `email_job_id` à tabela `pre_users`).

#### `start_with_rq.sh`
Script de inicialização que executa a migração e depois inicia a aplicação.

### 3. Alterações na Configuração

#### `config.py`
- Adicionadas configurações do Redis Queue:
  - `RQ_REDIS_URL`: URL de conexão ao Redis (database 1)
  - `RQ_DEFAULT_TIMEOUT`: Timeout padrão para as tarefas (300 segundos)

#### `docker-compose.yml`
- Adicionado serviço `rq_worker` para processar tarefas
- Alterado comando do `flaskapp` para usar `start_with_rq.sh`

### 4. Alterações na Aplicação Principal

#### `app.py`
- **Importações**: Adicionadas importações do RQ (`Queue`, `Job`)
- **Configuração**: Inicialização da queue de emails
- **Endpoints API**: 
  - `/api/job_status/<job_id>`: Verificar status de uma tarefa
  - `/api/email_jobs`: Listar todas as tarefas na queue
- **Modelos**: Adicionado campo `email_job_id` ao modelo `PreUser`
- **Funções de Email**: Substituído envio síncrono por tarefas assíncronas

#### `templates/login.html`
- **JavaScript**: Adicionado monitoramento automático do status das tarefas
- **UI**: Feedback visual em tempo real sobre o estado do envio de emails

## Como Funciona

### 1. Envio de Email
Quando uma operação requer envio de email:
1. Uma tarefa é adicionada à queue Redis
2. O utilizador recebe feedback imediato
3. O worker processa a tarefa em background
4. O frontend monitoriza o progresso via API

### 2. Monitorização
O frontend verifica automaticamente o status das tarefas a cada 3 segundos:
- **Queued**: Email na fila de envio
- **Started**: A enviar email
- **Finished**: Email enviado com sucesso
- **Failed**: Erro no envio

### 3. Feedback Visual
Estados visuais no frontend:
- 🔵 **Azul**: Processando
- 🟢 **Verde**: Sucesso
- 🟡 **Amarelo**: Erro
- ⚪ **Cinza**: Estado desconhecido

## Vantagens

### Para o Utilizador
- **Resposta Imediata**: Não precisa aguardar o envio do email
- **Feedback Visual**: Sabe o estado do envio em tempo real
- **Melhor UX**: Interface não trava durante operações de email

### Para o Sistema
- **Performance**: Operações não bloqueantes
- **Escalabilidade**: Fácil adicionar mais workers
- **Reliability**: Retry automático em caso de falha
- **Monitoring**: APIs para monitorização das tarefas

## Configuração e Execução

### 1. Migração da Base de Dados (MANUAL)
Antes de iniciar a aplicação, execute o seguinte comando SQL na sua base de dados:

```sql
ALTER TABLE pre_users ADD COLUMN email_job_id VARCHAR(36);
```

**📋 Consulte o arquivo `MIGRATION.md` para instruções detalhadas por tipo de base de dados.**

### 2. Iniciar a Aplicação
```bash
docker-compose up
```

A aplicação irá:
1. Aguardar o Redis estar disponível
2. Iniciar o worker RQ em background (com auto-restart em caso de falha)
3. Iniciar a aplicação Flask principal
4. Processar emails automaticamente em background

### 3. Arquitetura Simplificada
- **Um único serviço Docker**: `flaskapp`
- **Worker RQ integrado**: Roda em background no mesmo container
- **Auto-restart**: Worker reinicia automaticamente se falhar
- **Monitorização**: Loop infinito com delay de 5 segundos entre restarts

### Variáveis de Ambiente
```bash
# Redis Queue (opcional - tem defaults)
RQ_REDIS_URL=redis://redis:6379/1
RQ_DEFAULT_TIMEOUT=300
```

## Estrutura dos Serviços

```
┌─────────────────────────────────┐    ┌─────────────┐
│         flaskapp                │    │    Redis    │
│  ┌─────────────┐ ┌─────────────┐│    │   Queue     │
│  │   Flask     │ │  RQ Worker  ││◀──▶│             │
│  │    App      │ │ (background)││    │             │
│  └─────────────┘ └─────────────┘│    └─────────────┘
└─────────────────────────────────┘           │
              │                               │
              │         ┌─────────────┐       │
              └────────▶│    SMTP     │◀──────┘
                        │   Server    │
                        └─────────────┘
```

### Vantagens desta Arquitetura
- **Simplicidade**: Apenas um serviço Docker para a aplicação
- **Robustez**: Worker reinicia automaticamente em caso de falha
- **Eficiência**: Menos overhead de containers
- **Facilidade**: Mais fácil de debuggar e monitorizar

## APIs Disponíveis

### GET /api/job_status/<job_id>
Retorna o status de uma tarefa específica.

**Resposta:**
```json
{
  "job_id": "abc123",
  "status": "finished",
  "progress": 100,
  "message": "Email enviado com sucesso",
  "error": ""
}
```

### GET /api/email_jobs
Lista todas as tarefas na queue de emails.

**Resposta:**
```json
{
  "queue_length": 2,
  "jobs": [
    {
      "job_id": "abc123",
      "status": "finished",
      "progress": 100,
      "created_at": "2025-01-01T10:00:00",
      "started_at": "2025-01-01T10:00:01",
      "ended_at": "2025-01-01T10:00:05"
    }
  ]
}
```

## Troubleshooting

### Worker não está a processar tarefas
1. Verificar se o serviço `rq_worker` está em execução
2. Verificar logs: `docker-compose logs rq_worker`
3. Verificar conectividade ao Redis

### Emails não chegam
1. Verificar configurações SMTP no `.env`
2. Verificar logs do worker para erros de envio
3. Usar API `/api/job_status/<job_id>` para ver detalhes do erro

### Migração da base de dados falha
1. Verificar se a base de dados está acessível
2. Executar manualmente: `python migrate_db.py`
3. Se persistir, eliminar e recriar as tabelas

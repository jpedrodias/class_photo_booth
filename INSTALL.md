# INSTALL.md – Guia de Instalação e Deploy

Este ficheiro descreve como instalar, configurar e executar a aplicação Class Photo Booth, sobretudo usando Docker Compose (modo recomendado).

## Sumário rápido

- Preparar o `.env` com variáveis de ambiente
- Iniciar com Docker Compose em desenvolvimento
- Preparar Gunicorn para produção

## Requisitos

- Docker e Docker Compose
- Um ficheiro `.env` configurado (veja secção abaixo)

## Exemplo mínimo de `.env`

```env
# Aplicação
FLASKAPP_DEBUG=True
FLASKAPP_SECRET_KEY=troca-esta-chave-por-uma-segura

# Email (SMTP)
MAIL_SERVER=smtp.example.com
MAIL_PORT=587
MAIL_USERNAME=seu-email@example.com
MAIL_PASSWORD=sua-senha
MAIL_DEFAULT_SENDER="Class Photo Booth <seu-email@example.com>"

# Redis
REDIS_HOST=redis
REDIS_PORT=6379
REDIS_DB=0

# Docker (opcional)
TZ=Europe/Lisbon
UID=1000
GID=1000
```

## Iniciar em modo desenvolvimento (Docker)

Abra um terminal (PowerShell no Windows) na raiz do repositório e execute:

```powershell
docker compose up
```

Aceda a `http://localhost:5000` (ou à porta configurada).

Para executar em background:

```powershell
docker compose up -d
```

## Inicialização da Base de Dados

Após iniciar os contentores pela primeira vez, execute o seguinte comando para criar a base de dados e o utilizador administrador:

```powershell
docker exec -it flaskapp /bin/bash -c "python ./init_database.py"
```

Parar os serviços:

```powershell
docker compose down
```

## Preparar para produção

1. Defina `FLASKAPP_DEBUG=False` no `.env`.
2. No `docker-compose.yml`, altere o comando do serviço Flask para usar Gunicorn:

```yaml
command: gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

Escolha `-w <NUM_WORKERS>` com base no número de CPUs disponíveis.

## Verificações básicas após iniciar

- Aceder com o utilizador 'admin@example.com' e password 'ChangeMe1#'.
- Confirmar envio de emails de verificação (se SMTP configurado)
- Importar CSV de teste e verificar uploads/renomeações de fotos
- Conferir painel Redis em `/settings` para sessões e estatísticas

## Recomendações e boas práticas

- Backup regular da base de dados e das pastas de fotos
- Usar proxy reversa (nginx) e HTTPS em produção
- Proteger `.env` e segredos

Se precisar, posso adicionar exemplos de `docker-compose.yml` e de configuração de Gunicorn.

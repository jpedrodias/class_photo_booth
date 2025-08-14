# INSTALL.md – Guia de Instalação e Deploy

Este guia detalha todos os passos necessários para instalar, configurar e colocar em produção a aplicação **Class Photo Booth** usando Docker Compose.

---

## 1. Clonar o Repositório

```bash
git clone https://github.com/jpedrodias/class_photo_booth.git
cd class_photo_booth
```

## 2. Configurar o Ficheiro `.env`

- Copie o ficheiro `.env.example` para `.env` (se existir) ou crie um novo `.env`.
- Edite as variáveis conforme o seu ambiente:
  - `FLASKAPP_SECRET_KEY`: Chave secreta para sessões Flask
  - `MAIL_SERVER`, `MAIL_PORT`, `MAIL_USERNAME`, `MAIL_PASSWORD`, `MAIL_SENDER`: Configuração de email
  - `REDIS_HOST`, `REDIS_PORT`, `REDIS_DB`: Configuração do Redis
  - `FLASKAPP_DEBUG`: Defina como `False` para produção
  - Outros parâmetros conforme necessário

> **Nota:** Guarde o ficheiro `.env` em local seguro. Não partilhe credenciais.

## 3. Iniciar os Serviços em Modo de Desenvolvimento

```bash
docker compose up
```

- Aguarde até todos os containers estarem prontos.
- Aceda à aplicação em [http://ip_servidor:5000](http://ip_servidor:5000) ou na porta definida em `.env`.
- Verifique os logs no terminal para eventuais erros.

## 4. Verificar Funcionamento

- Crie a primeira conta (será admin).
- Teste envio de email (verificação e recuperação de password).
- Teste upload de CSV, captura de fotos, downloads ZIP/DOCX.
- Verifique os painéis Redis em `/settings`.
- Confirme que as sessões estão a ser guardadas em Redis.

## 5. Parar os Serviços

```bash
docker compose down
```

---

## 6. Preparar para Produção (Gunicorn)

- Edite o ficheiro `docker-compose.yml`:
  - Altere o comando do serviço Flask para usar Gunicorn:
    ```yaml
    command: gunicorn -w <NUM_WORKERS> -b 0.0.0.0:5000 app:app
    ```
  - Substitua `<NUM_WORKERS>` pelo número de CPUs disponíveis (ex: 2, 4, 8). Recomenda-se `número de CPUs x 2` para aplicações web.
  - Certifique-se que o modo debug está desativado (`FLASKAPP_DEBUG=False` no `.env`).
  - Opcional: configure volumes e rede conforme o ambiente.

> **Exemplo de comando Gunicorn:**
> `gunicorn -w 4 -b 0.0.0.0:5000 app:app`

## 7. Iniciar em Modo Detach (Produção)

```bash
docker compose up -d
```

- Os serviços vão iniciar em background.
- Verifique os logs com:
  ```bash
  docker compose logs flaskapp
  docker compose logs redis
  docker compose logs postgres
  ```
- Para parar os serviços:
  ```bash
  docker compose down
  ```

---

## Recomendações Adicionais para Administradores

- **Backups:** Faça backup regular da base de dados e das pastas de fotos.
- **Segurança:** Proteja o acesso ao servidor, utilize firewalls e mantenha as credenciais seguras.
- **Dica de Segurança Adicional:**
  - Só ative o reencaminhamento externo (ex: abrir portas no router/firewall) para o servidor **depois** de criar o primeiro utilizador (admin).
  - Se o IP do servidor for externo (acesso público), coloque o serviço atrás de uma proxy reversa como **nginx** para proteger contra acessos diretos e facilitar HTTPS.
- **Atualizações:** Antes de atualizar, faça backup e teste em ambiente de desenvolvimento.
- **Monitorização:** Utilize os painéis de administração para monitorizar sessões, Redis, e estado do sistema.
- **Recuperação:** Em caso de erro, consulte os logs e a documentação (`README.md`, `SPECIFICATIONS.md`).
- **Volumes Docker:** Certifique-se que os volumes estão configurados para persistência dos dados entre reinicializações.
- **Ambiente:** Para produção, utilize sempre Gunicorn e desative o modo debug.

---

**Dúvidas ou problemas? Consulte a documentação ou abra uma issue no GitHub.**

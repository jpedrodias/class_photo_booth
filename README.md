# Class-Photo-Booth
O objetivo da aplicação **Class Photo Booth** é permitir a captura de fotografias de alunos por turma. A aplicação facilita a gestão, visualização e exportação das fotografias de forma organizada.

## � Alterações Recentes

- **Sessões Flask migradas para Redis (RAM-only)**: Utiliza Flask-Session com backend Redis, configurado para não persistir dados em disco (apenas memória).
- **Serialização das sessões com msgpack**: Maior compatibilidade e performance.
- **Configuração por variáveis de ambiente (.env)**: Email, Redis, debug, etc. agora configuráveis por .env.
- **Painéis de monitorização Redis**: Novos painéis em `settings.html` para monitorizar estado do Redis e sessões, com auto-refresh e debug.
- **Logout robusto**: Remove explicitamente a sessão do Redis.
- **Limpeza manual/automática de sessões**: Rotas administrativas para listar e limpar sessões expiradas ou inválidas.
- **Função JS para mostrar/ocultar senha**: Melhor usabilidade nos modais de alteração de password.
- **Exposição de erros para debugging**: Blocos try removidos em pontos críticos para facilitar debugging.
- **Atualização de requirements.txt**: Adicionado `msgpack` como dependência.

- **Funcionalidade PWA (Progressive Web App)**: Permite adicionar a aplicação à tela principal do telemóvel com ícone personalizado e nome, para experiência mobile otimizada.

## 📋 Funcionalidades
```
📸 CLASS PHOTO BOOTH v5.0
Sistema Completo de Gestão de Fotografias Escolares

  🔐 SISTEMA DE AUTENTICAÇÃO COMPLETO
  ├─ 📧 Registo com verificação por email
  ├─ 🔑 Login seguro com proteção anti-brute force
  ├─ 🔄 Recuperação de password via email
  ├─ 👥 Sistema de roles (none/viewer/editor/admin)
  ├─ 🛡️ Bloqueio automático de IPs suspeitos
  ├─ 📊 Auditoria completa de acessos
  └─ 👤 Utilizador 'admin@example.com' criado por defeito

  👤 GESTÃO AVANÇADA DE UTILIZADORES
  ├─ ➕ Criação de contas com validação de email
  ├─ ✏️ Edição de dados e permissões
  ├─ 🔑 Reset de passwords por administradores
  ├─ � Gestão de roles e permissões hierárquicas
  ├─ 📋 Tabela administrativa completa
  ├─ ✅ Aprovação manual de novos utilizadores
  └─ 🔒 Controlo granular de acesso por funcionalidade

  �🏠 GESTÃO DE TURMAS (Admin)
  ## Class Photo Booth

  O Class Photo Booth é uma aplicação web para captura, gestão e exportação de fotografias de alunos por turma.

  Este repositório contém o código-fonte, templates e scripts necessários para executar a aplicação em ambiente de desenvolvimento ou produção.

  ## Sumário (rápido)

  - Visão geral e funcionalidades: gerenciamento de turmas, alunos, captura de fotos, geração de DOCX e downloads em ZIP.
  - Autenticação completa com verificação por email, recuperação de password e roles (none, viewer, editor, admin).
  - Sessões em Redis, suporte PWA, processamento de imagem com OpenCV/Pillow.

  Para instruções de instalação e deploy consulte `INSTALL.md`. Para a especificação técnica complète e arquitetura consulte `SPECIFICATIONS.md`.

  ---

  ## Principais funcionalidades

  - Autenticação e verificação por email
  - Gestão de utilizadores com roles e permissões
  - CRUD de turmas e alunos, importação via CSV (replace/merge)
  - Captura de fotos com suporte a múltiplas câmaras e geração de thumbnails
  - Downloads por turma: ZIP (originais/thumbs) e DOCX com layout profissional
  - Painel administrativo com monitorização de sessões Redis e gestão de utilizadores

  ## Contribuições

  Contribuições são bem-vindas. Use issues e pull requests. Consulte `SPECIFICATIONS.md` para detalhes técnicos.

  ## Licença e Contacto

  Projeto licenciado sob MIT. Para questões: jpedrodias@gmail.com
FLASKAPP_NAME=class-photo-booth
FLASKAPP_FILE=app.py
FLASKAPP_PORT=80
FLASKAPP_DEBUG=True
FLASKAPP_SECRET_KEY=your-secret-key-here

# Configurações de email
MAIL_USERNAME=your-email@outlook.com
MAIL_PASSWORD=your-password
MAIL_SENDER=Class Photo Booth <your-email@outlook.com>

# Configurações Docker
TZ=Europe/Lisbon
UID=1000
GID=1000
```

### 🐳 **Instalação com Docker**
```bash
# 1. Clonar o repositório
git clone https://github.com/jpedrodias/class_photo_booth.git
cd class_photo_booth

# 2. Configurar .env
# Criar .env baseado no exemplo abaixo
# Editar .env com suas configurações

# 3. Construir e executar
docker-compose up -d

# 4. Aceder à aplicação
# http://localhost (ou porta configurada)
```

### 🔧 **Primeiro Acesso**
1. Aceder à aplicação no navegador
2. Fazer login com o utilizador `admin@example.com` e a password `ChangeMe1#`
3. Alterar a password do utilizador administrador
4. Configurar email de verificação
5. Importar dados via CSV (opcional)
6. Começar a usar!

## 📚 Documentação Completa

Para documentação técnica detalhada, consulte o arquivo [`SPECIFICATIONS.md`](SPECIFICATIONS.md) que inclui:
- Arquitetura completa do sistema
- Modelos de base de dados
- Fluxos de utilizador
- Considerações de segurança
- Guias de deployment

## 🤝 Contribuições

Contribuições são bem-vindas! Para contribuir:

1. Faça fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE) - veja o arquivo LICENSE para detalhes.

## 📞 Suporte

Para dúvidas, sugestões ou problemas:
- 📧 Email: jpedrodias@gmail.com
- 🐛 Issues: [GitHub Issues](https://github.com/jpedrodias/class_photo_booth/issues)
- 📖 Documentação: [SPECIFICATIONS.md](SPECIFICATIONS.md)

---

**Class Photo Booth v4.1** - Desenvolvido com ❤️ para facilitar a gestão de fotografias escolares
```

# Class-Photo-Booth
O objetivo da aplicação **Class Photo Booth** é permitir a captura de fotografias de alunos por turma. A aplicação facilita a gestão, visualização e exportação das fotografias de forma organizada.

## 📋 Funcionalidades

```
📸 CLASS PHOTO BOOTH v4.1
Sistema Completo de Gestão de Fotografias Escolares

  🔐 SISTEMA DE AUTENTICAÇÃO COMPLETO
  ├─ 📧 Registo com verificação por email
  ├─ 🔑 Login seguro com proteção anti-brute force
  ├─ 🔄 Recuperação de password via email
  ├─ 👥 Sistema de roles (none/viewer/editor/admin)
  ├─ 🛡️ Bloqueio automático de IPs suspeitos
  ├─ 📊 Auditoria completa de acessos
  └─ ⚡ Primeiro utilizador promovido automaticamente a admin

  👤 GESTÃO AVANÇADA DE UTILIZADORES
  ├─ ➕ Criação de contas com validação de email
  ├─ ✏️ Edição de dados e permissões
  ├─ 🔑 Reset de passwords por administradores
  ├─ � Gestão de roles e permissões hierárquicas
  ├─ 📋 Tabela administrativa completa
  ├─ ✅ Aprovação manual de novos utilizadores
  └─ 🔒 Controlo granular de acesso por funcionalidade

  �🏠 GESTÃO DE TURMAS (Admin)
  ├─ ✅ Criação e edição de turmas com nomes seguros
  ├─ 📋 Listagem com estatísticas visuais
  ├─ 🗑️ Eliminação em cascata com limpeza de ficheiros
  ├─ 📊 Estatísticas: alunos totais vs fotos tiradas
  ├─ ✨ Indicador visual de turmas completas
  └─ 🔄 Renomeação automática com movimentação de fotos

  👥 GESTÃO DE ALUNOS (Editor+)
  ├─ ➕ Adicionar alunos com processo único global
  ├─ ✏️ Editar dados com validação completa
  ├─ 🔄 Transferir alunos entre turmas (com fotos)
  ├─ 🗑️ Remover alunos com limpeza de ficheiros
  ├─ 📁 Upload em massa via CSV (substituição/merge)
  ├─ 🔢 Validação de processo (apenas números únicos)
  ├─ 🖼️ Remoção individual de fotografias
  ├─ 🔄 Sincronização automática com base de dados
  ├─ 📝 Renomeação automática de arquivos ao alterar processo
  ├─ 🛡️ Gestão robusta de erros com rollback automático
  └─ 📊 Controlo duplo de estado (foto_existe + foto_tirada)

  📸 CAPTURA DE FOTOGRAFIAS (Editor+)
  ├─ 📷 Interface avançada com múltiplas câmaras
  ├─ 👀 Pré-visualização em tempo real
  ├─ 🎯 Captura com clique, ENTER ou toque
  ├─ 🔄 Recaptura ilimitada até satisfação
  ├─ 🖼️ Geração automática de thumbnails (250x250px)
  ├─ 💾 Armazenamento seguro com nomes sanitizados
  ├─ 📱 Interface otimizada para dispositivos móveis
  ├─ 🎨 Drag & Drop direto no cartão do aluno
  └─ 🔄 Atualização dinâmica de contadores e estado

  📥 DOWNLOADS MÚLTIPLOS (Viewer+)
  ├─ 📦 ZIP Fotos Originais (alta resolução por turma)
  ├─ 🖼️ ZIP Thumbnails (otimizado, tamanho reduzido)
  ├─ 📄 Documento DOCX profissional por turma
  ├─ 💾 Download individual por aluno
  └─ 🚀 Geração dinâmica com nomes de ficheiro seguros

  📝 GERAÇÃO DE DOCUMENTOS WORD
  ├─ 📄 Templates DOCX editáveis e profissionais
  ├─ 🖼️ Inserção automática de fotos redimensionadas
  ├─ 📊 Layout em tabelas organizadas com formatação
  ├─ 🎨 Formatação automática com estilos consistentes
  ├─ 📏 Redimensionamento inteligente de imagens
  └─ 🖼️ Uso de thumbnails para performance otimizada

  📱 INTERFACE RESPONSIVA E UX
  ├─ 💻 Layout desktop otimizado
  ├─ 📱 Interface mobile-first touch-friendly
  ├─ 🎛️ Barras de ação contextuais por role
  ├─ 📋 Modais para todas as operações CRUD
  ├─ 🎨 Feedback visual em tempo real
  ├─ ♿ Acessibilidade e usabilidade otimizada
  ├─ 🌈 Design glassmorphism moderno
  ├─ 🎯 Navegação contextual inteligente
  ├─ 🎨 Destaque visual durante drag-and-drop
  ├─ 📊 Barras de progresso com estatísticas dinâmicas
  └─ 🔄 Scroll preservation entre operações

  ⚙️  CONFIGURAÇÕES E ADMINISTRAÇÃO (Admin)
  ├─ 🔧 Painel de configurações centralizadas
  ├─ � Gestão completa de utilizadores e roles
  ├─ 📁 Upload CSV com validação avançada
  ├─ 🔄 Reset completo (nuke) de dados e ficheiros
  ├─ 📊 Estatísticas globais do sistema
  ├─ 📧 Configuração de email para autenticação
  └─ 🛡️ Gestão de segurança e IPs banidos

  📧 SISTEMA DE EMAIL INTEGRADO
  ├─ 📨 Templates HTML responsivos personalizados
  ├─ ✅ Verificação de email no registo
  ├─ 🔑 Recuperação de password com códigos seguros
  ├─ 🎨 Design consistente com branding da aplicação
  ├─ ⏰ Códigos com expiração automática (24h)
  ├─ 🔧 Configuração flexível de servidores SMTP
  └─ ❌ Gestão de erros com fallback apropriado

  🐳 DEPLOYMENT PROFISSIONAL
  ├─ 🐳 Containerização Docker completa
  ├─ 📂 Mapeamento de volumes para persistência
  ├─ 🔧 Variáveis de ambiente configuráveis
  ├─ 👤 UID/GID dinâmico para permissões
  ├─ 🚀 Deploy produção-ready
  ├─ 📋 Logs e monitorização avançada
  ├─ 🔄 Scripts de inicialização automatizados
  ├─ 💾 Base de dados SQLite com SQLAlchemy ORM
  ├─ 🔧 Configuração flexível dev/prod
  └─ 🛡️ Gestão segura de permissões e volumes

  📋 ESPECIFICAÇÕES TÉCNICAS

  Backend:      Python 3.12 + Flask + SQLAlchemy + Flask-Mail
  Frontend:     HTML5 + CSS3 + Bootstrap 5 + JavaScript ES6+
  Base Dados:   SQLite com ORM e modelos relacionais avançados
  Autenticação: Sistema completo com roles e anti-brute force
  Email:        Flask-Mail com templates HTML responsivos
  Imagens:      OpenCV + Pillow (PIL) + processamento avançado
  Documentos:   python-docx com templates profissionais
  Segurança:    Werkzeug Security + validação + sanitização
  Deploy:       Docker + docker-compose + UID/GID dinâmico

  🎯 CASOS DE USO

  🏫 Escolas:         Sistema completo com controlo de acesso multi-utilizador
  👨‍🏫 Professores:     Captura e visualização com permissões granulares
  👤 Editores:        Gestão de alunos e captura de fotografias
  🔧 Administradores: Controlo total de utilizadores, turmas e sistema
  📸 Fotógrafos:      Interface profissional para sessões organizadas
  🏢 Organizações:    Documentação digital com roles e auditoria
  📋 Secretarias:     Relatórios profissionais e gestão administrativa
  🛡️ IT/Segurança:    Sistema robusto com autenticação e logging completo

💡 Class Photo Booth - Solução empresarial completa para fotografias escolares
🔐 Multi-user • 📱 Mobile-ready • 🚀 Production-ready • 🛡️ Enterprise-grade

## 🆕 Melhorias Recentes (v4.1)

### 🔄 **Renomeação Automática de Arquivos**
- Quando o processo de um aluno é alterado, todas as fotos são automaticamente renomeadas
- Mantém consistência entre base de dados e sistema de ficheiros
- Gestão robusta de erros com rollback automático em caso de falha

### 📊 **Controlo de Estado Avançado**
- Duplo controlo com flags `foto_existe` e `foto_tirada`
- Sincronização precisa entre base de dados e ficheiros
- Estatísticas dinâmicas em tempo real

### 🎨 **Interface Aprimorada**
- Drag & Drop direto nos cartões dos alunos
- Destaque visual durante operações de arraste
- Preservação de scroll entre operações
- Barras de progresso com estatísticas atualizadas

### 🛡️ **Robustez e Segurança**
- Sistema de rollback automático em operações críticas
- Validação aprimorada de dados e integridade
- Gestão de erros com feedback específico ao utilizador

## 🚀 Instalação e Configuração

### 📋 **Pré-requisitos**
- Docker & Docker Compose
- Arquivo `.env` configurado (veja exemplo abaixo)

### ⚙️ **Configuração do .env**
```env
# Configurações da aplicação
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
2. Criar primeira conta (será automaticamente admin)
3. Configurar email de verificação
4. Importar dados via CSV (opcional)
5. Começar a usar!

## 📚 Documentação Completa

Para documentação técnica detalhada, consulte o arquivo [`SPECIFICATION.md`](SPECIFICATION.md) que inclui:
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
- 📖 Documentação: [SPECIFICATION.md](SPECIFICATION.md)

---

**Class Photo Booth v4.1** - Desenvolvido com ❤️ para facilitar a gestão de fotografias escolares
```

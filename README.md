# Class-Photo-Booth
O objetivo da aplicação **Class Photo Booth** é permitir a captura de fotografias de alunos por turma. A aplicação facilita a gestão, visualização e exportação das fotografias de forma organizada.

## 📋 Funcionalidades

```
📸 CLASS PHOTO BOOTH v0.4
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
  └─ 🔄 Sincronização automática com base de dados

  📸 CAPTURA DE FOTOGRAFIAS (Editor+)
  ├─ 📷 Interface avançada com múltiplas câmaras
  ├─ 👀 Pré-visualização em tempo real
  ├─ 🎯 Captura com clique, ENTER ou toque
  ├─ 🔄 Recaptura ilimitada até satisfação
  ├─ 🖼️ Geração automática de thumbnails (250x250px)
  ├─ 💾 Armazenamento seguro com nomes sanitizados
  └─ 📱 Interface otimizada para dispositivos móveis

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
  └─ 🎯 Navegação contextual inteligente

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
  └─ 💾 Base de dados SQLite com SQLAlchemy ORM

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
```

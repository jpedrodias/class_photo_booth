# � Alterações Recentes (v5.0)

- **Sessões Flask migradas para Redis (RAM-only)**: Utiliza Flask-Session com backend Redis, configurado para não persistir dados em disco (apenas memória).
- **Serialização das sessões com msgpack**: Maior compatibilidade e performance.
- **Configuração por variáveis de ambiente (.env)**: Email, Redis, debug, etc. agora configuráveis por .env.
- **Painéis de monitorização Redis**: Novos painéis em `settings.html` para monitorizar estado do Redis e sessões, com auto-refresh e debug.
- **Logout robusto**: Remove explicitamente a sessão do Redis.
- **Limpeza manual/automática de sessões**: Rotas administrativas para listar e limpar sessões expiradas ou inválidas.
- **Função JS para mostrar/ocultar senha**: Melhor usabilidade nos modais de alteração de password.
- **Exposição de erros para debugging**: Blocos try removidos em pontos críticos para facilitar debugging.
- **Atualização de requirements.txt**: Adicionado `msgpack` como dependência.

- **Funcionalidade PWA (Progressive Web App)**: Todas as páginas principais podem ser adicionadas à tela principal do telemóvel, exibindo ícone personalizado e nome, proporcionando experiência mobile otimizada.

# �📸 Especificação Técnica Completa – Class Photo Booth v5.0

## 1. Introdução

### 1.1 Objetivo
O **Class Photo Booth** é uma aplicação web moderna e responsiva desenvolvida para facilitar a captura, gestão e organização de fotografias de alunos por turma. A aplicação utiliza uma arquitetura completa com sistema de autenticação avançado, gestão de utilizadores com roles e permissões, sistema de email, base de dados SQLAlchemy, proteção CSRF, sistema de autorização para fotografias e oferece uma interface intuitiva otimizada para dispositivos móveis e desktop com funcionalidades avançadas de CRUD e geração de documentos.

### 1.2 Escopo
A aplicação é uma solução web empresarial completa, desenvolvida em **Python com Flask**, com as seguintes capacidades:

- **Sistema de autenticação completo** com registo, verificação por email, recuperação de password
- **Sistema de roles e permissões** (none, viewer, editor, admin) com hierarquia de acesso
- **Gestão de utilizadores** com interface administrativa completa
- **Sistema de email** com templates HTML para verificação e recuperação de password
- **Proteção anti-brute force** com bloqueio de IPs por tentativas excessivas
- **Proteção CSRF** com Flask-WTF em todos os formulários
- **Base de dados SQLAlchemy** com modelos relacionais complexos (SQLite/PostgreSQL)
- **Sistema de autorização para fotografias** com controlo visual por cores
- **Gestão de emails** para professores e alunos com importação via CSV
- **Gestão completa de turmas e alunos** via interface web e upload CSV
- **Sistema CRUD completo** para turmas, alunos e utilizadores
- **Timestamps de última atualização** para rastreamento de alterações por turma
- **Interface responsiva** otimizada para dispositivos móveis
- **Captura de fotografias** com suporte a múltiplas câmaras
- **Upload manual de fotos** com drag-and-drop diretamente nos cartões dos alunos
- **Sistema visual de status** com badges coloridos conforme autorização
- **Processamento avançado** de imagens com PIL e OpenCV
- **Download múltiplo** (ZIP e DOCX) das fotografias por turma
- **Geração de documentos Word** com layout profissional
- **Deployment via Docker** com mapeamento de permissões
- **Sistema de logging** com rastreamento de tentativas de login
- **Scripts de migração** para atualizações da base de dados

### 1.3 Público-Alvo
O sistema destina-se a:
- **Operadores de fotografia escolar** com diferentes níveis de acesso
- **Professores e auxiliares** com permissões de visualização e captura
- **Editores de conteúdo** com capacidades de gestão de alunos e turmas
- **Administradores escolares** com acesso completo ao sistema
- **Secretarias escolares** para gestão de turmas e utilizadores
- **Qualquer organização** que necessite de documentação fotográfica estruturada com controlo de acesso

### 1.4 Tecnologias Implementadas
- **Backend**: Python 3.12, Flask, SQLAlchemy, Flask-Mail, Flask-WTF, OpenCV, Pillow (PIL), python-docx, Werkzeug Security
- **Base de Dados**: SQLite com SQLAlchemy ORM e modelos relacionais avançados (compatibilidade PostgreSQL)
- **Frontend**: HTML5, CSS3 (Bootstrap 5), JavaScript ES6+ com interfaces modais e drag-and-drop
- **Autenticação**: Sistema completo with hash de passwords, verificação por email, recuperação de password
- **Segurança**: Proteção CSRF, anti-brute force, validação de inputs, sanitização de dados
- **Email**: Flask-Mail com templates HTML responsivos
- **Containerização**: Docker & Docker Compose com mapeamento de permissões
- **Geração de Documentos**: python-docx para relatórios em Word profissionais
- **Design**: Mobile-first, responsivo, glassmorphism com sistema visual de status por cores

## 2. Arquitetura e Deployment

### 2.1 Estrutura de Deployment
```
├── docker-compose.yml      # Orquestração de containers
├── Dockerfile             # Imagem da aplicação
├── start.sh               # Script de inicialização com UID/GID
├── .env                   # Configurações de ambiente
├── .gitignore             # Controlo de versionamento
└── flaskapp/             # Código da aplicação
    ├── app.py            # Backend Flask com SQLAlchemy e autenticação
    ├── config.py         # Configurações da aplicação (Dev/Prod)
    ├── requirements.txt  # Dependências Python
    ├── database.sqlite   # Base de dados SQLite
    ├── session_files/    # Ficheiros de sessão Flask
    ├── templates/        # Templates HTML
    │   ├── login.html    # Interface de autenticação completa
    │   ├── home.html     # Página inicial personalizada por role
    │   ├── turmas.html   # Listagem de turmas
    │   ├── turma.html    # Gestão de alunos por turma
    │   ├── settings.html # Configurações e gestão de utilizadores
    │   ├── capture_photo.html # Interface de captura
    │   ├── template_email_send_verification.html # Email de verificação
    │   └── template_email_send_password_reset.html # Email de recuperação
    ├── static/          # Assets estáticos
    │   ├── favicon.ico
    │   ├── student_icon.jpg
    │   └── styles.css   # Estilos personalizados
    ├── docx_templates/  # Templates para documentos Word
    ├── photos_originals/ # Fotografias originais organizadas por turma
    ├── photos_thumbs/   # Miniaturas (250x250) organizadas por turma
    └── zips/            # Arquivos temporários para downloads
```

### 2.2 Base de Dados
- **SQLAlchemy ORM**: Gestão de dados com modelos Python complexos e relacionamentos
- **SQLite**: Base de dados embebida para simplicidade e portabilidade
- **Modelos Implementados**:
  - **User**: Utilizadores do sistema com autenticação e roles
  - **PreUser**: Utilizadores em processo de verificação por email
  - **LoginLog**: Logs de tentativas de login para segurança
  - **BannedIPs**: Sistema anti-brute force com bloqueio de IPs
  - **Turma**: Classes/turmas com nomes seguros para filesystem
  - **Aluno**: Estudantes com relacionamento para turmas
- **Constraints**: Unicidade global de processo (único em toda a aplicação)
- **Validação de Processo**: Apenas números inteiros positivos (NIF, número de estudante, etc.)
- **Relacionamentos**: One-to-Many entre Turma-Aluno e User-LoginLog
- **Migrations**: Criação automática de tabelas e índices
- **Segurança**: Hashing de passwords com Werkzeug, validação de emails

### 2.3 Mapeamento de Permissões
- **UID/GID dinâmico**: Container usa o mesmo UID/GID do host
- **Volumes persistentes**: Dados e base de dados mantidos entre reinicializações
- **Permissões automáticas**: Criação segura de diretórios

## 3. Sistema de Autenticação e Autorização

### 3.1 Arquitetura de Autenticação
- **Registo com verificação por email**: Sistema completo de criação de contas
- **Login seguro**: Validação de credenciais com proteção anti-brute force
- **Recuperação de password**: Sistema de reset via email com códigos temporários
- **Gestão de sessões**: Controlo de duração baseado em "remember me"
- **Logout seguro**: Limpeza completa da sessão
- **Primeiro utilizador**: Automaticamente promovido a administrador
Gerir alunos (CRUD)         |  ❌  |   ❌   |   ✅   |   ✅  |
Gerir turmas (CRUD)         |  ❌  |   ❌   |   ❌   |   ✅  |
# Especificações Técnicas — Class Photo Booth v5.0

Este documento serve como referência técnica. Contém a arquitetura, modelos de dados, permissões e fluxos principais.

Sumário rápido:

- Arquitetura: Flask + SQLAlchemy + Redis (sessions) + Docker
- Modelos: User, PreUser, LoginLog, BannedIPs, Turma, Aluno
- Autenticação: email verification, password reset, roles (none/viewer/editor/admin)
- Upload CSV: modos replace/merge, validação de processos (únicos e numéricos)
- Downloads: ZIP (originais/thumbs) e DOCX gerados dinamicamente

Para guias de instalação e deployment veja `INSTALL.md`.

## 1. Arquitetura geral

- Backend: Python 3.12, Flask
- ORM: SQLAlchemy (compatível com SQLite e PostgreSQL)
- Sessões: Flask-Session com backend Redis (in-memory)
- Processamento de imagens: OpenCV e Pillow (PIL)
- Geração de documentos: python-docx
- Containerização: Docker + Docker Compose

## 2. Modelos de dados (resumo)

- User: id, username (email), password_hash, name, role, is_verified
- PreUser: email, code, date (codes temporários para verificação/reset)
- LoginLog: date, success, remote_addr, user_id
- BannedIPs: remote_addr, date (para anti-brute-force)
- Turma: id, nome, nome_seguro, nome_professor, email_professor, last_updated
- Aluno: id, processo (único global), nome, numero, email, autorizacao, foto_existe, foto_tirada, turma_id

Notas:

- `Aluno.processo` é único em toda a aplicação (controle por import/CRUD).
- `Turma.nome_seguro` é sanitizado para uso em filesystem (criado com secure_filename).

## 3. Autenticação e autorização

- Registo por email com código de 6 caracteres.
- Recuperação de senha por código.
- Primeiro utilizador criado é promovido a `admin`.
- Hierarquia de roles: none < viewer < editor < admin.

Funções utilitárias presentes no código:

- `get_current_user()` — lê sessão e valida expirations/sliding session
- Decoradores: `required_login`, `required_role(min_role)`, `required_permission(permission)`

## 4. Importação CSV

- Formato esperado (mínimo): `turma,processo,nome` (campo `numero` opcional).
- Validação: `processo` deve ser inteiro positivo; duplicados no CSV são rejeitados.
- Operações: `replace` (substitui toda a DB de turmas/alunos) e `merge` (atualiza/insere mantendo dados existentes).
- Fotos existentes são movidas automaticamente para a turma indicada quando necessário.

## 5. Upload / Captura de imagens

- Upload via API `/upload/photo/<nome_seguro>/<processo>` aceita imagem em base64.
- Upload manual via formulário com verificação de extensão.
- Processamento: crop central + geração de thumbnail 250x250.

## 6. Admin / Redis / Sessões

- Painel em `/settings` para listar sessões Redis, limpar sessões inválidas e inspecionar tráfego.
- Serialização: `msgpack` é tentado; fallback para `pickle` e JSON.

## 7. Boas práticas de deployment

- Desativar `DEBUG` em produção.
- Executar com Gunicorn e configurar `NUM_WORKERS` conforme CPUs.
- Proteger serviços com proxy reverso (nginx) e TLS.

---

Se quiser, posso adicionar diagramas (ERD), exemplos de `docker-compose.yml` ou um resumo das rotas API mais relevantes.
- **Modais CRUD**: Criar, editar, reset password para utilizadores
- **Limpeza de dados**: Função nuke com senha de administrador
- **Estados adaptativos**: Interface baseada na existência de dados e permissões

### 6.3 Gestão de Utilizadores (Interface Administrativa)
#### 6.3.1 Tabela de Utilizadores
- **Avatar personalizado**: Iniciais do nome em círculo colorido
- **Informações detalhadas**: Nome, email, role, status de verificação
- **Badges de role**: Cores distintas para cada nível de permissão
- **Indicador "Você"**: Destaque para conta do utilizador atual
- **Ações por linha**: Editar e reset password por utilizador

#### 6.3.2 Modais de Gestão
- **Adicionar utilizador**: Formulário completo com nome, email e role
- **Editar utilizador**: Modificação de dados existentes
- **Reset password**: Modal específico com avisos de segurança
- **Validação em tempo real**: Feedback imediato de erros
- **Confirmações**: Diálogos para ações críticas

### 6.4 Sistema de Captura (Editor+)
- **Interface dedicada**: Página específica para captura de fotos
- **Seleção de câmara**: Dropdown com dispositivos disponíveis
- **Memória persistente**: localStorage para lembrar câmara escolhida
- **Preview em tempo real**: Stream de vídeo ao vivo
- **Controles por teclado**: Enter (capturar) / Escape (voltar)
- **Atualização automática**: Flag foto_tirada na base de dados

## 7. Sistema de Email e Comunicação

### 7.1 Templates de Email
- **Verificação de conta**: `template_email_send_verification.html`
  - Design responsivo com identidade visual da aplicação
  - Link de verificação com token seguro
  - Instruções claras para ativação da conta
- **Recuperação de password**: `template_email_send_password_reset.html`
  - Template para reset de password com link temporário
  - Design consistente com template de verificação
  - Instruções de segurança

### 7.2 Gestão de Campos Email
- **Professors**: Campo `email_professor` em Turma para comunicação direta
- **Alunos**: Campo `email` opcional para comunicação sobre autorizações
- **Integração CSV**: Suporte a import de emails através de ficheiro CSV
- **Comunicação automática**: Potencial para notificações sobre estado de autorizações

## 8. Sistema de Captura e Processamento de Imagens

### 8.1 Interface de Captura (`/capture_photo/<nome_seguro>/<processo>`)
- **Controlo de acesso**: Apenas editores e administradores
- **Seleção de câmara**: Dropdown com dispositivos disponíveis
- **Memória persistente**: localStorage para lembrar câmara escolhida
- **Preview em tempo real**: Stream de vídeo ao vivo
- **Controles por teclado**: Enter (capturar) / Escape (voltar)
- **Atualização automática**: Flag foto_tirada na base de dados

### 8.2 Processamento Avançado de Imagens
- **Captura original**: Resolução máxima da câmara
- **Processamento PIL**: Redimensionamento e crop inteligente
- **Thumbnails otimizadas**: 250x250px com crop central
- **Qualidade diferenciada**: 95% originais, 50% thumbnails
- **Formato consistente**: JPEG em ambos os tamanhos

### 8.3 Armazenamento Organizado por Turma
```
photos_originals/
├── turma_segura_1/
│   ├── 3035.jpg          # Processo do aluno
│   └── 3999.jpg
└── turma_segura_2/
    └── 4763.jpg

photos_thumbs/
├── turma_segura_1/
│   ├── 3035.jpg          # Thumbnail 250x250
│   └── 3999.jpg
└── turma_segura_2/
    └── 4763.jpg
```

## 9. Sistema de Download Avançado

### 9.1 Download ZIP (`/download/<turma>.zip`)
- **Controlo de acesso**: Viewers e superiores podem fazer download
- **Criação em memória**: Sem ficheiros temporários
- **Compressão otimizada**: ZIP standard
- **Nome descritivo**: `{turma}.zip`
- **Verificação de conteúdo**: Alerta se não há fotos
- **Fotos originais**: Qualidade máxima para arquivo

### 9.2 Geração de Documentos DOCX (`/download/<turma>.docx`)
- **Templates Word**: Uso de templates `.docx` profissionais
- **Layout inteligente**: Grid 4 colunas adaptativo baseado no número de alunos
- **Substituição de placeholders**: Data, turma, professor
- **Processamento de imagens**: Redimensionamento e crop para documentos
- **Inclusão total**: Todos os alunos (com foto ou placeholder)
- **Qualidade otimizada**: 150 DPI para impressão
- **Metadados**: Autor, título e propriedades do documento

### 9.3 Processamento de Imagens para DOCX
- **PIL avançado**: Redimensionamento proporcional
- **Crop central**: Manutenção da proporção original
- **Fallback inteligente**: Placeholder para alunos sem foto
- **Otimização de tamanho**: Baseado no número total de alunos
- **Uso de thumbnails**: Performance otimizada

### 9.4 Interface de Download
- **Dropdown Bootstrap**: Seleção de formato (ZIP/DOCX)
- **Versões mobile e desktop**: Interfaces adaptadas
- **Feedback visual**: Estados de loading
- **Detecção de conteúdo**: Desativa se não há dados
- **Controlo de permissões**: Baseado no role do utilizador

## 10. Funcionalidades Avançadas

### 10.1 Sistema de Placeholders e Drag & Drop
- **Ícone padrão**: `student_icon.jpg` para alunos sem foto
- **Integração completa**: Suporte em thumbnails e documentos
- **Consistência visual**: Mesmo estilo para todos os estados
- **Cursor uniforme**: Pointer em todos os cartões de aluno
- **Drag & Drop**: Suporte a arrastar ficheiros de imagem diretamente para o cartão do aluno, com feedback visual e integração total ao fluxo de upload manual

### 10.2 Gestão de Estados
- **Flags de controlo**: `foto_existe` (existência do ficheiro) e `foto_tirada` (estado de captura)
- **Ordenação inteligente**: Por número (nulls last) depois por nome
- **Contagens dinâmicas**: Estatísticas em tempo real
- **Sincronização**: Base de dados e sistema de ficheiros
- **Renomeação consistente**: Manutenção da integridade entre nomes de processos e nomes de arquivos

### 10.3 Movimentação e Gestão de Arquivos
- **Transferência de alunos**: Move fotos entre turmas
- **Renomeação de turmas**: Reorganiza estrutura de pastas
- **Renomeação de processos**: Quando o processo de um aluno é alterado, arquivos de foto são automaticamente renomeados para manter consistência
- **Validação de integridade**: Verificação de existência de arquivos
- **Gestão de erros**: Rollback automático em caso de falha na renomeação
- **Limpeza automática**: Remove arquivos órfãos

### 10.4 Templates DOCX
```
docx_templates/
└── template_relacao_alunos_fotos.docx    # Template base para relatórios
```
- **Placeholders dinâmicos**: `{turma}`, `{date}`, `{fullname_dt}`
- **Formatação profissional**: Layout padronizado
- **Tabelas responsivas**: Ajuste automático de colunas
- **Headers e footers**: Suporte completo a cabeçalhos

## 11. Requisitos Técnicos

### 11.1 Sistema Base
- **Python 3.12+**: Linguagem principal
- **Docker & Docker Compose**: Containerização
- **Sistema operativo**: Linux, Windows, macOS
- **Navegador moderno**: Chrome 90+, Firefox 90+, Safari 14+

### 11.2 Dependências Python
```txt
Flask                     # Framework web principal
Flask-SQLAlchemy          # ORM para base de dados
Flask-Mail                # Sistema de email
Flask-Session             # Backend de sessões (Redis)
redis                     # Cliente Redis
msgpack                   # Serialização eficiente de sessões
opencv-python             # Processamento de imagens
python-docx               # Geração de documentos Word
Pillow                    # Manipulação avançada de imagens
```

### 11.3 Configuração de Ambiente
```env
# Configurações da aplicação
FLASKAPP_DEBUG=True                          # Modo debug (dev/prod)
FLASKAPP_SECRET_KEY=supersecretkey           # Chave para sessões Flask
DATABASE_URL=sqlite:///alunos.db             # URL da base de dados
FLASKAPP_PORT=80                             # Porta de exposição

# Configurações de email
MAIL_SERVER=smtp.office365.com               # Servidor SMTP
MAIL_PORT=587                                # Porta SMTP
MAIL_USE_TLS=True                            # TLS
MAIL_USE_SSL=False                           # SSL
MAIL_USERNAME=seuemail@outlook.com           # Email para envio
MAIL_PASSWORD=suapassword                    # Password do email
MAIL_SENDER=Class Photo Booth <seuemail@outlook.com>  # Remetente
# Configurações Redis
REDIS_HOST=redis                             # Host Redis (container)
REDIS_PORT=6379                              # Porta Redis
REDIS_DB=0                                   # DB Redis
SESSION_TYPE=redis                           # Backend de sessões
SESSION_KEY_PREFIX=session:                  # Prefixo das sessões
SESSION_SERIALIZATION_FORMAT=msgpack         # Formato de serialização

# Configurações Docker
TZ=Europe/Lisbon                             # Timezone
UID=1000                                     # User ID (auto-configurado)
GID=1000                                     # Group ID (auto-configurado)
```

## 12. Fluxos de Utilizador Completos

### 12.1 Primeiro Acesso e Configuração Inicial
1. **Navegador** → `http://localhost` → Página de login
2. **Primeiro administrador**:
   - Clica "Criar nova conta"
   - Insere email válido → Sistema envia código por email
   - Recebe email com código de verificação
   - Completa registo com nome, password segura e código
   - Sistema atribui automaticamente role "admin"
   - Login automático → Redirecionamento para `/turmas` (vazia)
3. **Upload inicial de dados**:
   - Acede a `/settings` → Upload CSV
   - Escolhe modo (substituir/merge) → Importação
   - Dados importados → Redirecionamento para `/turmas`

### 12.2 Gestão de Utilizadores (Admin)
1. **Criar novos utilizadores**:
   - `/settings` → "Adicionar Utilizador" 
   - Modal com nome, email, role inicial
   - Sistema envia email de verificação ao novo utilizador
   - Novo utilizador segue fluxo de verificação
2. **Gerir utilizadores existentes**:
   - Editar informações (nome, email, role)
   - Reset password para utilizadores
   - Aprovação de contas (alterar de 'none' para role ativo)

### 12.3 Registo de Novos Utilizadores
1. **Auto-registo**:
   - Página login → "Criar nova conta"
   - Insere email → Recebe código por email
   - Completa verificação com nome e password
   - Conta criada com role 'none' (aguarda aprovação)
2. **Aguardar aprovação**:
   - Login → Página inicial com mensagem de aguardar validação
   - Administrador aprova alterando role para viewer/editor/admin

### 12.4 Gestão de Turmas (Admin)
1. **Visualização** → Cards com estatísticas e ações
2. **Nova turma** → Modal com formulário de criação
3. **Editar turma** → Renomeação com validação e movimentação de fotos
4. **Remover turma** → Confirmação e limpeza completa de arquivos

### 12.5 Gestão de Alunos (Editor+)
1. **Selecionar turma** → Visualização da pauta completa
2. **Adicionar aluno** → Modal com processo, nome e número
3. **Editar aluno** → Modificação de dados com validação
4. **Transferir aluno** → Seleção de turma destino com movimentação de fotos
5. **Remover elementos** → Aluno completo ou apenas foto

### 12.6 Captura e Download
1. **Captura (Editor+)** → Seleção de aluno → Escolha de câmara → Foto
2. **Preview automático** → Thumbnail gerada e exibida
3. **Download (Viewer+)** → Dropdown com opções ZIP/DOCX
4. **Documentos** → ZIP com fotos originais ou DOCX formatado

### 12.7 Recuperação de Password
1. **Login** → "Esqueci-me da password"
2. **Inserir email** → Sistema envia código de recuperação
3. **Email recebido** → "Já tenho código de recuperação"
4. **Inserir código e nova password** → Password alterada com sucesso

## 13. Considerações de Segurança

### 13.1 Autenticação Multi-Camada
- **Hashing de passwords**: Werkzeug Security com salt automático
- **Validação de email**: Regex pattern matching para formato
- **Força de password**: Mínimo 6 caracteres com maiúsculas, minúsculas e números
- **Sessões seguras**: Flask sessions com chaves secretas
- **Timeout controlado**: Sessões de 2h (normal) ou 30 dias (remember me)
- **Verificação por email**: Códigos de 6 caracteres com expiração de 24h

### 13.2 Proteção Anti-Brute Force
- **Tracking de tentativas**: Todas as tentativas registadas em LoginLog
- **Limite de tentativas**: Máximo 5 tentativas falhadas por IP em 15 minutos
- **Bloqueio automático**: IPs maliciosos banidos automaticamente
- **Tabela de IPs banidos**: Gestão persistente de bloqueios
- **Logging detalhado**: IP, utilizador, timestamp, resultado para auditoria

### 13.3 Validação de Dados
- **Entrada sanitizada**: Validação rigorosa de todos os formulários
- **Prevenção SQL Injection**: SQLAlchemy ORM com queries parametrizadas
- **Sanitização de filesystem**: secure_filename() para nomes de turmas
- **Validação de processo**: Apenas números inteiros positivos aceites
- **Unicidade garantida**: Constraints na base de dados para emails e processos
- **Tipo de ficheiros**: Apenas CSV e imagens aceites em uploads
- **Limites de tamanho**: Proteção contra uploads excessivos

### 13.4 Gestão Segura de Ficheiros
- **Paths seguros**: safe_join() para prevenção de directory traversal
- **Nomes sanitizados**: Conversão automática de nomes inseguros
- **Permissões controladas**: Acesso restrito aos diretórios da aplicação
- **Validação de existência**: Verificação antes de operações de ficheiro
- **Limpeza automática**: Remoção segura de arquivos órfãos
- **Estrutura de diretórios**: Organização segura por turma

### 13.5 Controlo de Acesso Baseado em Roles
- **Decorators de autorização**: @required_login, @required_permission, @required_role
- **Verificação por endpoint**: Cada rota protegida conforme necessário
- **Interface adaptativa**: UI mostra apenas opções permitidas por role
- **Validação server-side**: Dupla verificação de permissões no backend
- **Auditoria de acesso**: Logging de ações por utilizador e role

## 14. Performance e Otimização

### 14.1 Base de Dados
- **Índices otimizados**: Processo indexado globalmente para consultas rápidas
- **Constraint único**: Unicidade global de processo para integridade de dados
- **Relacionamentos eficientes**: Lazy loading com backref para otimização
- **Transações**: Operações atômicas para consistência
- **Queries otimizadas**: Uso de filtros e joins eficientes
- **Cleanup automático**: Limpeza de registos expirados (PreUser, códigos)

### 14.2 Sistema de Email
- **Envio assíncrono**: Processamento em background para não bloquear UI
- **Templates reutilizáveis**: HTML templates para consistência e performance
- **Fallback handling**: Gestão de erros de envio com feedback apropriado
- **Configuração flexível**: Suporte para diferentes provedores SMTP

### 14.3 Processamento de Imagens
- **Thumbnails inteligentes**: Geração sob demanda com cache em filesystem
- **Compressão otimizada**: Qualidades diferentes para originais vs thumbnails
- **Processamento PIL/OpenCV**: Algoritmos otimizados para redimensionamento
- **Cache de filesystem**: Reutilização de thumbnails existentes

### 14.4 Interface e UX
- **CSS otimizado**: Bootstrap 5 com customizações mínimas
- **JavaScript essencial**: Funcionalidade crítica apenas, sem frameworks pesados
- **Carregamento progressivo**: Imagens e conteúdo carregados sob demanda
- **Cache headers**: Controlo de cache para assets estáticos
- **Modais eficientes**: Reutilização de componentes Bootstrap

## 15. Manutenção e Backup

### 15.1 Estrutura de Dados
- **Base de dados**: `database.sqlite` centralizando metadados
- **Arquivos organizados**: Estrutura de pastas por turma
- **Sincronização**: Coerência entre DB e filesystem
- **Integridade**: Validação automática de consistência
- **Renomeação automática**: Manutenção da consistência entre processos e nomes de arquivos

### 15.2 Operações de Manutenção
- **Limpeza completa**: Função nuke com senha de administrador
- **Backup seletivo**: Exportação de dados por turma
- **Importação flexível**: CSV com merge ou substituição
- **Logs detalhados**: Rastreamento de todas as operações

### 15.3 Deployment e Updates
- **Docker volumes**: Persistência de dados entre atualizações
- **Git integration**: Versionamento com .gitignore adequado
- **Dependency management**: requirements.txt com versões fixas
- **Environment variables**: Configuração flexível via .env

---

**Versão do Documento**: 5.0  
**Data de Atualização**: Janeiro 2025  
**Estado da Implementação**: ✅ 100% Completo

Esta especificação reflete fielmente a aplicação **Class Photo Booth** implementada, incluindo todas as funcionalidades avançadas: sistema completo de autenticação com roles e permissões, gestão de utilizadores, sistema de email com templates HTML, proteção anti-brute force, base de dados SQLAlchemy com modelos relacionais, CRUD completo para todas as entidades, geração de documentos DOCX, processamento avançado de imagens com PIL/OpenCV, gestão de placeholders, interface completamente responsiva com operações modais, sistema de autorização de fotografias com visual status badges, e controlo de acesso granular baseado em roles.

### Funcionalidades Principais Implementadas:
✅ Sistema de autenticação completo com registo, verificação e recuperação  
✅ Gestão de utilizadores com roles (none/viewer/editor/admin)  
✅ Sistema de email com templates HTML responsivos  
✅ Proteção anti-brute force com bloqueio de IPs  
✅ Interface administrativa para gestão de utilizadores  
✅ CRUD completo para turmas, alunos e utilizadores  
✅ Sistema de captura de fotos com controlo de permissões  
✅ Upload manual de foto com suporte a drag-and-drop diretamente no cartão do aluno, preenchendo automaticamente o modal  
✅ Destaque visual do cartão durante drag-and-drop (CSS externo)  
✅ Processamento avançado de imagens (PIL/OpenCV)  
✅ Geração de documentos Word profissionais  
✅ Downloads em ZIP e DOCX  
✅ Renomeação automática de arquivos de foto quando processo do aluno é alterado  
✅ Gestão robusta de erros com rollback automático em operações críticas  
✅ Flags de estado duplas para controlo preciso de fotos (`foto_existe`, `foto_tirada`)  
✅ Interface responsiva mobile-first  
✅ Deployment Docker com mapeamento seguro de permissões  

### Modelos de Base de Dados:
- **User**: Autenticação e autorização
- **PreUser**: Verificações pendentes  
- **LoginLog**: Auditoria de acesso
- **BannedIPs**: Proteção anti-brute force
- **Turma**: Classes com nomes seguros
- **Aluno**: Estudantes com processo único global

### Sistema de Roles:
- **none**: Aguarda aprovação
- **viewer**: Visualização apenas
- **editor**: + Captura e gestão de alunos  
- **admin**: + Gestão completa do sistema
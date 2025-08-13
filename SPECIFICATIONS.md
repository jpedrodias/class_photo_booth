# 📸 Especificação Técnica Completa – Class Photo Booth v5.0

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

### 3.2 Sistema de Roles e Permissões
#### 3.2.1 Hierarquia de Roles
- **none**: Conta criada mas à espera de validação pelo administrador
- **viewer**: Visualização de turmas e fotografias
- **editor**: Visualização + captura de fotos + gestão de alunos
- **admin**: Acesso completo incluindo gestão de turmas, utilizadores e sistema

#### 3.2.2 Matriz de Permissões
```
Funcionalidade               | none | viewer | editor | admin |
----------------------------|------|--------|--------|-------|
Visualizar turmas           |  ❌  |   ✅   |   ✅   |   ✅  |
Visualizar fotografias      |  ❌  |   ✅   |   ✅   |   ✅  |
Capturar fotografias        |  ❌  |   ❌   |   ✅   |   ✅  |
Gerir alunos (CRUD)         |  ❌  |   ❌   |   ✅   |   ✅  |
Gerir turmas (CRUD)         |  ❌  |   ❌   |   ❌   |   ✅  |
Upload CSV                  |  ❌  |   ❌   |   ❌   |   ✅  |
Gestão de utilizadores      |  ❌  |   ❌   |   ❌   |   ✅  |
Limpeza do sistema (nuke)   |  ❌  |   ❌   |   ❌   |   ✅  |
```

### 3.3 Fluxo de Registo e Verificação
1. **Registo inicial**: Utilizador insere email válido
2. **Envio de email**: Sistema envia código de verificação de 6 caracteres
3. **Verificação**: Utilizador insere código, nome completo e password segura
4. **Validação de password**: Mínimo 6 caracteres com maiúsculas, minúsculas e números
5. **Criação de conta**: Primeiro utilizador = admin, restantes = none (à espera de aprovação)
6. **Aprovação**: Administrador pode alterar role de 'none' para 'viewer', 'editor' ou 'admin'

### 3.4 Sistema Anti-Brute Force
- **Tracking de tentativas**: Registo de todas as tentativas de login (sucesso/falha)
- **Limite de tentativas**: Máximo 5 tentativas falhadas em 15 minutos
- **Bloqueio automático**: IPs com tentativas excessivas são automaticamente banidos
- **Tabela BannedIPs**: Gestão persistente de IPs bloqueados
- **Logging detalhado**: Rastreamento de IP, utilizador, timestamp e resultado

### 3.5 Recuperação de Password
- **Solicitação**: Utilizador insere email registado no sistema
- **Código de recuperação**: Sistema envia código de 6 caracteres por email
- **Reset seguro**: Utilizador insere código e define nova password
- **Validação**: Mesmos critérios de segurança da password inicial
- **Expiração**: Códigos válidos por 24 horas apenas

## 4. Sistema de Email e Comunicações

### 4.1 Configuração de Email
- **Servidor SMTP**: Suporte para Office365 (smtp.office365.com:587)
- **Autenticação**: Configuração via variáveis de ambiente
- **Templates HTML**: Emails responsivos com branding consistente
- **Fallback**: Gestão de erros com feedback ao utilizador

### 4.2 Templates de Email Implementados
#### 4.2.1 Verificação de Email (`template_email_send_verification.html`)
- **Propósito**: Confirmar email durante registo
- **Conteúdo**: Código de verificação de 6 caracteres alfanuméricos
- **Design**: HTML responsivo com branding da aplicação
- **Validade**: 24 horas

#### 4.2.2 Recuperação de Password (`template_email_send_password_reset.html`)
- **Propósito**: Reset de password esquecida
- **Conteúdo**: Código de recuperação de 6 caracteres alfanuméricos
- **Instruções**: Passo-a-passo para reset seguro
- **Validade**: 24 horas

### 4.3 Gestão de Códigos
- **Geração**: Algoritmo seguro com letras minúsculas e números
- **Armazenamento**: Tabela PreUser com timestamps
- **Expiração**: Limpeza automática de códigos expirados
- **Unicidade**: Verificação de códigos únicos por email

## 5. Gestão de Dados

### 5.1 Sistema de Base de Dados Avançado
#### 5.1.1 Modelo User (Utilizadores)
- **Campos**: ID, email (único), password_hash, name, role, is_verified
- **Validação**: Email regex, password strength (6+ chars, mixed case, numbers)
- **Segurança**: Hashing com Werkzeug, proteção contra SQL injection
- **Relacionamentos**: One-to-Many com LoginLog
- **Métodos**: has_permission(), check_password(), validação de email/password

#### 5.1.2 Modelo PreUser (Verificações Pendentes)
- **Campos**: ID, email, code, date
- **Propósito**: Armazenar utilizadores em processo de verificação
- **Códigos**: 6 caracteres alfanuméricos gerados aleatoriamente
- **Cleanup**: Limpeza automática de registos expirados (>24h)

#### 5.1.3 Modelo LoginLog (Auditoria)
- **Campos**: ID, date, success, remote_addr (IP), user_id
- **Propósito**: Tracking de tentativas de login para segurança
- **Anti-brute force**: Contagem de tentativas falhadas por IP
- **Estatísticas**: Base para análise de padrões de acesso

#### 5.1.4 Modelo BannedIPs (Segurança)
- **Campos**: ID, date, remote_addr (IP)
- **Propósito**: Bloqueio automático de IPs com comportamento malicioso
- **Gestão**: Métodos is_banned(), ban_ip() para controlo automático

#### 5.1.5 Modelo Turma (Classes)
- **Campos**: ID, nome (display), nome_seguro (filesystem), nome_professor, email_professor, last_updated, relacionamento com alunos
- **Campos de Professor**: nome_professor (string), email_professor (string, opcional)
- **Timestamps**: last_updated automático para rastreamento de alterações
- **Segurança**: Sanitização automática de nomes para filesystem seguro
- **Métodos**: create_directories(), update_nome(), delete_directories(), update_last_modified()
- **Validação**: Unicidade de nome_seguro, gestão de colisões
- **Importação CSV**: Suporte a colunas professor e email_professor/email

#### 5.1.6 Modelo Aluno (Estudantes)
- **Campos**: ID, processo (único global), nome, numero, email, autorizacao, foto_existe, foto_tirada, turma_id
- **Campo Email**: email (string, opcional) para contacto direto com aluno
- **Campo Autorização**: autorizacao (boolean, default True) para controlo de publicação em redes sociais
- **Sistema Visual**: Badge colorido conforme estado de autorização:
  - **Verde (success)**: Foto tirada + autorização concedida
  - **Vermelho (danger)**: Foto tirada + sem autorização
  - **Amarelo (warning)**: Foto não tirada (independente da autorização)
- **Constraints**: Processo único em toda a aplicação (não apenas por turma)
- **Validação**: Processo deve ser número inteiro positivo
- **Relacionamento**: Many-to-One com Turma
- **Gestão de Estados**: Flag `foto_existe` para controlo de existência de ficheiro, `foto_tirada` para controlo de captura
- **Renomeação Automática**: Quando o processo de um aluno é alterado, os arquivos de foto são automaticamente renomeados
- **Importação CSV**: Suporte a coluna email opcional

### 5.2 Upload CSV (RF-CSV)
- **Formato suportado**: `turma,processo,nome,numero` (número opcional)
- **Validação de Processo**: CSV rejeita processos não numéricos e duplicados
- **Unicidade Global**: Processo deve ser único em toda a aplicação
- **Modos de operação**: Substituição completa ou merge de dados
- **Validação automática**: Verificação de extensão .csv
- **Gestão de fotos**: Manutenção e movimentação automática de imagens
- **Interface avançada**: Drag & drop com seleção de modo
- **Permissões**: Apenas administradores podem fazer upload

### 5.3 Sistema de Autorização de Fotografias
- **Campo Booleano**: `autorizado` determina se a foto pode ser usada
- **Interface Visual**: Badges coloridos indicam estado de autorização:
  - **Verde**: Aluno autorizado com foto disponível
  - **Vermelho**: Aluno não autorizado ou sem foto
  - **Amarelo**: Estados transitórios ou pendentes
- **Controlo Manual**: Possibilidade de alterar autorização por aluno
- **Integração com CSV**: Campo email opcional suporta comunicação sobre autorizações
- **Impacto Visual**: Estados refletidos em tempo real na interface

### 5.4 CRUD Completo com Controlo de Acesso
#### 5.3.1 Gestão de Utilizadores (Admin apenas)
- **Criar utilizador**: Formulário modal com validação completa
- **Editar utilizador**: Modificação de nome, email e role
- **Reset password**: Funcionalidade para administradores resetarem passwords
- **Gerir roles**: Alteração de permissões (none/viewer/editor/admin)
- **Validação**: Email único, password strength, roles válidos

#### 5.3.2 Gestão de Turmas (Admin apenas)
- **Criar turma**: Formulário modal com validação e sanitização automática
- **Editar turma**: Renomeação com movimentação automática de fotos
- **Remover turma**: Remoção em cascata com limpeza completa de arquivos
- **Validação**: Verificação de nomes únicos e sanitização para filesystem

#### 5.3.3 Gestão de Alunos (Editor+)
- **Adicionar aluno**: Formulário com processo (apenas números inteiros), nome e número
- **Validação de Processo**: Sistema rejeita processos não numéricos e já existentes globalmente
- **Unicidade Global**: Processo único em toda a aplicação (sugestão: NIF, número de estudante)
- **Editar aluno**: Modificação de dados com validação completa
- **Renomeação Automática de Arquivos**: Quando o processo é alterado, fotos originais e thumbnails são automaticamente renomeadas
- **Transferir aluno**: Movimentação entre turmas com fotos (sem conflito de processo)
- **Remover aluno**: Limpeza completa de dados e arquivos
- **Remover foto**: Manutenção de flags de estado (`foto_existe`, `foto_tirada`)

## 6. Interface Responsiva e UX

### 6.1 Design Mobile-First
- **Viewport otimizado**: Experiência consistente em dispositivos
- **Grid responsivo**: Adaptação automática a diferentes ecrãs
- **Touch-friendly**: Botões adequados para interação táctil
- **Cursor consistente**: Pointer em todos os elementos interativos
- **Navegação contextual**: Breadcrumbs e botões de retorno inteligentes

### 6.2 Páginas Principais

#### 6.2.1 Login Completo (`/login`)
- **Design moderno**: Gradientes e sombras suaves com glassmorphism
- **Múltiplas ações**: Login, registo, verificação, recuperação de password
- **Validação client-side**: Feedback imediato com JavaScript
- **Estados dinâmicos**: Interface adapta conforme ação selecionada
- **Formulários responsivos**: Campos adaptativos por tipo de ação
- **Proteção visual**: Indicadores de segurança e campos obrigatórios

#### 6.2.2 Página Inicial (`/`)
- **Redirecionamento inteligente**: Baseado no role do utilizador
- **Boas-vindas personalizadas**: Mensagem específica por role
- **Utilizadores 'none'**: Página explicativa sobre aguardar aprovação
- **Utilizadores ativos**: Redirecionamento automático para turmas

#### 6.2.3 Listagem de Turmas (`/turmas`)
- **Cards interativos**: Efeitos hover e animações
- **Estatísticas visuais**: Total de alunos e fotos por turma
- **Ações contextuais**: Editar e remover turmas (admin apenas)
- **Status visual**: Indicador de turmas completas
- **Modal para nova turma**: Criação rápida via popup (admin apenas)
- **Controlo de acesso**: Interface adapta conforme permissões do utilizador

### 6.2.4 Gestão da Turma (`/turma/<nome_seguro>`)
- **Grid adaptativo**: Layout responsivo para alunos
- **Estatísticas detalhadas**: Contagem de fotos e progresso
- **Cartões de aluno**: Com thumbnail e ações CRUD conforme permissões
- **Drag & Drop de imagem**: Arraste um ficheiro JPG/PNG para o cartão do aluno para abrir automaticamente o modal de upload manual, com os dados do aluno preenchidos e o ficheiro já selecionado, pronto para envio
- **Destaque visual**: Cartão do aluno recebe destaque visual ao arrastar ficheiro (CSS `.student-card.dragover` em `styles.css`)
- **Dropdown de download**: Opções ZIP e DOCX
- **Ações por aluno**: Editar, transferir, remover, remover foto (baseado em role)
- **Suporte completo**: Todos os alunos aparecem (com/sem foto)
- **Captura de fotos**: Botão direto para interface de captura (editor+)

#### 6.2.5 Configurações (`/settings`)
- **Interface administrativa**: Separação clara entre upload CSV e gestão de utilizadores
- **Upload flexível**: CSV com substituição ou merge (admin apenas)
- **Gestão de utilizadores**: Interface completa para administração de contas
- **Tabela de utilizadores**: Vista detalhada com roles, status e ações
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
Flask-SQLAlchemy         # ORM para base de dados
Flask-Mail               # Sistema de email
opencv-python            # Processamento de imagens
python-docx              # Geração de documentos Word
Pillow                   # Manipulação avançada de imagens
```

### 11.3 Configuração de Ambiente
```env
# Configurações da aplicação
FLASKAPP_DEBUG=True                          # Modo debug (dev/prod)
FLASKAPP_SECRET_KEY=supersecretkey           # Chave para sessões Flask
DATABASE_URL=sqlite:///alunos.db             # URL da base de dados
FLASKAPP_PORT=80                             # Porta de exposição

# Configurações de email
MAIL_USERNAME=seuemail@outlook.com           # Email para envio
MAIL_PASSWORD=suapassword                    # Password do email
MAIL_SENDER=Class Photo Booth <seuemail@outlook.com>  # Remetente

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
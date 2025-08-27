# Class-Photo-Booth
O objetivo da aplicação **Class Photo Booth** é permitir a captura de fotografias de alunos por turma. A aplicação facilita a gestão, visualização e exportação das fotografias de forma organizada.

## 📋 Funcionalidades
```
📸 CLASS PHOTO BOOTH v1.1
Sistema Completo de Gestão de Fotografias Escolares

  🔐 SISTEMA DE AUTENTICAÇÃO COMPLETO
  ├─ 📧 Registo com verificação por email
  ├─ 🔑 Login seguro com proteção anti-brute force
  ├─ 🔄 Recuperação de palavra-passe via email
  ├─ 👥 Sistema de roles (none/viewer/editor/admin)
  ├─ 🛡️ Bloqueio automático de IPs suspeitos
  ├─ 📊 Auditoria completa de acessos
  └─ 👤 Utilizador 'admin@example.com' criado por defeito

  👤 GESTÃO AVANÇADA DE UTILIZADORES
  ├─ ➕ Criação de contas com validação de email
  ├─ ✏️ Edição de dados e permissões
  ├─ 🔑 Reset de palavras-passe por administradores
  ├─ 🔒 Gestão de roles e permissões hierárquicas
  ├─ 📋 Tabela administrativa completa
  ├─ ✅ Aprovação manual de novos utilizadores
  └─ 🔒 Controlo granular de acesso por funcionalidade

  🏠 GESTÃO DE TURMAS (Admin)
  ├─ ➕ Criar turmas
  ├─ ✏️ Editar detalhes das turmas
  ├─ 📋 Ver todas as turmas
  ├─ 🗑️ Eliminar turmas
  └─ 📊 Estatísticas das turmas

  👨‍🎓 GESTÃO DE ALUNOS
  ├─ ➕ Adicionar alunos às turmas
  ├─ ✏️ Editar informações dos alunos
  ├─ 📋 Ver alunos por turma
  ├─ 🗑️ Remover alunos
  ├─ 📊 Estatísticas dos alunos
  └─ 🔍 Procurar e filtrar alunos

  📸 CAPTURA DE FOTOGRAFIAS
  ├─ 📷 Integração com câmara
  ├─ 🖼️ Geração de miniaturas
  ├─ 📁 Armazenamento organizado por turma
  ├─ 🔄 Processamento em lote
  └─ 📊 Estatísticas das fotografias

  📤 EXPORTAÇÃO E DOWNLOAD
  ├─ 📦 Download ZIP (originais/miniaturas)
  ├─ 📄 Geração de DOCX com layout profissional
  ├─ 📊 Estatísticas de exportação
  └─ 🔄 Opções de exportação automatizadas

  ⚙️ PAINEL ADMINISTRATIVO
  ├─ 👤 Gestão de utilizadores
  ├─ 🏠 Gestão de turmas
  ├─ 📊 Estatísticas do sistema
  ├─ 🔧 Definições de configuração
  ├─ 📋 Registos de auditoria
  └─ 🛠️ Manutenção do sistema
```

### 🐳 **Instalação com Docker**
```bash
# 1. Clonar o repositório
git clone https://github.com/jpedrodias/class_photo_booth.git
cd class_photo_booth

# 2. Configurar .env
# Criar .env baseado no exemplo abaixo
# Editar .env com as suas configurações

# 3. Construir e executar
docker-compose up -d

# 4. Adicionar o primeiro utilizador
docker exec -it flaskapp /bin/bash -c "python ./init_database.py"

# 5. Aceder à aplicação
# http://localhost (ou porta configurada)
```

PS: O passo 4 é opcional e neste caso, o primeiro utilizador a criar conta será o Admin.

### 🔧 **Primeiro Acesso**
1. Aceder à aplicação no navegador
2. Fazer login com o utilizador `admin@example.com` e a palavra-passe `ChangeMe1#`
3. Alterar a palavra-passe do utilizador administrador
4. Configurar email de verificação
5. Importar dados via CSV (opcional)
6. Começar a usar!

## 📚 Documentação Completa

Para documentação técnica detalhada, consulte o arquivo [`SPECIFICATIONS.md`](SPECIFICATIONS.md) que inclui:
- Arquitetura completa do sistema
- Modelos de base de dados
- Fluxos de utilizador
- Considerações de segurança
- Guias de implementação

## 🤝 Contribuições

Contribuições são bem-vindas! Para contribuir:

1. Faça fork do projeto
2. Crie uma branch para a sua funcionalidade (`git checkout -b feature/AmazingFeature`)
3. Faça commit das suas alterações (`git commit -m 'Add some AmazingFeature'`)
4. Faça push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE) - veja o arquivo LICENSE para detalhes.

## 📞 Suporte

Para dúvidas, sugestões ou problemas:
- 📧 Email:
- 🐛 Issues: [GitHub Issues](https://github.com/jpedrodias/class_photo_booth/issues)
- 📖 Documentação: [SPECIFICATIONS.md](SPECIFICATIONS.md)

---

**Class Photo Booth v1.1** - Desenvolvido com ❤️ para facilitar a gestão de fotografias escolares
```

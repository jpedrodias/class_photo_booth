# Implementação de Proteção CSRF

## O que foi implementado

### 1. Flask-WTF adicionado às dependências
- Adicionado `Flask-WTF` ao `requirements.txt`

### 2. Configuração no app.py
- Importada a extensão: `from flask_wtf.csrf import CSRFProtect`
- Inicializada a proteção: `csrf = CSRFProtect(app)`
- Criado helper global para templates: `inject_csrf_token()`

### 3. Exceções para APIs
- A rota `/upload/photo/<nome_seguro>/<processo>` foi marcada com `@csrf.exempt` porque é uma API que recebe JSON, não formulários HTML

## Como usar nos templates

### Para todos os formulários HTML, adicionar:
```html
<form method="POST" action="/exemplo">
    <!-- CSRF Token obrigatório -->
    <input type="hidden" name="csrf_token" value="{{ csrf_token() }}"/>
    
    <!-- resto dos campos do formulário -->
    <input type="text" name="campo1">
    <button type="submit">Enviar</button>
</form>
```

### Exemplo já implementado:
- O arquivo `templates/login.html` já foi atualizado com o token CSRF

## Templates que precisam ser atualizados

Todos os formulários nestes templates precisam do token CSRF:

1. **turmas.html**
   - Formulário de adicionar turma (linha 236)
   - Formulário de editar turma (linha 271) 
   - Formulário de eliminar turma (linha 307)

2. **turma.html**
   - Formulário de adicionar aluno (linha 265)
   - Formulário de editar aluno (linha 326)
   - Formulário de eliminar aluno (linha 385)
   - Formulário de transferir aluno (linha 432)
   - Formulário de remover foto (linha 489)
   - Formulário de upload manual (linha 581)

3. **settings.html**
   - Todos os formulários de gestão de utilizadores
   - Formulários de upload CSV
   - Formulário de rescan de fotos
   - Formulário de limpeza completa

## Como aplicar a correção

Para cada formulário `<form>`, adicionar logo após a tag de abertura:
```html
<input type="hidden" name="csrf_token" value="{{ csrf_token() }}"/>
```

## Verificação

Após implementar, se um formulário for submetido sem o token CSRF, receberás um erro 400 (Bad Request) com a mensagem "The CSRF token is missing."

## Segurança adicional

O Flask-WTF também:
- Verifica que o token não expirou
- Verifica que o token foi gerado para a sessão atual
- Protege contra ataques de timing
- Regenera tokens automaticamente quando necessário

## Exceções para APIs

Se tiveres outras rotas que recebem JSON (não formulários HTML), podes marcá-las com:
```python
@csrf.exempt
@app.route('/api/endpoint', methods=['POST'])
def api_endpoint():
    # código da API
```

Mas lembra-te que estas rotas ficam sem proteção CSRF, então implementa outras validações de segurança como:
- Autenticação por token/API key
- Verificação de origem
- Rate limiting

# Skill Doc — Construir o sistema com Claude Code

## O que é o Claude Code

Claude Code é um agente de codificação da Anthropic que opera diretamente
no terminal do seu computador. Ele lê arquivos do projeto, escreve código,
executa comandos e interage com o sistema de arquivos — tudo orientado
pelos artefatos e instruções que você fornece.

Documentação oficial: https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview

## Pré-requisitos

1. Node.js 18 ou superior instalado
   - Verificar: `node --version`
   - Download:  https://nodejs.org

2. Conta Anthropic com acesso à API
   - Obter chave: https://console.anthropic.com

3. Claude Code instalado:
   ```bash
   npm install -g @anthropic-ai/claude-code
   ```

4. Python 3.12 instalado no sistema

## Instalação por sistema operacional

### Windows

```bat
REM 1. Instalar Node.js via https://nodejs.org (LTS recomendado)
REM 2. Abrir Prompt de Comando ou PowerShell como administrador
npm install -g @anthropic-ai/claude-code
claude --version
```

### Linux (Ubuntu/Debian)

```bash
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs
npm install -g @anthropic-ai/claude-code
claude --version
```

### macOS

```bash
brew install node  # ou instalar via https://nodejs.org
npm install -g @anthropic-ai/claude-code
claude --version
```

## Configuração da chave de API

### Windows (PowerShell)

```powershell
$env:ANTHROPIC_API_KEY='sua-chave-aqui'
# Para persistir entre sessões:
[System.Environment]::SetEnvironmentVariable('ANTHROPIC_API_KEY','sua-chave','User')
```

### Linux / macOS

```bash
export ANTHROPIC_API_KEY='sua-chave-aqui'
# Para persistir:
echo "export ANTHROPIC_API_KEY='sua-chave'" >> ~/.bashrc
source ~/.bashrc
```

## Como iniciar uma sessão

```bash
# 1. Abrir terminal
# 2. Navegar até a pasta do projeto:
cd gerenciador_financas_pessoal

# 3. Ativar o ambiente virtual Python:
# Windows:     .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate

# 4. Iniciar Claude Code:
claude
```

## Sequência recomendada de prompts

Copie e use os prompts abaixo em ordem, um por sessão.
Aguarde a execução completa antes de prosseguir.

### PROMPT 1 — Leitura e entendimento dos artefatos

```
Leia os seguintes arquivos nesta ordem:
1. README.md
2. docs/PRD.md
3. docs/FLOW.md
4. docs/SCHEMA.md
5. AGENTS.md
6. CLAUDE.md
7. MEMORY.md

Depois, responda:
a) O que o sistema deve fazer?
b) Quais são as principais restrições?
c) Como os dados estão modelados?
d) Quais dúvidas precisam ser esclarecidas antes de começar?
```

### PROMPT 2 — Preparar ambiente Python

```
Com base nos artefatos lidos:
1. Crie o arquivo requirements.txt (pode ficar vazio ou
   com comentário, pois Tkinter e sqlite3 são nativos)
2. Crie o arquivo .gitignore incluindo .venv/, *.db, __pycache__/
3. Explique como o usuário deve criar e ativar
   o ambiente virtual em Windows, Linux e macOS
```

### PROMPT 3 — Implementar banco de dados

```
Implemente o arquivo database.py com:
- Função get_connection() que retorna conexão SQLite com
  PRAGMA foreign_keys = ON
- Função initialize_db() que cria as tabelas usando o schema
  exatamente como definido em docs/SCHEMA.md
- Inserção das categorias padrão via INSERT OR IGNORE
- Docstrings explicativas em cada função

Restrições:
- Usar apenas sqlite3 da biblioteca padrão
- Não usar ORM externo
- Respeitar o schema do docs/SCHEMA.md sem modificações
```

### PROMPT 4 — Implementar camada de persistência

```
Crie repositories/lancamentos_repository.py com as funções:
- inserir_lancamento(conn, tipo, valor, data, categoria_id, descricao=None)
- listar_lancamentos(conn, tipo=None, categoria_id=None,
    data_inicio=None, data_fim=None)
- listar_categorias(conn)
- calcular_saldo(conn)

Restrições:
- Sem lógica de negócio (apenas SQL)
- Sem imports de ui/ ou services/
- Funções devem receber conexão como parâmetro
- Datas no formato YYYY-MM-DD
```

### PROMPT 5 — Implementar serviços de negócio

```
Crie services/lancamentos_service.py com:
- validar_lancamento(tipo, valor, data, categoria_id)
  que retorna (True, None) ou (False, 'mensagem de erro')
- registrar_lancamento(conn, tipo, valor, data, categoria_id, descricao)
  que valida e chama o repositório

Crie services/saldo_service.py com:
- obter_saldo(conn) que retorna float
- formatar_saldo(valor) que retorna string formatada em R$

Restrições:
- Sem imports de ui/
- tipo deve ser 'receita' ou 'despesa'
- valor deve ser float > 0
- data deve estar no formato YYYY-MM-DD
```

### PROMPT 6 — Implementar interface gráfica

```
Crie ui/main_window.py com uma janela Tkinter que:
- Exibe formulário com: tipo (Combobox), valor (Entry),
  data (Entry com valor padrão hoje), categoria (Combobox),
  descrição (Entry opcional) e botão Salvar
- Exibe saldo consolidado atualizado
- Exibe lista de lançamentos em Treeview com colunas:
  Data, Tipo, Categoria, Valor, Descrição
- Exibe filtros por: período (data início/fim),
  categoria (Combobox) e tipo (Combobox)
- Botão Filtrar atualiza a lista sem apagar dados
- Botão Limpar Filtros restaura a listagem completa

Restrições:
- Usar apenas Tkinter nativo (sem bibliotecas adicionais)
- GUI NÃO deve acessar SQLite diretamente
- Chamar apenas services/ para operações
- Mostrar mensagens de erro ao usuário (messagebox)
```

### PROMPT 7 — Implementar ponto de entrada

```
Crie main.py que:
1. Importa database e ui
2. Chama database.initialize_db() ao iniciar
3. Cria e exibe a janela principal
4. Trata exceções de inicialização com mensagem clara
```

### PROMPT 8 — Validação completa

```
Execute o sistema: python main.py

Verifique se:
1. A janela abre sem erros
2. É possível cadastrar uma receita de R$ 1000,00
3. É possível cadastrar uma despesa de R$ 150,00
4. O saldo exibe R$ 850,00
5. Ao fechar e reabrir, os dados persistem
6. Os filtros funcionam sem apagar dados

Se algo falhar, mostre o erro e corrija.
Depois, atualize MEMORY.md com as decisões tomadas.
```

## Dicas para profissionais de outras áreas

- Se o agente pedir confirmação antes de criar arquivos, diga 'sim'
- Se o agente listar lacunas antes de implementar, responda às perguntas
- Se algo não funcionar, cole a mensagem de erro no chat
- Não precisa entender o código: entenda o que cada parte faz
- Salve as conversas importantes para referência futura

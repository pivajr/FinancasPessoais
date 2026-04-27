# Skill Doc — Construir o sistema com Codex CLI

## O que é o Codex CLI

Codex CLI é o agente de codificação da OpenAI para terminal.
Funciona de forma similar ao Claude Code: lê arquivos do projeto,
escreve código e executa comandos orientado pelos artefatos fornecidos.

Documentação: https://github.com/openai/codex

## Pré-requisitos

1. Node.js 22 ou superior
   - Verificar: `node --version`

2. Conta OpenAI com acesso à API
   - Obter chave: https://platform.openai.com/api-keys

3. Codex CLI instalado:
   ```bash
   npm install -g @openai/codex
   ```

4. Python 3.12 instalado

## Instalação por sistema operacional

### Windows

```bat
REM 1. Instalar Node.js 22+ via https://nodejs.org
REM 2. Abrir PowerShell como administrador
npm install -g @openai/codex
codex --version
```

### Linux (Ubuntu/Debian)

```bash
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt-get install -y nodejs
npm install -g @openai/codex
codex --version
```

### macOS

```bash
brew install node@22
npm install -g @openai/codex
codex --version
```

## Configuração da chave de API

### Windows (PowerShell)

```powershell
$env:OPENAI_API_KEY='sua-chave-aqui'
```

### Linux / macOS

```bash
export OPENAI_API_KEY='sua-chave-aqui'
```

## Como iniciar uma sessão

```bash
cd gerenciador_financas_pessoal
# Ativar ambiente virtual Python
codex
```

## Modo de aprovação

O Codex opera em três modos:

- `suggest`   → sugere, você aprova cada passo (mais seguro)
- `auto-edit` → edita arquivos automaticamente, você aprova execuções
- `full-auto` → executa tudo automaticamente (use com cuidado)

Para iniciantes, use o modo padrão (suggest) ou auto-edit:

```bash
codex --approval-mode auto-edit
```

## Sequência recomendada de prompts

Use os mesmos prompts descritos em `build_with_claude_code.md`
(PROMPT 1 a PROMPT 8). Os prompts são compatíveis com ambos os agentes.

Diferença principal na sintaxe de uso:

```
Claude Code: claude
Codex CLI:   codex
```

## Diferenças práticas entre os agentes

| Aspecto              | Claude Code        | Codex CLI           |
|----------------------|--------------------|---------------------|
| Empresa              | Anthropic          | OpenAI              |
| Modelo padrão        | Claude Sonnet      | o4-mini / GPT-4o    |
| Contexto de arquivos | Lê projeto inteiro | Lê arquivos pedidos |
| Execução de comandos | Sim                | Sim                 |
| Modo interativo      | Sim                | Sim                 |
| Conta necessária     | Anthropic API      | OpenAI API          |

## Dicas para profissionais de outras áreas

- O Codex pode pedir confirmação antes de executar comandos: sempre leia
- Se aparecer erro de permissão, execute o terminal como administrador
- Em caso de dúvida sobre um prompt, comece com:
  `'Leia o AGENTS.md e me diga o que você entende sobre este projeto'`
- Guarde os prompts que funcionaram bem para reutilizar

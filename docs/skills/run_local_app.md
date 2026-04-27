# Skill Doc — Executar a aplicação localmente

## Passo a passo

1. Ativar o ambiente virtual

   - Windows:      `.venv\Scripts\activate`
   - Linux/macOS:  `source .venv/bin/activate`

2. Executar:

   ```bash
   python main.py
   # ou: python3 main.py
   ```

## Comportamento esperado

- Banco SQLite criado automaticamente (se não existir)
- Janela principal abre sem erros
- Categorias padrão carregadas
- Saldo exibido como R$ 0,00 na primeira execução

## Verificações mínimas

- [ ] Interface abre sem erro
- [ ] É possível cadastrar uma receita
- [ ] É possível cadastrar uma despesa
- [ ] Lançamento aparece na listagem
- [ ] Saldo é atualizado corretamente
- [ ] Ao fechar e reabrir, os dados persistem
- [ ] Filtros funcionam sem apagar dados

## Política de falha

Se a interface não abrir:

1. Verificar versão do Python (3.12 recomendado)
2. Verificar se Tkinter está disponível
3. Verificar erros de importação no terminal
4. Verificar se o banco foi criado em `financas.db`

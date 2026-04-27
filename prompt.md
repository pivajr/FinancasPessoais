# PROMPT CONTRACT
# Construção da Aplicação Python — Gerenciador de Finanças Pessoal
# Agente: Claude Code | Diretório raiz: Fin_Pessoal/
# Referência metodológica: Capítulo 5 — Prompt Contracts

---

## LEITURA OBRIGATÓRIA DE ARTEFATOS

Antes de processar qualquer bloco deste contrato, leia os arquivos
abaixo nesta ordem exata. Não pule nenhum. Não assuma nada que não
esteja escrito neles.

  1.  Fin_Pessoal/README.md
  2.  Fin_Pessoal/docs/PRD.md
  3.  Fin_Pessoal/docs/FLOW.md
  4.  Fin_Pessoal/docs/SCHEMA.md
  5.  Fin_Pessoal/AGENTS.md
  6.  Fin_Pessoal/CLAUDE.md
  7.  Fin_Pessoal/MEMORY.md
  8.  Fin_Pessoal/docs/CONTEXT_PROJECT.md
  9.  Fin_Pessoal/docs/CONTEXT_ARCHITECTURE.md
  10. Fin_Pessoal/docs/CONTEXT_WORKFLOW.md

Após ler todos os artefatos, responda apenas:
  a) "Artefatos lidos. Projeto compreendido." — se tudo estiver claro.
  b) Uma lista numerada de dúvidas críticas — se houver lacunas que
     impeçam a execução segura de qualquer etapa.

Aguarde confirmação ou resolução das dúvidas antes de iniciar.
Se não houver dúvidas, aguarde o comando GO.

---

## BLOCO 1 — OBJETIVO

### Objetivo central

Implementar a aplicação completa do Gerenciador de Finanças Pessoal
em Python, produzindo todos os arquivos .py do projeto e o arquivo
requirements.txt, dentro da estrutura de diretórios já existente
em Fin_Pessoal/, de acordo com os artefatos lidos acima.

O resultado desta sessão deve ser um sistema funcional, executável
localmente com o comando `python main.py`, que um usuário real consiga
usar imediatamente para registrar receitas e despesas, visualizar saldo
e consultar histórico — sem necessidade de qualquer ajuste manual
posterior no código.

### Sub-objetivos por camada

1. Criar requirements.txt e .gitignore na raiz do projeto.

2. Implementar Fin_Pessoal/database.py:
   - Conexão SQLite com PRAGMA foreign_keys = ON
   - Inicialização do banco (tabelas + índices + categorias padrão)

3. Implementar Fin_Pessoal/repositories/lancamentos_repository.py:
   - Listagem de categorias ativas
   - Inserção de lançamento
   - Listagem de lançamentos com filtros opcionais
   - Cálculo de saldo

4. Implementar Fin_Pessoal/services/lancamentos_service.py:
   - Validação de campos do lançamento
   - Orquestração de registro (valida → persiste)

5. Implementar Fin_Pessoal/services/saldo_service.py:
   - Obtenção do saldo consolidado
   - Formatação monetária em R$

6. Implementar Fin_Pessoal/ui/main_window.py:
   - Formulário de cadastro (tipo, valor, data, categoria, descrição)
   - Exibição de saldo consolidado atualizado
   - Área de filtros (período, categoria, tipo)
   - Treeview com listagem de lançamentos
   - Integração exclusivamente via services/ (escrita) e
     repositories/ (leitura)

7. Implementar Fin_Pessoal/main.py:
   - Ponto de entrada: inicializa banco, abre conexão, exibe janela

8. Criar arquivos __init__.py vazios em:
   - Fin_Pessoal/repositories/
   - Fin_Pessoal/services/
   - Fin_Pessoal/ui/

### Fora de escopo nesta sessão

- Edição ou exclusão de lançamentos (próximo incremento)
- Cadastro de novas categorias pelo usuário
- Exportação de dados (CSV, PDF ou qualquer outro formato)
- Gráficos, relatórios ou visualizações além do Treeview
- Múltiplos usuários ou qualquer forma de autenticação
- Sincronização em nuvem ou acesso remoto
- Testes automatizados (previstos para incremento separado)
- Modificação de qualquer arquivo .md existente no projeto

---

## BLOCO 2 — RESTRIÇÕES

### Stack obrigatória

- Linguagem: Python 3.12
- Interface gráfica: Tkinter nativo (tkinter, tkinter.ttk,
  tkinter.messagebox) — sem bibliotecas externas de GUI
- Banco de dados: SQLite via sqlite3 da biblioteca padrão
- ORM: nenhum — apenas SQL direto via sqlite3
- Dependências externas: nenhuma — requirements.txt ficará vazio
  (apenas comentário explicativo)

### Arquitetura — separação obrigatória de camadas

A arquitetura do projeto segue três camadas claramente separadas,
conforme definido em CONTEXT_ARCHITECTURE.md:

  ui/  →  services/  →  repositories/

Cada camada tem responsabilidade exclusiva:

- ui/ (main_window.py): componentes Tkinter, eventos, exibição.
  NÃO deve importar sqlite3. NÃO deve conter SQL.
  NÃO deve conter regras de negócio.

- services/ (lancamentos_service.py, saldo_service.py): validações,
  cálculos, orquestração. NÃO deve acessar o banco diretamente.
  NÃO deve importar nada de ui/.

- repositories/ (lancamentos_repository.py): apenas SQL via sqlite3.
  NÃO deve conter lógica de negócio. NÃO deve importar nada de ui/
  ou services/.

- database.py: exclusivamente conexão e inicialização do banco.
  NÃO deve importar nada de ui/, services/ ou repositories/.

- main.py: ponto de entrada. Autorizado a importar database e ui.

Qualquer violação dessa separação é uma restrição bloqueante.
Se a implementação de uma funcionalidade exigir acoplamento indevido
entre camadas, pare, declare o problema e proponha alternativa.

### Convenções de código

- Cada arquivo .py deve ter docstring no topo explicando sua
  responsabilidade dentro da arquitetura do projeto.
- Cada função deve ter docstring descrevendo parâmetros e retorno.
- Nomes de variáveis, funções e parâmetros em português, seguindo
  o padrão já adotado nos artefatos (lancamento, categoria, saldo,
  tipo, valor, data_lancamento, descricao, categoria_id).
- Nomes de arquivos e módulos em snake_case, conforme estrutura
  já definida.
- Datas sempre no formato YYYY-MM-DD, sem exceção.
- Valores monetários armazenados como NUMERIC/float; formatação
  em R$ feita exclusivamente pela função formatar_saldo() em
  saldo_service.py.

### Convenções de banco de dados

- A conexão deve sempre executar PRAGMA foreign_keys = ON
  imediatamente após abrir.
- Todas as tabelas e índices criados com IF NOT EXISTS.
- Categorias padrão inseridas via INSERT OR IGNORE.
- O schema SQL a ser implementado é exatamente o definido em
  Fin_Pessoal/docs/SCHEMA.md — sem alterações, sem otimizações
  não previstas, sem campos adicionais.

### O que não pode acontecer

- Não introduzir nenhuma biblioteca externa (sem pip install).
- Não usar ORM (SQLAlchemy, Peewee, Django ORM ou qualquer outro).
- Não criar tabelas, campos ou índices além dos definidos em SCHEMA.md.
- Não modificar arquivos .md existentes.
- Não criar arquivos fora da estrutura definida em CONTEXT_PROJECT.md.
- Não implementar funcionalidades listadas em "Fora de escopo".
- Não avançar para a etapa seguinte sem concluir e verificar a atual.
- Não usar dados hardcoded na interface; tudo que vier do banco deve
  ser lido do banco.
- Não usar variáveis globais para a conexão com o banco — a conexão
  deve ser passada como parâmetro entre as camadas.

---

## BLOCO 3 — FORMATO DE SAÍDA

### Protocolo de execução

Este contrato é executado em etapas sequenciais, controladas por
comandos explícitos do humano. Nenhuma etapa avança sem confirmação.

Comando GO      → inicia a Etapa 1.
Comando PRÓXIMO → avança para a etapa seguinte.
Comando PARAR   → interrompe a execução. Aguardar nova instrução.

### Formato de resposta ao concluir cada etapa

Ao finalizar cada etapa, responda exatamente nesta estrutura:

  ✅ ETAPA [N] CONCLUÍDA — [nome da etapa]

  Arquivos criados ou modificados:
  - [caminho completo de cada arquivo]

  O que foi implementado:
  [2 a 3 frases descrevendo o que foi feito e como se conecta
  à arquitetura do projeto]

  Limitações ou decisões tomadas:
  [Se houver alguma decisão não prevista nos artefatos, ou alguma
  limitação encontrada, registre aqui. Se não houver, escreva
  "Nenhuma."]

  Pronto para PRÓXIMO.

### Formato de resposta ao encontrar ambiguidade durante uma etapa

Se encontrar qualquer ambiguidade, lacuna ou conflito durante
a execução de uma etapa, interrompa imediatamente e responda:

  ⚠️ PAUSA NA ETAPA [N] — [descrição curta do problema]

  Situação encontrada:
  [Descreva com precisão o que está indefinido ou conflitante]

  Alternativa A:
  [Descreva a primeira opção, com implicações]

  Alternativa B:
  [Descreva a segunda opção, com implicações]

  Aguardando decisão antes de continuar.

Não escolha uma alternativa por conta própria. Não invente solução
para contornar o problema. Aguarde instrução explícita.

### Especificação dos arquivos e seus conteúdos esperados

#### requirements.txt

  # Gerenciador de Finanças Pessoal — MVP
  # Sem dependências externas.
  # Tkinter e sqlite3 fazem parte da biblioteca padrão do Python 3.12.
  # Para instalar o ambiente virtual:
  #   python -m venv .venv
  #   source .venv/bin/activate    (Linux/macOS)
  #   .venv\Scripts\activate       (Windows)

#### .gitignore

Deve incluir no mínimo:
  .venv/
  __pycache__/
  *.pyc
  *.pyo
  *.db
  *.db-shm
  *.db-wal
  .env
  .DS_Store

#### database.py

Funções obrigatórias:

  get_connection(db_path="financas.db") → sqlite3.Connection
    - Abre conexão SQLite no caminho informado
    - Executa PRAGMA foreign_keys = ON imediatamente
    - Retorna a conexão aberta
    - Inclui bloco if __name__ == "__main__" para teste direto

  initialize_db(db_path="financas.db") → None
    - Chama get_connection()
    - Executa o SQL completo de criação de tabelas e índices
      conforme docs/SCHEMA.md
    - Insere categorias padrão via INSERT OR IGNORE
    - Fecha a conexão ao final
    - Exibe mensagem de confirmação quando executado diretamente

#### repositories/lancamentos_repository.py

Funções obrigatórias (todas recebem conn como primeiro parâmetro):

  listar_categorias(conn) → list[dict]
    Retorno: [{"id": int, "nome": str, "tipo_padrao": str | None}]
    Filtro: ativo = 1 apenas

  inserir_lancamento(conn, tipo, valor, data_lancamento,
                     categoria_id, descricao=None) → int
    Retorno: id do registro inserido (lastrowid)

  listar_lancamentos(conn, tipo=None, categoria_id=None,
                     data_inicio=None, data_fim=None) → list[dict]
    Retorno: [{"id", "tipo", "valor", "data_lancamento",
               "descricao", "categoria_id", "nome_categoria",
               "criado_em"}]
    Todos os parâmetros são filtros opcionais (None = sem filtro)
    Ordenação: data_lancamento DESC, id DESC

  calcular_saldo(conn) → float
    Retorno: soma(receitas) - soma(despesas)
    Retorna 0.0 se não houver lançamentos

#### services/lancamentos_service.py

Funções obrigatórias:

  validar_lancamento(tipo, valor, data_lancamento,
                     categoria_id) → tuple[bool, str | None]
    Retorno sucesso:  (True, None)
    Retorno falha:    (False, "mensagem de erro descritiva")
    Validações:
      - tipo: deve ser exatamente 'receita' ou 'despesa'
      - valor: deve ser conversível para float e maior que zero
      - data_lancamento: deve estar no formato YYYY-MM-DD e
        ser uma data de calendário válida
      - categoria_id: deve ser inteiro maior que zero

  registrar_lancamento(conn, tipo, valor, data_lancamento,
                       categoria_id, descricao=None) → int
    - Chama validar_lancamento()
    - Se inválido: levanta ValueError com a mensagem de erro
    - Se válido: chama inserir_lancamento() do repositório
    - Retorna o id do lançamento inserido

#### services/saldo_service.py

Funções obrigatórias:

  obter_saldo(conn) → float
    - Chama calcular_saldo() do repositório
    - Retorna float

  formatar_saldo(valor: float) → str
    - Retorna string no formato: "R$ 1.250,00"
    - Valores negativos: "R$ -1.250,00"
    - Sem bibliotecas externas de formatação monetária

#### ui/main_window.py

Classe obrigatória: MainWindow(tk.Frame)

  __init__(self, master, conn):
    - Recebe a janela raiz (master) e a conexão (conn)
    - Carrega categorias via listar_categorias()
    - Monta todos os widgets
    - Carrega lançamentos iniciais
    - Exibe saldo inicial

  Layout obrigatório (de cima para baixo):

  [ÁREA 1 — FORMULÁRIO DE CADASTRO]
    - Combobox: Tipo        → valores: Receita | Despesa
    - Entry:    Valor       → numérico
    - Entry:    Data        → YYYY-MM-DD, padrão = hoje
    - Combobox: Categoria   → populado do banco, apenas ativas
    - Entry:    Descrição   → opcional
    - Botão:    Salvar

  [ÁREA 2 — SALDO CONSOLIDADO]
    - Label: "Saldo consolidado: R$ X.XXX,XX"
    - Atualizado após cada cadastro bem-sucedido

  [ÁREA 3 — FILTROS]
    - Entry:    Data início  → YYYY-MM-DD
    - Entry:    Data fim     → YYYY-MM-DD
    - Combobox: Categoria    → mesmas categorias do formulário
    - Combobox: Tipo         → Todos | Receita | Despesa
    - Botão:    Filtrar
    - Botão:    Limpar Filtros

  [ÁREA 4 — LISTAGEM]
    - Treeview com colunas: Data | Tipo | Categoria | Valor | Descrição
    - Coluna Valor alinhada à direita, formatada em R$
    - Linhas em receita com cor diferente de despesa (opcional,
      mas valorizado — use apenas se não comprometer a clareza)
    - Ordenação: mais recente primeiro

  Comportamentos obrigatórios:

  Botão Salvar:
    1. Lê os campos do formulário
    2. Chama lancamentos_service.registrar_lancamento()
    3. Se ValueError: exibe messagebox.showerror() com a mensagem
    4. Se sucesso: limpa formulário, atualiza Treeview e saldo

  Botão Filtrar:
    1. Lê os campos de filtro
    2. Chama lancamentos_repository.listar_lancamentos() com filtros
    3. Atualiza o Treeview sem alterar dados no banco

  Botão Limpar Filtros:
    1. Limpa todos os campos de filtro
    2. Recarrega todos os lançamentos (sem filtro)
    3. Atualiza o Treeview

#### main.py

Estrutura obrigatória:

  import tkinter as tk
  import tkinter.messagebox as messagebox
  from database import initialize_db, get_connection
  from ui.main_window import MainWindow

  def main():
      try:
          initialize_db()
          conn = get_connection()
          root = tk.Tk()
          root.title("Gerenciador de Finanças Pessoal")
          app = MainWindow(root, conn)
          app.pack(fill="both", expand=True)
          root.mainloop()
      except Exception as e:
          messagebox.showerror("Erro de inicialização", str(e))
          raise

  if __name__ == "__main__":
      main()

### Checklist de verificação final (Etapa 8)

Após executar `python main.py`, confirme cada item abaixo.
Responda com ✅ ou ❌ para cada um, com observação se ❌.

  [ ] A janela abre sem erros ou warnings no terminal
  [ ] O título da janela exibe "Gerenciador de Finanças Pessoal"
  [ ] O Combobox de categorias está populado com as categorias padrão
  [ ] É possível cadastrar uma receita de R$ 1.000,00 na categoria Salário
  [ ] É possível cadastrar uma despesa de R$ 150,00 na categoria Transporte
  [ ] Após os dois cadastros, o saldo exibe R$ 850,00
  [ ] Os dois lançamentos aparecem no Treeview após o cadastro
  [ ] Ao fechar e reabrir (python main.py), os dados persistem
  [ ] O filtro por tipo "Despesa" exibe apenas a despesa cadastrada
  [ ] O botão Limpar Filtros restaura os dois lançamentos na listagem
  [ ] Tentar salvar sem preencher o valor exibe mensagem de erro
  [ ] Tentar salvar com valor zero ou negativo exibe mensagem de erro
  [ ] Tentar salvar com data em formato inválido exibe mensagem de erro
  [ ] O banco financas.db foi criado na pasta Fin_Pessoal/

### Formato do relatório de atualização do MEMORY.md (Etapa 9)

Adicione ao final de Fin_Pessoal/MEMORY.md exatamente esta seção:

  ---

  ## Sessão de construção — [data atual no formato YYYY-MM-DD]

  ### Arquivos criados
  [Lista de todos os arquivos .py e de configuração criados,
  com caminho relativo a partir de Fin_Pessoal/]

  ### Decisões tomadas durante a implementação
  [Registre cada decisão tomada que não estava explicitamente
  prevista nos artefatos. Se nenhuma, escreva "Nenhuma."]

  ### Desvios em relação aos artefatos
  [Registre qualquer ponto em que a implementação diferiu do
  que estava especificado. Se nenhum, escreva "Nenhum."]

  ### Limitações identificadas
  [Limitações técnicas ou de escopo descobertas durante a
  construção. Se nenhuma, escreva "Nenhuma."]

  ### Próximos incrementos sugeridos
  - Edição de lançamentos existentes
  - Exclusão de lançamentos com confirmação
  - Exportação de dados em CSV
  - Testes automatizados (pytest) para services e repositories
  - Cadastro de novas categorias pelo usuário

---

## BLOCO 4 — CONDIÇÕES DE FALHA

As condições abaixo definem situações em que a execução deve
ser interrompida. A resposta correta não é improvisar uma solução.
É sinalizar, parar e aguardar instrução.

### CF-01 — Conflito com artefatos

Se qualquer decisão de implementação necessária para viabilizar
uma funcionalidade contradizer o que está definido em PRD.md,
FLOW.md, SCHEMA.md, AGENTS.md, CLAUDE.md ou MEMORY.md:

→ Pare a etapa.
→ Descreva o conflito com precisão.
→ Cite os trechos em conflito de cada artefato.
→ Proponha no máximo 2 alternativas de resolução.
→ Aguarde decisão humana antes de continuar.

Não contorne silenciosamente nenhum conflito entre artefatos.

### CF-02 — Violação de separação de camadas

Se uma funcionalidade da interface gráfica exigir acesso direto
ao banco de dados (importar sqlite3 em ui/), ou se uma função
do repositório precisar de lógica de negócio (validação em
repositories/), ou qualquer outro cruzamento de camadas:

→ Pare a etapa.
→ Descreva o cruzamento identificado.
→ Proponha a refatoração mínima para preservar a separação.
→ Aguarde aprovação antes de implementar.

Violações de arquitetura não são contornadas. São resolvidas.

### CF-03 — Schema divergente

Se a implementação do database.py ou do repositório exigir
tabelas, campos, tipos ou índices que não estão em SCHEMA.md:

→ Pare a etapa.
→ Liste exatamente o que está divergindo.
→ Não crie tabelas ou campos adicionais por iniciativa própria.
→ Aguarde confirmação antes de qualquer alteração no schema.

O schema é fonte de verdade. Código se adapta ao schema,
não o contrário.

### CF-04 — Dependência externa não autorizada

Se a implementação de qualquer funcionalidade parecer exigir
uma biblioteca que não seja parte da biblioteca padrão do
Python 3.12 (tkinter, sqlite3, datetime, os, sys, etc.):

→ Pare a etapa.
→ Descreva qual funcionalidade exige a dependência.
→ Nomeie a biblioteca necessária e o que ela resolveria.
→ Proponha uma alternativa com biblioteca nativa.
→ Aguarde aprovação antes de instalar qualquer dependência.

Nenhuma dependência externa é instalada sem decisão explícita.

### CF-05 — Funcionalidade fora de escopo solicitada ou inferida

Se, ao interpretar os artefatos ou o código existente, identificar
que uma funcionalidade aparentemente necessária está na lista
"Fora de escopo" deste contrato (edição, exclusão, exportação,
autenticação, múltiplos usuários, gráficos, etc.):

→ Não implemente.
→ Registre a observação na seção "Limitações identificadas"
  da Etapa 9.
→ Sugira o incremento correspondente nos próximos passos.

### CF-06 — Contexto insuficiente para implementação segura

Se, em qualquer momento, faltar informação nos artefatos para
tomar uma decisão técnica que não seja trivial — e se essa decisão
impactar comportamento visível ao usuário, integridade dos dados
ou arquitetura do projeto:

→ Pare a etapa.
→ Descreva exatamente o que está faltando.
→ Não invente comportamento, não assuma padrão genérico.
→ Proponha no máximo 2 formas de obter a informação necessária.
→ Aguarde instrução antes de continuar.

### CF-07 — Falha na verificação final

Se, durante a Etapa 8, qualquer item do checklist não puder
ser marcado como ✅:

→ Não avance para a Etapa 9.
→ Identifique o arquivo responsável pela falha.
→ Apresente o traceback completo.
→ Proponha a correção mínima necessária.
→ Re-execute apenas o trecho afetado.
→ Repita a verificação do item específico antes de continuar.

A verificação completa é pré-requisito para o encerramento
da sessão. Não é opcional.

---

## PROTOCOLO DE EXECUÇÃO — RESUMO OPERACIONAL

Passo 1: Cole este contrato inteiro no Claude Code.
Passo 2: Aguarde a confirmação de leitura dos artefatos.
Passo 3: Resolva as dúvidas listadas (se houver).
Passo 4: Digite GO para iniciar a Etapa 1.
Passo 5: Após cada etapa, revise os arquivos criados.
Passo 6: Digite PRÓXIMO para avançar à etapa seguinte.
Passo 7: Na Etapa 8, valide manualmente cada item do checklist.
Passo 8: Confirme a atualização do MEMORY.md na Etapa 9.

Em qualquer momento, digite PARAR para interromper a execução.

Sequência de etapas:

  ETAPA 1 — requirements.txt e .gitignore
  ETAPA 2 — database.py
  ETAPA 3 — repositories/lancamentos_repository.py
  ETAPA 4 — services/lancamentos_service.py
  ETAPA 5 — services/saldo_service.py
  ETAPA 6 — ui/main_window.py
  ETAPA 7 — main.py
  ETAPA 8 — Verificação funcional completa
  ETAPA 9 — Atualização do MEMORY.md

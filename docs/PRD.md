# PRD — Gerenciador de Finanças Pessoais

## 1 Visão do produto

O Gerenciador de Finanças Pessoais é uma aplicação **desktop local** para controle financeiro individual. Seu objetivo é permitir o registro e a consulta de receitas e despesas de forma simples, com categorização, saldo consolidado e histórico persistente.

## 2 Problema que o produto resolve

O produto reduz a desorganização decorrente de registros dispersos. Ele aumenta a visibilidade sobre entradas e saídas por período e por categoria, permitindo decisões financeiras menos baseadas em percepção e mais baseadas em registro.

## 3 Objetivo do sistema

O sistema deve permitir que um usuário individual:

- cadastre receitas e despesas;
- associe categoria a cada lançamento;
- registre data, valor e descrição opcional;
- visualize saldo consolidado;
- consulte histórico de movimentações;
- filtre a listagem por período, categoria e tipo;
- mantenha os dados gravados entre execuções do programa.

## 4 Perfil de usuário

O usuário principal é alguém que deseja controle financeiro básico, prefere simplicidade, não quer depender de internet e aceita cadastrar movimentações manualmente.

Existe também um perfil secundário: estudantes e leitores que usam o projeto como caso prático para aprender Python com interface gráfica e banco de dados.

## 5 Escopo do MVP

O que entra na primeira versão:

- cadastro manual de lançamentos (receita ou despesa);
- categorias associadas a cada lançamento;
- data, valor e descrição opcional;
- listagem dos lançamentos cadastrados;
- filtros básicos por período, categoria e tipo;
- exibição de saldo consolidado;
- persistência local em SQLite;
- interface gráfica desktop simples.

## 6 Fora de escopo no MVP

O que fica para depois (ou para nunca, se não fizer sentido):

- login, autenticação e múltiplos usuários;
- sincronização em nuvem;
- integração com bancos ou cartões, importação de extratos;
- gráficos avançados e relatórios sofisticados;
- recorrência automática, metas complexas e controle de investimentos;
- versões web e mobile.

## 7 Requisitos funcionais

**RF01** — Cadastrar lançamento financeiro.
**RF02** — Definir tipo do lançamento: receita ou despesa.
**RF03** — Registrar valor monetário (obrigatoriamente maior que zero).
**RF04** — Associar categoria ao lançamento.
**RF05** — Registrar data da movimentação.
**RF06** — Registrar descrição opcional.
**RF07** — Listar lançamentos cadastrados.
**RF08** — Exibir saldo consolidado.
**RF09** — Filtrar lançamentos por período.
**RF10** — Filtrar lançamentos por categoria.
**RF11** — Filtrar lançamentos por tipo.
**RF12** — Persistir dados em SQLite.
**RF13** — Reabrir dados persistidos ao iniciar novamente.
**RF14** — Validar campos obrigatórios antes de salvar.
**RF15** — Atualizar listagem após cadastro bem-sucedido.
**RF16** — Atualizar saldo após cadastro bem-sucedido.

## 8 Requisitos não funcionais

**RNF01** — Execução local sem depender de internet.
**RNF02** — Compatibilidade com Windows, Linux e macOS.
**RNF03** — Arquitetura simples, legível e didática.
**RNF04** — Persistência confiável em SQLite.
**RNF05** — Usabilidade básica e intuitiva.
**RNF06** — Baixo acoplamento entre GUI, regras de negócio e persistência.
**RNF07** — Facilidade de evolução incremental sem reescrita excessiva.
**RNF08** — Preferência por bibliotecas padrão ou dependências mínimas.

## 9 Critérios de aceite do MVP

O MVP será considerado pronto quando:

- for possível cadastrar receita e despesa com validação dos campos;
- os dados persistirem em SQLite e reaparecerem ao reabrir o programa;
- a listagem exibir lançamentos e responder a filtros básicos;
- o saldo consolidado for calculado corretamente e atualizado após cada cadastro;
- o projeto permanecer simples e compreensível.

## 10 Riscos e cuidados

- **Inflação de escopo:** a tentação de adicionar gráficos, metas e integrações antes de o MVP estar consolidado.
- **Acoplamento excessivo:** misturar SQL diretamente na interface gráfica, comprometendo manutenção futura.
- **Divergência entre artefatos:** PRD, fluxo, schema e código dizendo coisas diferentes — o pior tipo de inconsistência.

## Sobre este projeto

Este não é um sistema financeiro corporativo.
É um Gerenciador de Finanças Pessoal: local, simples, didático e evolutivo.

O valor aqui não está em complexidade tecnológica.
Está na coerência entre problema, fluxo, modelagem e implementação.

## Público deste projeto

Este projeto foi pensado para três perfis distintos:

1. Desenvolvedores em formação que querem aprender Python com GUI e SQLite
   a partir de um caso real e bem estruturado.
2. Profissionais de outras áreas (gestores, analistas, professores,
   empreendedores) que desejam construir o sistema com ajuda de agentes,
   mesmo sem experiência prévia em programação.
3. Leitores do livro que querem praticar os conceitos de Programação
   Aumentada por IA em um projeto completo e reproduzível.

Para o perfil 1: o código e a arquitetura devem ser legíveis e didáticos.
Para o perfil 2: os artefatos e as instruções devem ser autoexplicativos.
Para o perfil 3: a coerência entre artefatos é a principal lição.

## O que é importante preservar

- Simplicidade real de uso
- Execução completamente local
- Stack acessível (Python, Tkinter, SQLite)
- Arquitetura leve e compreensível
- Separação mínima entre GUI, regras e persistência
- Clareza para leitores em formação e profissionais de outras áreas

## O que evitar

- Inventar recursos sofisticados antes do MVP estar consolidado
- Converter o projeto para web
- Trocar a stack base sem necessidade documentada
- Usar jargão técnico desnecessário nas explicações
- Acoplar a interface ao banco de dados
- Propor abstrações prematuras
- Adicionar dependências externas sem justificativa explícita

## Como pensar ao trabalhar neste repositório

Antes de escrever código, pense nesta sequência:

1. Qual problema real esta mudança resolve?
2. Isso cabe no escopo atual do MVP?
3. O fluxo do sistema continua coerente?
4. O schema ainda sustenta a lógica?
5. A implementação está simples o suficiente?
6. A mudança será compreensível para quem estudar depois?
7. Quem não é desenvolvedor consegue entender o que foi feito?

## Relação entre artefatos

- PRD.md     → define o que o sistema é e o que ele não é
- FLOW.md    → explica como o sistema se comporta
- SCHEMA.md  → explica como os dados são organizados
- MEMORY.md  → registra decisões operacionais e aprendizados
- O código deve nascer como consequência desses artefatos.

## Regra fundamental

Se houver tensão entre sofisticação e clareza, prefira clareza.
Se houver tensão entre velocidade e coerência, prefira coerência.

## Quando registrar em MEMORY.md

Registre quando:

- Uma decisão importante de modelagem for tomada
- Um desvio justificado do plano original acontecer
- Uma limitação relevante for descoberta
- Uma convenção operacional for criada
- Uma dívida técnica consciente for aceita

## Forma de colaborar

O modelo de colaboração ideal neste projeto é:

```
humano define problema
  → artefatos delimitam intenção
  → agente implementa parte restrita
  → humano revisa
  → projeto aprende
  → memória é atualizada
```

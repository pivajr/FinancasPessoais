# Skill Doc — Revisar consistência entre GUI e SQLite

## Objetivo

Verificar se a interface gráfica e o banco de dados estão coerentes,
garantindo que nenhum dado exibido na GUI diverge do que está persistido
no SQLite, e que nenhuma operação da GUI acessa o banco diretamente.

## Passo a passo

1. Listar todos os widgets e campos da interface (`ui/main_window.py`)
2. Para cada campo exibido, identificar a coluna correspondente no SQLite
3. Verificar se os tipos de dados são compatíveis (ex: datas, valores)
4. Confirmar que a GUI chama apenas `services/`, nunca `repositories/` diretamente
5. Confirmar que os filtros da GUI geram queries corretas via repositório
6. Verificar se o saldo exibido corresponde ao cálculo em `saldo_service.py`

## Checklist de consistência

- [ ] Todos os campos do formulário têm coluna correspondente no banco?
- [ ] O formato de data na GUI é YYYY-MM-DD?
- [ ] O valor monetário é convertido corretamente para float antes de salvar?
- [ ] A listagem exibe exatamente os campos retornados pelo repositório?
- [ ] O saldo é recalculado após cada inserção?
- [ ] A GUI não importa `sqlite3` nem `repositories/` diretamente?

## Saída esperada

1. Mapeamento campo GUI → coluna SQLite
2. Inconsistências encontradas (tipos, formatos, valores)
3. Violações de separação de camadas
4. Correções necessárias

## Política de falha

Se houver acoplamento direto entre GUI e banco, registrar como
dívida técnica em MEMORY.md e propor refatoração no próximo incremento.

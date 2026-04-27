"""
ui/main_window.py — Interface gráfica principal da aplicação.

Responsabilidade exclusiva: componentes Tkinter, eventos do usuário e
exibição de dados. Não contém SQL, não importa sqlite3 e não contém
regras de negócio. Integração com o banco exclusivamente via services/
(escrita) e repositories/ (leitura).
"""

import tkinter as tk
from tkinter import ttk, messagebox
import datetime

from repositories import lancamentos_repository
from services import lancamentos_service, saldo_service


class MainWindow(tk.Frame):

    def __init__(self, master, conn):
        """
        Inicializa a janela principal com conexão ao banco e carrega dados iniciais.

        Parâmetros:
            master (tk.Tk): janela raiz do Tkinter.
            conn (sqlite3.Connection): conexão aberta com o banco.
        """
        super().__init__(master)
        self.conn = conn
        self.categorias = lancamentos_repository.listar_categorias(conn)
        self._construir_widgets()
        self._atualizar_listagem()
        self._atualizar_saldo()

    # ------------------------------------------------------------------ #
    # Construção da interface
    # ------------------------------------------------------------------ #

    def _construir_widgets(self):
        """Constrói e posiciona todas as áreas da janela."""
        self._construir_formulario()
        self._construir_saldo()
        self._construir_filtros()
        self._construir_listagem()

    def _construir_formulario(self):
        """Área 1 — formulário de cadastro de lançamento."""
        frame = ttk.LabelFrame(self, text="Novo Lançamento", padding=8)
        frame.pack(fill="x", padx=10, pady=(10, 4))

        ttk.Label(frame, text="Tipo:").grid(row=0, column=0, sticky="w", padx=(0, 4))
        self.combo_tipo = ttk.Combobox(
            frame, values=["Receita", "Despesa"], state="readonly", width=10
        )
        self.combo_tipo.current(0)
        self.combo_tipo.grid(row=0, column=1, sticky="w", padx=(0, 12))

        ttk.Label(frame, text="Valor:").grid(row=0, column=2, sticky="w", padx=(0, 4))
        self.entry_valor = ttk.Entry(frame, width=14)
        self.entry_valor.grid(row=0, column=3, sticky="w", padx=(0, 12))

        ttk.Label(frame, text="Data:").grid(row=0, column=4, sticky="w", padx=(0, 4))
        self.entry_data = ttk.Entry(frame, width=12)
        self.entry_data.insert(0, datetime.date.today().isoformat())
        self.entry_data.grid(row=0, column=5, sticky="w")

        ttk.Label(frame, text="Categoria:").grid(
            row=1, column=0, sticky="w", padx=(0, 4), pady=(6, 0)
        )
        nomes = [c["nome"] for c in self.categorias]
        self.combo_categoria = ttk.Combobox(
            frame, values=nomes, state="readonly", width=16
        )
        if nomes:
            self.combo_categoria.current(0)
        self.combo_categoria.grid(row=1, column=1, sticky="w", padx=(0, 12), pady=(6, 0))

        ttk.Label(frame, text="Descrição:").grid(
            row=1, column=2, sticky="w", padx=(0, 4), pady=(6, 0)
        )
        self.entry_descricao = ttk.Entry(frame, width=30)
        self.entry_descricao.grid(
            row=1, column=3, columnspan=2, sticky="ew", padx=(0, 12), pady=(6, 0)
        )

        ttk.Button(frame, text="Salvar", command=self._salvar_lancamento).grid(
            row=1, column=5, sticky="w", pady=(6, 0)
        )

    def _construir_saldo(self):
        """Área 2 — exibição do saldo consolidado."""
        frame = ttk.Frame(self, padding=(10, 6))
        frame.pack(fill="x", padx=10)

        self.label_saldo = ttk.Label(
            frame,
            text="Saldo consolidado: R$ 0,00",
            font=("TkDefaultFont", 11, "bold"),
        )
        self.label_saldo.pack(anchor="w")

    def _construir_filtros(self):
        """Área 3 — filtros de consulta."""
        frame = ttk.LabelFrame(self, text="Filtros", padding=8)
        frame.pack(fill="x", padx=10, pady=4)

        ttk.Label(frame, text="Data início:").grid(row=0, column=0, sticky="w", padx=(0, 4))
        self.entry_filtro_data_inicio = ttk.Entry(frame, width=12)
        self.entry_filtro_data_inicio.grid(row=0, column=1, sticky="w", padx=(0, 12))

        ttk.Label(frame, text="Data fim:").grid(row=0, column=2, sticky="w", padx=(0, 4))
        self.entry_filtro_data_fim = ttk.Entry(frame, width=12)
        self.entry_filtro_data_fim.grid(row=0, column=3, sticky="w", padx=(0, 12))

        ttk.Label(frame, text="Categoria:").grid(row=0, column=4, sticky="w", padx=(0, 4))
        nomes_com_todas = ["Todas"] + [c["nome"] for c in self.categorias]
        self.combo_filtro_categoria = ttk.Combobox(
            frame, values=nomes_com_todas, state="readonly", width=14
        )
        self.combo_filtro_categoria.current(0)
        self.combo_filtro_categoria.grid(row=0, column=5, sticky="w", padx=(0, 12))

        ttk.Label(frame, text="Tipo:").grid(row=0, column=6, sticky="w", padx=(0, 4))
        self.combo_filtro_tipo = ttk.Combobox(
            frame, values=["Todos", "Receita", "Despesa"], state="readonly", width=10
        )
        self.combo_filtro_tipo.current(0)
        self.combo_filtro_tipo.grid(row=0, column=7, sticky="w", padx=(0, 12))

        ttk.Button(frame, text="Filtrar", command=self._aplicar_filtros).grid(
            row=0, column=8, sticky="w", padx=(0, 6)
        )
        ttk.Button(frame, text="Limpar Filtros", command=self._limpar_filtros).grid(
            row=0, column=9, sticky="w"
        )

    def _construir_listagem(self):
        """Área 4 — Treeview com a listagem de lançamentos."""
        frame = ttk.LabelFrame(self, text="Lançamentos", padding=8)
        frame.pack(fill="both", expand=True, padx=10, pady=(4, 10))

        colunas = ("data", "tipo", "categoria", "valor", "descricao")
        self.tree = ttk.Treeview(frame, columns=colunas, show="headings", height=14)

        self.tree.heading("data", text="Data")
        self.tree.heading("tipo", text="Tipo")
        self.tree.heading("categoria", text="Categoria")
        self.tree.heading("valor", text="Valor")
        self.tree.heading("descricao", text="Descrição")

        self.tree.column("data", width=90, anchor="center")
        self.tree.column("tipo", width=80, anchor="center")
        self.tree.column("categoria", width=130, anchor="w")
        self.tree.column("valor", width=110, anchor="e")
        self.tree.column("descricao", width=280, anchor="w")

        self.tree.tag_configure("receita", foreground="#1a6e1a")
        self.tree.tag_configure("despesa", foreground="#b22222")

        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    # ------------------------------------------------------------------ #
    # Ações dos botões
    # ------------------------------------------------------------------ #

    def _salvar_lancamento(self):
        """Lê o formulário, chama o serviço de registro e atualiza a interface."""
        tipo = self.combo_tipo.get().lower()
        valor = self.entry_valor.get().strip()
        data_lancamento = self.entry_data.get().strip()
        nome_categoria = self.combo_categoria.get()
        descricao = self.entry_descricao.get().strip() or None

        categoria_id = self._id_categoria_por_nome(nome_categoria)
        if categoria_id is None:
            messagebox.showerror("Erro", "Selecione uma categoria válida.")
            return

        try:
            lancamentos_service.registrar_lancamento(
                self.conn, tipo, valor, data_lancamento, categoria_id, descricao
            )
        except ValueError as erro:
            messagebox.showerror("Erro de validação", str(erro))
            return

        self._limpar_formulario()
        self._atualizar_listagem()
        self._atualizar_saldo()

    def _aplicar_filtros(self):
        """Lê os campos de filtro e recarrega a listagem filtrada."""
        data_inicio = self.entry_filtro_data_inicio.get().strip() or None
        data_fim = self.entry_filtro_data_fim.get().strip() or None

        nome_cat = self.combo_filtro_categoria.get()
        categoria_id = (
            self._id_categoria_por_nome(nome_cat) if nome_cat != "Todas" else None
        )

        tipo_selecionado = self.combo_filtro_tipo.get()
        tipo = tipo_selecionado.lower() if tipo_selecionado != "Todos" else None

        lancamentos = lancamentos_repository.listar_lancamentos(
            self.conn,
            tipo=tipo,
            categoria_id=categoria_id,
            data_inicio=data_inicio,
            data_fim=data_fim,
        )
        self._preencher_treeview(lancamentos)

    def _limpar_filtros(self):
        """Limpa os campos de filtro e restaura a listagem completa."""
        self.entry_filtro_data_inicio.delete(0, "end")
        self.entry_filtro_data_fim.delete(0, "end")
        self.combo_filtro_categoria.current(0)
        self.combo_filtro_tipo.current(0)
        self._atualizar_listagem()

    # ------------------------------------------------------------------ #
    # Métodos auxiliares
    # ------------------------------------------------------------------ #

    def _atualizar_listagem(self):
        """Recarrega o Treeview com todos os lançamentos, sem filtro."""
        lancamentos = lancamentos_repository.listar_lancamentos(self.conn)
        self._preencher_treeview(lancamentos)

    def _atualizar_saldo(self):
        """Recalcula e exibe o saldo consolidado atualizado."""
        saldo = saldo_service.obter_saldo(self.conn)
        self.label_saldo.config(
            text=f"Saldo consolidado: {saldo_service.formatar_saldo(saldo)}"
        )

    def _preencher_treeview(self, lancamentos):
        """
        Substitui o conteúdo do Treeview pela lista de lançamentos informada.

        Parâmetros:
            lancamentos (list[dict]): lista retornada pelo repositório.
        """
        for item in self.tree.get_children():
            self.tree.delete(item)

        for lancamento in lancamentos:
            valor_formatado = saldo_service.formatar_saldo(lancamento["valor"])
            self.tree.insert(
                "",
                "end",
                values=(
                    lancamento["data_lancamento"],
                    lancamento["tipo"].capitalize(),
                    lancamento["nome_categoria"],
                    valor_formatado,
                    lancamento["descricao"] or "",
                ),
                tags=(lancamento["tipo"],),
            )

    def _limpar_formulario(self):
        """Restaura os campos do formulário ao estado inicial após cadastro."""
        self.combo_tipo.current(0)
        self.entry_valor.delete(0, "end")
        self.entry_data.delete(0, "end")
        self.entry_data.insert(0, datetime.date.today().isoformat())
        if self.categorias:
            self.combo_categoria.current(0)
        self.entry_descricao.delete(0, "end")

    def _id_categoria_por_nome(self, nome):
        """
        Busca o id de uma categoria pelo nome.

        Parâmetros:
            nome (str): nome da categoria buscada.

        Retorno:
            int | None: id da categoria, ou None se não encontrada.
        """
        for cat in self.categorias:
            if cat["nome"] == nome:
                return cat["id"]
        return None

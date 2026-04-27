"""
main.py — Ponto de entrada da aplicação.

Responsabilidade exclusiva: inicializar o banco, abrir a conexão e
exibir a janela principal. Autorizado a importar database e ui.
"""

import tkinter as tk
import tkinter.messagebox as messagebox

from database import initialize_db, get_connection
from ui.main_window import MainWindow


def main():
    """Inicializa o banco, abre a janela principal e inicia o loop de eventos."""
    try:
        initialize_db()
        conn = get_connection()
        root = tk.Tk()
        root.title("Gerenciador de Finanças Pessoal")
        root.minsize(800, 540)
        app = MainWindow(root, conn)
        app.pack(fill="both", expand=True)
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Erro de inicialização", str(e))
        raise


if __name__ == "__main__":
    main()

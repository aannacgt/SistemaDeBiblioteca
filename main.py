# Importação da classe TelaLogin do módulo de interface login
from src.interface.login import TelaLogin

# Importação da classe TelaInicial do módulo de interface telainicial
from src.interface.telainicial import TelaInicial

# Importação da biblioteca Tkinter para criar a interface gráfica
import tkinter as tk

# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    # Criação da janela principal da aplicação, que será a base para a interface gráfica
    root = tk.Tk()
    # Instancia a classe TelaInicial, passando a janela principal 'root' como parâmetro.
    # Aqui, a interface da tela inicial será configurada na janela 'root'.
    TelaInicial(root)
    # Inicia o loop de eventos do Tkinter, mantendo a janela aberta e aguardando interações do usuário.
    root.mainloop()

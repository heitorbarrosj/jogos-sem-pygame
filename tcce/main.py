import tkinter as tk
import os

def abrir_jogo(jogo):
    try:
        os.system(f"python {jogo}.py")
    except:
        print(f"Erro ao iniciar o jogo {jogo}.")

root = tk.Tk()
root.title("Escolha seu Jogo")

label = tk.Label(root, text="Escolha qual jogo deseja jogar:")
label.pack(pady=10)

btn_cobrinha = tk.Button(root, text="Cobrinha", command=lambda: abrir_jogo("cobrinha"))
btn_cobrinha.pack(pady=10)

btn_ping_pong = tk.Button(root, text="Ping Pong", command=lambda: abrir_jogo("ping_pong"))
btn_ping_pong.pack(pady=10)

root.mainloop()
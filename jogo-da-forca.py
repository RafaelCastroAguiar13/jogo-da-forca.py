from tkinter import *
from tkinter import messagebox
from random import choice

def carregar_palavras():
    with open("palavras.txt", "r", encoding="utf-8") as f:
        return [linha.strip().lower() for linha in f.readlines()]

def nova_partida():
    global palavra, oculto, tentativas, letras_erradas
    palavra = choice(palavras)
    oculto = ["_" for _ in palavra]
    tentativas = 0
    letras_erradas = []
    atualizar_tela()

def verificar(letra):
    global tentativas
    letra = letra.lower()
    if not letra or len(letra) > 1 or not letra.isalpha():
        return

    if letra in palavra:
        for i, l in enumerate(palavra):
            if l == letra:
                oculto[i] = letra
    elif letra not in letras_erradas:
        tentativas += 1
        letras_erradas.append(letra)
    atualizar_tela()

def atualizar_tela():
    oculto_label.config(text=" ".join(oculto))

    forca_text.config(state="normal")
    forca_text.delete("1.0", END)
    forca_text.insert(END, desenhos[min(tentativas, 7)])
    forca_text.config(state="disabled")

    letras_erradas_label.config(text="Erros: " + " ".join(letras_erradas))

    if "_" not in oculto:
        messagebox.showinfo("Vitória!", f"Parabéns! A palavra era: {palavra}")
        nova_partida()
    elif tentativas == 8:
        messagebox.showinfo("Derrota", f"Você perdeu! A palavra era: {palavra}")
        nova_partida()

# Interface
app = Tk()
app.title("Forca")
app.configure(bg="white")
app.geometry("400x500")

# Desenho forca
forca_text = Text(app, bg="white", font=("Courier", 14), height=10, width=20, bd=0)
forca_text.place(x=100, y=10)
forca_text.config(state="disabled")

# Palavra oculta
oculto_label = Label(app, text="", font=("Courier", 24), bg="white")
oculto_label.place(x=50, y=250)

# Letras erradas
letras_erradas_label = Label(app, text="", font=("Arial", 14), bg="white", fg="red")
letras_erradas_label.place(x=50, y=300)

# Campo letra
entrada = Entry(app, font=("Arial", 20), width=2, justify="center")
entrada.place(x=170, y=350)

# Botão jogar
Button(app, text="Jogar", command=lambda: (verificar(entrada.get()), entrada.delete(0, END)),
       font=("Arial", 14), bg="#ddd").place(x=160, y=400)

# Dados do jogo
palavras = carregar_palavras()
tentativas = 0
letras_erradas = []
desenhos = [
    "  _______\n |/      |\n |\n |\n |\n |\n_|___\n",
    "  _______\n |/      |\n |      (_)\n |\n |\n |\n_|___\n",
    "  _______\n |/      |\n |      (_)\n |       |\n |\n |\n_|___\n",
    "  _______\n |/      |\n |      (_)\n |      \\|\n |\n |\n_|___\n",
    "  _______\n |/      |\n |      (_)\n |      \\|/\n |\n |\n_|___\n",
    "  _______\n |/      |\n |      (_)\n |      \\|/\n |       |\n |\n_|___\n",
    "  _______\n |/      |\n |      (_)\n |      \\|/\n |       |\n |      /\n_|___\n",
    "  _______\n |/      |\n |      (_)\n |      \\|/\n |       |\n |      / \\\n_|___\n"
]

nova_partida()
app.mainloop()

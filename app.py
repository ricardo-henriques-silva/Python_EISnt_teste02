import tkinter as tk
from tkinter import simpledialog,messagebox
import random

class SimuladorFutebol(tk.Tk):

    # Inicialização da janela da APP
    def __init__(self):
        super().__init__()
        self.title("Simulador de Equipa")

    # Inicialização do nome da equipa
        self.nome_equipa = tk.StringVar()
        self.nome_equipa.set("Minha Equipa")

    # Inicialização do saldo
        self.saldo = tk.IntVar()
        self.saldo.set(1000)

    # Inicialização da formação táctica
        formacao_tactica_arr = ['4-3-3', '4-4-2', '3-5-2', '3-4-3', '4-5-1', '5-3-2', '4-1-4-1', '4-2-4']
        self.formacao_tactica = tk.StringVar()
        self.formacao_tactica.set('4-3-3')

    # Inicialização dos pontos no arranque da época
        self.pontos=0

    # Definição do dicionário equipa
        self.equipa = {"nome": self.nome_equipa, "jogadores": [], "saldo": self.saldo, "formacao_tactica": self.formacao_tactica, "pontos": self.pontos }
        print(self.equipa)
        
    # Labels das variáveis da equipa
        self.labelnome = tk.Label(self, textvariable=self.nome_equipa).pack()
        self.labelsaldo = tk.Label(self, textvariable=str(self.saldo)).pack()
        self.labeltactica = tk.Label(self, textvariable=self.formacao_tactica).pack()

    # Botões de configuração das variáveia da equipa
        tk.Button(self, text="Alterar nome da equipa", command=self.alterar_nome_equipa).pack()
        tk.Button(self, text="Alterar táctica da equipa", command=lambda: self.alterar_tactica_equipa(formacao_tactica_arr)).pack()
        
    # Botão de avanço para a próxima jornada  
        tk.Button(self, text="Simular Jogo", command=lambda: self.simular_jogo()).pack()

    # Função de configuração do nome da equipa
    def alterar_nome_equipa(self):
        novo_nome = simpledialog.askstring('Alterar Valor', 'Escolha o novo nome da equipa:')
        if novo_nome:
            self.nome_equipa.set(novo_nome)
            print(self.equipa)

    # Função de escolha de formação táctica
    def alterar_tactica_equipa(self,formacao_tactica_arr):
        messagebox.showinfo('Tácticas disponíveis', f'As tácticas disponíveis são:\n{formacao_tactica_arr}')
        nova_tactica = simpledialog.askstring('Alterar táctica', 'Escolha uma das tácticas disponíveis:')
        if nova_tactica:
            self.formacao_tactica.set(nova_tactica)
            print(self.equipa)
    
    # Função de simulação de jogo
    def simular_jogo(self):
        resultado = random.choice(['Vitória', 'Derrota', 'Empate'])
        if resultado == 'Vitória':
            self.pontos = self.pontos + 3
        elif resultado == 'Empate':
            self.pontos = self.pontos + 1
        tk.Label(self, text=f"Resultado do jogo: {resultado} | Pontos: {self.pontos}").pack()

if __name__ == '__main__':
    app = SimuladorFutebol()
    app.mainloop()
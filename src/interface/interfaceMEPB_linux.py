from tkinter import *
import ttkbootstrap as tb
import json
from src import Biblioteca
from src.configuracao import Configuracao
from src.tratamento import ErroSoftware
from src.validador import Validador


class InterfaceMEPB_Linux(Validador):
    def __init__(self) -> None:
        self.configuracao = Configuracao()
        
        self.mepb = Biblioteca()
        self.fonte = ('Arial', 13)

        self.janela = self.abrir_janela_linux()

        self.frame_janela = tb.Frame(self.janela, bootstyle='default')
        self.logo = self.carregar_imagem(self.frame_janela, self.configuracao.imagens + 'logo.png', 6)
        self.igreja = self.igreja_linux(self.frame_janela)
        self.menu_biblioteca = tb.Menubutton(self.frame_janela, text='Menu')
        self.frame_funcao = tb.Labelframe(self.frame_janela)
        self.menu_button_biblioteca()
        self.principal()

        self.logo.grid(row=0, column=0, padx=50, pady=10, sticky='w')
        self.igreja.grid(row=0, column=1)
        self.menu_biblioteca.grid(row=1, column=0, sticky='n', ipadx=5, ipady=5)
        self.frame_funcao.grid(row=1, column=1)

        self.label_aux1 = tb.Label(self.frame_janela, text='   ')
        self.label_aux2 = tb.Label(self.frame_janela, text='   ')
        self.label_aux1.grid(row=2, column=1, pady=10)
        self.label_aux2.grid(row=2, column=2, ipadx=10, ipady=10, padx=10)

        self.frame_janela.pack()
        self.fechar_janela()

    def menu_button_biblioteca(self):
        inside_menu = tb.Menu(self.menu_biblioteca)

        option_menu = StringVar()
        for opcao in ['Principal', 'Cadastro', 'Aluguel', 'Pesquisar Livro', 'Pesquisar Aluguel', 'Mostrar Livros', 'Mostrar Alugados', 'Gasto Total', 'Administrador']:
            inside_menu.add_radiobutton(label=opcao, variable=option_menu, command=lambda option=opcao: self.menu_selecionado(option))

        self.menu_biblioteca['menu'] = inside_menu

    def menu_selecionado(self, option_selected):
        if option_selected == 'Principal':
            self.principal()
        elif option_selected == 'Cadastro':
            self.cadastro()
        elif option_selected == 'Aluguel':
            self.aluguel()
        elif option_selected == 'Pesquisar Livro':
            self.pesquisar_livro()
        elif option_selected == 'Pesquisar Aluguel':
            self.pesquisar_aluguel()
        elif option_selected == 'Mostrar Livros':
            self.mostrar_livros()
        elif option_selected == 'Mostrar Alugados':
            self.mostrar_alugados()
        elif option_selected == 'Gasto Total':
            self.gasto_total()
        elif option_selected == 'Administrador':
            self.administrador()
    
    @staticmethod
    def igreja_linux(frame):
        label_igreja_linux = tb.Label(frame,
            anchor='n',
            compound='bottom',
            font='{Z003} 30 {}',
            relief='flat',
            state='normal',
            text='Missão  Evangélica Pentecostal do Brasil - Itambé'
        )
        return label_igreja_linux
    
    def abrir_janela_linux(self):
        janela = tb.Window(themename='journal')
        janela.title('Biblioteca')
        icon = PhotoImage(file=self.configuracao.imagens + 'logo.png')
        janela.iconphoto(True, icon)
        # width= janela.winfo_screenwidth()
        # height= janela.winfo_screenheight()
        janela.geometry("%dx%d" % (1000, 520))
        janela.resizable(False, False)
        return janela

    def fechar_janela(self):
        self.janela.mainloop()

    @staticmethod
    def carregar_imagem(frame, nome_imagem, tamanho):
        imagem = PhotoImage(file=nome_imagem)
        imagem = imagem.subsample(tamanho,tamanho)
        label_imagem = tb.Label(frame, image=imagem)
        label_imagem.imagem = imagem
        return label_imagem

    def saida_texto(self, texto, janela, height, width, column, row, sticky):
        saida = tb.Text(janela, height=height, width=width, font=self.fonte, state='disabled')
        saida.configure(state='normal')
        saida.delete('1.0', 'end')
        saida.insert('1.0', texto)
        saida.configure(state='disabled')
        saida.grid(column=column, row=row, sticky=sticky, padx=0, pady=3)

    def saida_scrolled_text(self, texto, janela, height, width, column, row, sticky, padx, pady):
        saida = tb.ScrolledText(janela, wrap=WORD, height=height, width=width, font=self.fonte, state='disabled')
        saida.configure(state='normal')
        saida.delete('1.0', 'end')
        saida.insert('1.0', texto)
        saida.configure(state='disabled')
        saida.grid(column=column, row=row, sticky=sticky, padx=padx, pady=pady)

    def mensagem_status_saida(self, mensagem_sucesso, erro_processo, janela, column, row, sticky, ipadx):
        mensagem = mensagem_sucesso if (not erro_processo) else 'Erro'
        ipadx_erro = 34

        if mensagem_sucesso[:5] == 'Senha' and erro_processo:
            mensagem = 'Senha incorreta'
            ipadx_erro = 0

        if erro_processo:
            status = tb.Label(janela, text=mensagem, font=self.fonte, bootstyle="inverse-primary")
            status.grid(column=column, row=row, sticky=sticky, ipadx=ipadx_erro, ipady=5)
        else:
            status = tb.Label(janela, text=mensagem, font=self.fonte, bootstyle="inverse-success")
            status.grid(column=column, row=row, sticky=sticky, ipadx=ipadx, ipady=5)

    def acao_cadastrar(self, event):
        nome, autor, editora, paginas, genero, preco, janela = event

        erro_processo = False
        try:
            informacoes_livro = [
                nome.get(),
                autor.get(),
                editora.get(),
                int(paginas.get()),
                genero.get(),
                float(preco.get())
            ]
            
            self.mepb.app_cadastrar_livro_biblioteca(informacoes_livro)
        except Exception as erro:
            erro_processo = True
            ErroSoftware(erro)

        self.mensagem_status_saida('Cadastrado', erro_processo, janela, column=1, row=6, sticky='e', ipadx=8)

    def acao_remover(self, event):
        codigo, janela = event

        erro_processo = False
        try:
            self.mepb.app_remover_livro_biblioteca(int(codigo.get()))
        except Exception as erro:
            erro_processo = True
            ErroSoftware(erro)

        self.mensagem_status_saida('Removido', erro_processo, janela, column=3, row=1, sticky='e', ipadx=14)

    def acao_alugar(self, event):
        codigo, nome, janela = event

        erro_processo = False
        try:
            informacoes_aluguel = [int(codigo.get()), nome.get()]
            self.mepb.app_alugar_livro_biblioteca(informacoes_aluguel)
        except Exception as erro:
            erro_processo = True
            ErroSoftware(erro)

        self.mensagem_status_saida('Alugado', erro_processo, janela, column=1, row=2, sticky='e', ipadx=21)

    def acao_devolver(self, event):
        codigo, janela = event

        erro_processo = False
        try:
            self.mepb.app_devolucao_livro_biblioteca(codigo_livro=int(codigo.get()))
        except Exception as erro:
            erro_processo = True
            ErroSoftware(erro)

        self.mensagem_status_saida('Devolvido', erro_processo, janela, column=3, row=1, sticky='e', ipadx=15)

    def acao_pesquisar_livro(self, event):
        pesquisa, janela, tipo_janela, titulo = event

        informacoes = ''
        try:
            if tipo_janela == 'disponibilidade':
                informacoes = self.mepb.app_pesquisar_livro_biblioteca(pesquisa=pesquisa, tipo_pesquisa=tipo_janela)
            else:
                if type(pesquisa.get()) == str and pesquisa.get() == '':
                    raise ErroSoftware('Nada pesquisado!')

                informacoes = self.mepb.app_pesquisar_livro_biblioteca(pesquisa=pesquisa.get(), tipo_pesquisa=tipo_janela)
        except Exception as erro:
            ErroSoftware(erro)

        self.janela_pesquisar_livro(janela, informacoes, tipo_janela, titulo)

    def acao_pesquisar_aluguel(self, event):
        pesquisa, janela, tipo_janela, titulo = event

        informacoes = ''
        try:
            informacoes = self.mepb.app_pesquisar_aluguel_biblioteca(pesquisa=pesquisa.get(), tipo_pesquisa=tipo_janela)
        except Exception as erro:
            ErroSoftware(erro)

        self.janela_pesquisar_aluguel(janela, informacoes, tipo_janela, titulo)

    def acao_mostrar_livros(self, _):
        informacoes = self.mepb.app_mostrar_livros_biblioteca()
        self.saida_scrolled_text(texto=informacoes, janela=self.frame_funcao, height=15, width=64, column=1, row=0,
                                 sticky='nw', padx=0, pady=3)

    def acao_mostrar_alugados(self, _):
        try:
            informacoes = self.mepb.app_mostrar_alugados_biblioteca()
            self.saida_scrolled_text(texto=informacoes, janela=self.frame_funcao, height=15, width=64, column=1, row=0,
                                     sticky='nw', padx=0, pady=3)
        except Exception as erro:
            ErroSoftware(erro)

    def acao_gasto_total(self, _):
        try:
            gasto = self.mepb.app_gasto_total_livros()
            self.saida_texto(texto=gasto, janela=self.frame_funcao, height=1, width=10, column=1, row=0, sticky='nw')
        except Exception as erro:
            ErroSoftware(erro)

    def acao_administrador(self, event):
        senha, janela = event

        erro_processo = False
        try:
            self.mepb.app_validar_entrada(senha=senha.get())
        except Exception as erro:
            erro_processo = True
            ErroSoftware(erro)

        self.mensagem_status_saida('Senha correta', erro_processo, janela, column=3, row=1, sticky='e', ipadx=7)

    def principal(self):
        self.frame_funcao.destroy()
        self.frame_funcao = tb.Labelframe(self.frame_janela)
        self.frame_funcao.config(text='Principal')

        imagem_membros = self.carregar_imagem(self.frame_funcao, self.configuracao.imagens + 'membros.png', 2)

        nome_arquivo = self.configuracao.info + 'historia.json'
        informacoes = ''

        with open(nome_arquivo) as f:
            json_arquivo = json.load(f)

        with open(nome_arquivo, 'r'):
            for info in json_arquivo['historia']:
                informacoes += info

        self.saida_scrolled_text(texto=informacoes, janela=self.frame_funcao, height=9, width=74, column=0, row=1,
                                 sticky='nw', padx=10, pady=3)

        imagem_membros.grid(column=0, row=0)
        self.frame_funcao.grid(row=1, column=1, sticky='nw', ipadx=0, ipady=10)

    def criar_label(self, janela, text_label):
        return tb.Label(janela, text=text_label, font=self.fonte), tb.Entry(janela, font=self.fonte)

    @staticmethod
    def criar_botao(janela, text_botao, comando, texto_comando):
        return tb.Button(janela, text=text_botao, bootstyle='info', command=lambda: comando(texto_comando))

    def janela_cadastrar(self, notebook_cadastro):
        janela_adicionar = tb.Frame(notebook_cadastro)
        nome_label, nome_entry = self.criar_label(janela_adicionar, 'Nome:    ')
        autor_label, autor_entry = self.criar_label(janela_adicionar, 'Autor:    ')
        editora_label, editora_entry = self.criar_label(janela_adicionar, 'Editora:    ')
        paginas_label, paginas_entry = self.criar_label(janela_adicionar, 'Páginas:    ')
        genero_label, genero_entry = self.criar_label(janela_adicionar, 'Gênero:    ')
        preco_label, preco_entry = self.criar_label(janela_adicionar, 'Preço:    ')
        info_cadastro = (nome_entry, autor_entry, editora_entry, paginas_entry, genero_entry, preco_entry, janela_adicionar)
        cadastrar_button = self.criar_botao(janela_adicionar, 'Adicionar', self.acao_cadastrar, info_cadastro)
        self.saida_texto(texto='', janela=janela_adicionar, height=1, width=10, column=1, row=6, sticky='e')
        nome_label.grid(column=0, row=0, sticky='nw', pady=10)
        nome_entry.grid(column=1, row=0, ipadx=100, sticky='nw')
        autor_label.grid(column=0, row=1, sticky='nw', pady=10)
        autor_entry.grid(column=1, row=1, ipadx=100, sticky='nw')
        editora_label.grid(column=0, row=2, sticky='nw', pady=10)
        editora_entry.grid(column=1, row=2, ipadx=100, sticky='nw')
        paginas_label.grid(column=0, row=3, sticky='nw', pady=10)
        paginas_entry.grid(column=1, row=3, sticky='nw')
        genero_label.grid(column=0, row=4, sticky='nw', pady=10)
        genero_entry.grid(column=1, row=4, ipadx=100, sticky='nw')
        preco_label.grid(column=0, row=5, sticky='nw', pady=10)
        preco_entry.grid(column=1, row=5, sticky='nw')
        cadastrar_button.grid(column=1, row=6, sticky='nw', pady=10)
        notebook_cadastro.add(janela_adicionar, text='Adicionar')

    def janela_remover(self, notebook_cadastro):
        janela_remover = tb.Frame(notebook_cadastro)
        codigo_livro_label, codigo_livro_texto = self.criar_label(janela_remover, 'Código do livro:    ')
        remover = (codigo_livro_texto, janela_remover)
        remover_button = self.criar_botao(janela_remover, 'Remover', self.acao_remover, remover)
        self.saida_texto(texto='', janela=janela_remover, height=1, width=10, column=3, row=1, sticky='e')
        codigo_livro_label.grid(column=0, row=0, sticky='nw', pady=10)
        codigo_livro_texto.grid(column=1, row=0, sticky='nw')
        remover_button.grid(column=1, row=1, sticky='nw', pady=10)
        notebook_cadastro.add(janela_remover, text='Remover')

    def cadastro(self):
        self.frame_funcao.destroy()
        self.frame_funcao = tb.Labelframe(self.frame_janela)
        self.frame_funcao.config(text='Cadastro')

        notebook_cadastro = tb.Notebook(self.frame_funcao, bootstyle='dark')
        notebook_cadastro.pack(padx=20)

        self.janela_cadastrar(notebook_cadastro)
        self.janela_remover(notebook_cadastro)

        self.frame_funcao.grid(row=1, column=1, ipadx=95, ipady=10, sticky='nw')

    def janela_alugar(self, notebook_aluguel):
        janela_alugar = tb.Frame(notebook_aluguel)
        codigo_livro_label, codigo_livro_entry = self.criar_label(janela_alugar, 'Código do livro:    ')
        nome_pessoa_label, nome_entry = self.criar_label(janela_alugar, 'Nome completo:    ')
        alugar = (codigo_livro_entry, nome_entry, janela_alugar)
        alugar_button = self.criar_botao(janela_alugar, 'Alugar', self.acao_alugar, alugar)
        self.saida_texto(texto='', janela=janela_alugar, height=1, width=10, column=1, row=2, sticky='e')
        codigo_livro_label.grid(column=0, row=0, sticky='nw', pady=10)
        codigo_livro_entry.grid(column=1, row=0, sticky='nw')
        nome_pessoa_label.grid(column=0, row=1, sticky='nw')
        nome_entry.grid(column=1, row=1, ipadx=100, sticky='nw')
        alugar_button.grid(column=1, row=2, sticky='nw', pady=10)
        notebook_aluguel.add(janela_alugar, text='Alugar')

    def janela_devolver(self, notebook_aluguel):
        janela_devolver = tb.Frame(notebook_aluguel)
        codigo_livro_label, codigo_livro_entry = self.criar_label(janela_devolver, 'Código do livro:    ')
        devolver = (codigo_livro_entry, janela_devolver)
        devolver_button = self.criar_botao(janela_devolver, 'Devolver', self.acao_devolver, devolver)
        self.saida_texto(texto='', janela=janela_devolver, height=1, width=10, column=3, row=1, sticky='e')
        codigo_livro_label.grid(column=0, row=0, sticky='nw', pady=10)
        codigo_livro_entry.grid(column=1, row=0, sticky='nw')
        devolver_button.grid(column=1, row=1, sticky='nw', pady=10)
        notebook_aluguel.add(janela_devolver, text='Devolver')

    def aluguel(self):
        self.frame_funcao.destroy()
        self.frame_funcao = tb.Labelframe(self.frame_janela)
        self.frame_funcao.config(text='Aluguel')

        notebook_aluguel = tb.Notebook(self.frame_funcao, bootstyle='dark')
        notebook_aluguel.pack(padx=20)

        self.janela_alugar(notebook_aluguel)
        self.janela_devolver(notebook_aluguel)

        self.frame_funcao.grid(row=1, column=1, ipadx=68, ipady=101, sticky='nw')

    def janela_pesquisar_livro(self, janela, texto_saida, tipo_janela, titulo):
        if tipo_janela == 'disponibilidade':
            label = tb.Label(janela, text='Disponibilidade:', font=self.fonte)
            botao_disponivel = self.criar_botao(janela, 'Disponível', self.acao_pesquisar_livro,
                                               ('Disponível', janela, tipo_janela, titulo))
            botao_indisponivel = self.criar_botao(janela, 'Indisponível', self.acao_pesquisar_livro,
                                                 ('Indisponível', janela, tipo_janela, titulo))
            self.saida_scrolled_text(texto=texto_saida, janela=janela, height=12, width=50, column=1, row=1, sticky='nw',
                                     padx=0, pady=0)

            label.grid(column=0, row=0, sticky='nw', pady=10)
            botao_disponivel.grid(column=1, row=0, sticky='w')
            botao_indisponivel.grid(column=1, row=0, sticky='w', padx=100)
        else:
            label, entry = self.criar_label(janela, titulo)
            self.saida_scrolled_text(texto=texto_saida, janela=janela, height=10, width=50, column=1, row=1, sticky='nw',
                                     padx=0, pady=0)
            pesquisa = (entry, janela, tipo_janela, titulo)
            button = self.criar_botao(janela, 'Pesquisar', self.acao_pesquisar_livro, pesquisa)
            label.grid(column=0, row=0, sticky='nw', pady=10)
            entry.grid(column=1, row=0, sticky='nw')
            button.grid(column=1, row=2, sticky='nw', pady=10)

    def funcao_frame_pesquisar_livro(self, notebook_pesquisar, nome_janela, tipo_janela):
        janela = tb.Frame(notebook_pesquisar)

        self.janela_pesquisar_livro(janela, '', tipo_janela, nome_janela + ':    ')
        notebook_pesquisar.add(janela, text=nome_janela)

    def pesquisar_livro(self):
        self.frame_funcao.destroy()
        self.frame_funcao = tb.Labelframe(self.frame_janela)
        self.frame_funcao.config(text='Pesquisar Livro')

        notebook_pesquisar = tb.Notebook(self.frame_funcao, bootstyle='dark')
        notebook_pesquisar.pack(padx=20)

        self.funcao_frame_pesquisar_livro(notebook_pesquisar, 'Código', 'codigo')
        self.funcao_frame_pesquisar_livro(notebook_pesquisar, 'Nome', 'nome')
        self.funcao_frame_pesquisar_livro(notebook_pesquisar, 'Autor', 'autor')
        self.funcao_frame_pesquisar_livro(notebook_pesquisar, 'Editora', 'editora')
        self.funcao_frame_pesquisar_livro(notebook_pesquisar, 'Gênero', 'genero')
        self.funcao_frame_pesquisar_livro(notebook_pesquisar, 'Disponibilidade', 'disponibilidade')

        self.frame_funcao.grid(row=1, column=1, ipadx=35, ipady=16, sticky='nw')

    def janela_pesquisar_aluguel(self, janela, texto_saida, tipo_janela, titulo):
        label, entry = self.criar_label(janela, titulo)
        self.saida_scrolled_text(texto=texto_saida, janela=janela, height=10, width=50, column=1, row=1, sticky='nw',
                                 padx=0, pady=0)
        pesquisa = (entry, janela, tipo_janela, titulo)
        button = self.criar_botao(janela, 'Pesquisar', self.acao_pesquisar_aluguel, pesquisa)
        label.grid(column=0, row=0, sticky='nw', pady=10)
        entry.grid(column=1, row=0, ipadx=100, sticky='nw')
        button.grid(column=1, row=2, sticky='nw', pady=10)

    def funcao_frame_pesquisar_aluguel(self, notebook_pesquisar, nome_janela, tipo_janela):
        janela = tb.Frame(notebook_pesquisar)
        self.janela_pesquisar_aluguel(janela, '', tipo_janela, nome_janela + ':    ')
        notebook_pesquisar.add(janela, text=nome_janela)

    def pesquisar_aluguel(self):
        self.frame_funcao.destroy()
        self.frame_funcao = tb.Labelframe(self.frame_janela)
        self.frame_funcao.config(text='Pesquisar Aluguel')

        notebook_pesquisar = tb.Notebook(self.frame_funcao, bootstyle='dark')
        notebook_pesquisar.pack(padx=20)

        self.funcao_frame_pesquisar_aluguel(notebook_pesquisar, 'Nome da pessoa', 'nomePessoa')
        self.funcao_frame_pesquisar_aluguel(notebook_pesquisar, 'Código do livro', 'codigoLivro')
        self.funcao_frame_pesquisar_aluguel(notebook_pesquisar, 'Nome do livro', 'nomeLivro')
        self.funcao_frame_pesquisar_aluguel(notebook_pesquisar, 'Data de aluguel', 'dataAluguel')
        self.funcao_frame_pesquisar_aluguel(notebook_pesquisar, 'Data de entrega', 'dataEntrega')

        self.frame_funcao.grid(row=1, column=1, ipadx=20, ipady=16, sticky='nw')

    def mostrar_livros(self):
        self.frame_funcao.destroy()
        self.frame_funcao = tb.Labelframe(self.frame_janela)
        self.frame_funcao.config(text='Mostrar Livros')

        mostrar_dados_label = tb.Label(self.frame_funcao, text='Dados:    ', font=self.fonte)
        self.saida_scrolled_text(texto='', janela=self.frame_funcao, height=15, width=64, column=1, row=0, sticky='nw',
                                 padx=0, pady=3)
        mostrar_livros_button = self.criar_botao(self.frame_funcao, 'Pesquisar', self.acao_mostrar_livros, 'mostrarLivros')
        mostrar_dados_label.grid(column=0, row=0, sticky='nw', padx=10, pady=10)
        mostrar_livros_button.grid(column=1, row=1, sticky='nw', pady=10)

        self.frame_funcao.grid(row=1, column=1, ipadx=6, ipady=3, sticky='nw')

    def mostrar_alugados(self):
        self.frame_funcao.destroy()
        self.frame_funcao = tb.Labelframe(self.frame_janela)
        self.frame_funcao.config(text='Mostrar Alugados')

        mostrar_dados_label = tb.Label(self.frame_funcao, text='Dados:    ', font=self.fonte)
        self.saida_scrolled_text(texto='', janela=self.frame_funcao, height=15, width=64, column=1, row=0, sticky='nw',
                                 padx=0, pady=3)
        mostrar_alugados_button = self.criar_botao(self.frame_funcao, 'Pesquisar', self.acao_mostrar_alugados,
                                                'mostrarAlugados')
        mostrar_dados_label.grid(column=0, row=0, sticky='nw', padx=10, pady=10)
        mostrar_alugados_button.grid(column=1, row=1, sticky='nw', pady=10)

        self.frame_funcao.grid(row=1, column=1, ipadx=6, ipady=3, sticky='nw')

    def gasto_total(self):
        self.frame_funcao.destroy()
        self.frame_funcao = tb.Labelframe(self.frame_janela)
        self.frame_funcao.config(text='Gasto Total')

        mostrar_dados_label = tb.Label(self.frame_funcao, text='Gasto Total:    ', font=self.fonte)
        self.saida_texto(texto='', janela=self.frame_funcao, height=1, width=10, column=1, row=0, sticky='nw')
        gasto_total_button = self.criar_botao(self.frame_funcao, 'Pesquisar', self.acao_gasto_total, 'gastoTotal')
        mostrar_dados_label.grid(column=0, row=0, sticky='nw', padx=10, pady=10)
        gasto_total_button.grid(column=1, row=1, sticky='nw', pady=10)

        self.frame_funcao.grid(row=1, column=1, ipadx=241, ipady=133, sticky='nw')

    def administrador(self):
        self.frame_funcao.destroy()
        self.frame_funcao = tb.Labelframe(self.frame_janela)
        self.frame_funcao.config(text='Administrador')

        senha_label = tb.Label(self.frame_funcao, text='Senha:    ', font=self.fonte)
        senha_entry = tb.Entry(self.frame_funcao, font=self.fonte, show='*')
        senha = (senha_entry, self.frame_funcao)
        senha_button = self.criar_botao(self.frame_funcao, 'Entrar', self.acao_administrador, senha)
        self.saida_texto(texto='', janela=self.frame_funcao, height=1, width=12, column=3, row=1, sticky='e')

        senha_label.grid(column=0, row=0, sticky='nw', padx=10, pady=10)
        senha_entry.grid(column=1, row=0, sticky='nw', padx=0, pady=3)
        senha_button.grid(column=1, row=1, sticky='nw', pady=10)

        self.frame_funcao.grid(row=1, column=1, ipadx=152, ipady=133, sticky='nw')

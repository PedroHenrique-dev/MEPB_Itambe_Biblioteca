from tkinter import *
import ttkbootstrap as tb
import json
from estrutura import Biblioteca
from estrutura.tratamento import ErroSoftware
from estrutura.gerenciador.validador import Validador
from estrutura.config import Configuracao


class InterfaceMEPB_Linux(Validador):
    def __init__(self) -> None:
        self.configuracao = Configuracao()
        
        self.usuarioAdministrador = False

        self.mepb = Biblioteca()
        self.fonte = ('Arial', 13)

        self.janela = self.abrirJanela_linux()

        self.frameJanela = tb.Frame(self.janela, bootstyle='defalt')
        self.logo = self.carregarImagem(self.frameJanela, self.configuracao.imagens + 'logo.png', 6)
        self.igreja = self.igreja_linux(self.frameJanela)
        self.menuBiblioteca = tb.Menubutton(self.frameJanela, text='Menu')
        self.frameFuncao = tb.Labelframe(self.frameJanela)
        self.menuButtonBiblioteca()
        self.principal()

        self.logo.grid(row=0, column=0, padx=50, pady=10, sticky='w')
        self.igreja.grid(row=0, column=1)
        self.menuBiblioteca.grid(row=1, column=0, sticky='n', ipadx=5, ipady=5)
        self.frameFuncao.grid(row=1, column=1)

        self.labelAux1 = tb.Label(self.frameJanela, text='   ')
        self.labelAux2 = tb.Label(self.frameJanela, text='   ')
        self.labelAux1.grid(row=2, column=1, pady=10)
        self.labelAux2.grid(row=2, column=2, ipadx=10, ipady=10, padx=10)

        self.frameJanela.pack()
        self.fecharJanela()

    def menuButtonBiblioteca(self):
        insideMenu = tb.Menu(self.menuBiblioteca)

        optionMenu = StringVar()
        for option in ['Principal', 'Cadastro', 'Aluguel', 'Pesquisar Livro', 'Pesquisar Aluguel', 'Mostrar Livros', 'Mostrar Alugados', 'Gasto Total', 'Administrador']:
            insideMenu.add_radiobutton(label=option, variable=optionMenu, command=lambda option=option: self.menuSelecionado(option))

        self.menuBiblioteca['menu'] = insideMenu

    def menuSelecionado(self, optionSelected):
        if optionSelected == 'Principal':
            self.principal()
        elif optionSelected == 'Cadastro':
            self.cadastro()
        elif optionSelected == 'Aluguel':
            self.aluguel()
        elif optionSelected == 'Pesquisar Livro':
            self.pesquisarLivro()
        elif optionSelected == 'Pesquisar Aluguel':
            self.pesquisarAluguel()
        elif optionSelected == 'Mostrar Livros':
            self.mostrarLivros()
        elif optionSelected == 'Mostrar Alugados':
            self.mostrarAlugados()
        elif optionSelected == 'Gasto Total':
            self.gastoTotal()
        elif optionSelected == 'Administrador':
            self.administrador()
    
    @staticmethod
    def igreja_linux(frame):
        labelIgreja_linux = tb.Label(frame,
                               anchor='n',
                               compound='bottom',
                               font='{Z003} 30 {}',
                               relief='flat',
                               state='normal',
                               text='Missão  Evangélica Pentecostal do Brasil - Itambé'
                               )
        return labelIgreja_linux
    
    def abrirJanela_linux(self):
        janela = tb.Window(themename='journal')
        janela.title('Biblioteca')
        icon = PhotoImage(file=self.configuracao.imagens + 'logo.png')
        janela.iconphoto(True, icon)
        width= janela.winfo_screenwidth()
        height= janela.winfo_screenheight()
        janela.geometry("%dx%d" % (1000, 520))
        # janela.geometry('953x500')
        # janela.attributes('-fullscreen', True)
        # janela.resizable(False, False)
        return janela

    def fecharJanela(self):
        self.janela.mainloop()

    @staticmethod
    def carregarImagem(frame, nomeImagem, tamanho):
        imagem = PhotoImage(file=nomeImagem)
        imagem = imagem.subsample(tamanho,tamanho)
        labelImagem = tb.Label(frame, image=imagem)
        labelImagem.imagem = imagem
        return labelImagem

    def saidaTexto(self, texto, janela, height, width, column, row, sticky):
        saida = tb.Text(janela, height=height, width=width, font=self.fonte, state='disabled')
        saida.configure(state='normal')
        saida.delete('1.0', 'end')
        saida.insert('1.0', texto)
        saida.configure(state='disabled')
        saida.grid(column=column, row=row, sticky=sticky, padx=0, pady=3)

    def saidaScrolledText(self, texto, janela, height, width, column, row, sticky, padx, pady):
        saida = tb.ScrolledText(janela, wrap=WORD, height=height, width=width, font=self.fonte, state='disabled')
        saida.configure(state='normal')
        saida.delete('1.0', 'end')
        saida.insert('1.0', texto)
        saida.configure(state='disabled')
        saida.grid(column=column, row=row, sticky=sticky, padx=padx, pady=pady)

    def mensagemStatusSaida(self, mensagemSucesso, erroProcesso, janela, column, row, sticky, ipadx):
        mensagem = mensagemSucesso if (not erroProcesso) else 'Erro'
        ipadxErro = 34

        if mensagemSucesso[:5] == 'Senha' and erroProcesso:
            mensagem = 'Senha incorreta'
            ipadxErro = 0

        if erroProcesso:
            status = tb.Label(janela, text=mensagem, font=self.fonte, bootstyle="inverse-primary")
            status.grid(column=column, row=row, sticky=sticky, ipadx=ipadxErro, ipady=5)
        else:
            status = tb.Label(janela, text=mensagem, font=self.fonte, bootstyle="inverse-success")
            status.grid(column=column, row=row, sticky=sticky, ipadx=ipadx, ipady=5)

    def acaoCadastrar(self, event):
        nome, autor, editora, paginas, genero, preco, janela = event

        erroProcesso = False
        try:
            if not self.usuarioAdministrador:
                raise ErroSoftware('Usuário não autorizado!')

            informacoesLivro = (
            nome.get(), autor.get(), editora.get(), int(paginas.get()), genero.get(), float(preco.get()))
            self.mepb.appCadastrarLivroBiblioteca(informacoesLivro)
        except Exception as erro:
            erroProcesso = True

        self.mensagemStatusSaida('Cadastrado', erroProcesso, janela, column=1, row=6, sticky='e', ipadx=8)

    def acaoRemover(self, event):
        codigo, janela = event

        erroProcesso = False
        try:
            if not self.usuarioAdministrador:
                raise ErroSoftware('Usuário não autorizado!')

            self.mepb.appRemoverLivroBiblioteca(int(codigo.get()))
        except Exception as erro:
            erroProcesso = True

        self.mensagemStatusSaida('Removido', erroProcesso, janela, column=3, row=1, sticky='e', ipadx=14)

    def acaoAlugar(self, event):
        codigo, nome, janela = event

        erroProcesso = False
        try:
            informacoesLivro = (int(codigo.get()), nome.get())
            self.mepb.appAlugarLivroBiblioteca(informacoesLivro)
        except Exception as erro:
            erroProcesso = True

        self.mensagemStatusSaida('Alugado', erroProcesso, janela, column=1, row=2, sticky='e', ipadx=21)

    def acaoDevolver(self, event):
        codigo, janela = event

        erroProcesso = False
        try:
            if not self.usuarioAdministrador:
                raise ErroSoftware('Usuário não autorizado!')

            self.mepb.appDevolucaoLivroBiblioteca(int(codigo.get()))
        except Exception as erro:
            erroProcesso = True

        self.mensagemStatusSaida('Devolvido', erroProcesso, janela, column=3, row=1, sticky='e', ipadx=15)

    def acaoPesquisarLivro(self, event):
        pesquisa, janela, tipoJanela, titulo = event

        informacoes = ''
        erroProcesso = False
        try:
            if tipoJanela == 'disponibilidade':
                informacoes = self.mepb.appPesquisarLivroBiblioteca(pesquisa, tipoJanela)
            else:
                if type(pesquisa.get()) == str and pesquisa.get() == '':
                    raise ErroSoftware('Nada pesquisado!')

                informacoes = self.mepb.appPesquisarLivroBiblioteca(pesquisa.get(), tipoJanela)
        except Exception as erro:
            erroProcesso = True

        self.janelaPesquisarLivro(janela, informacoes, tipoJanela, titulo)

    def acaoPesquisarAluguel(self, event):
        pesquisa, janela, tipoJanela, titulo = event

        informacoes = ''
        erroProcesso = False
        try:
            if not self.usuarioAdministrador:
                raise ErroSoftware('Usuário não autorizado!')

            if type(pesquisa.get()) == str and pesquisa.get() == '':
                raise ErroSoftware('Nada pesquisado!')

            informacoes = self.mepb.appPesquisarAluguelBiblioteca(pesquisa.get(), tipoJanela)
        except Exception as erro:
            erroProcesso = True

        self.janelaPesquisarAluguel(janela, informacoes, tipoJanela, titulo)

    def acaoMostrarLivros(self, event):
        informacoes = self.mepb.appMostrarLivrosBiblioteca()
        self.saidaScrolledText(texto=informacoes, janela=self.frameFuncao, height=15, width=64, column=1, row=0,
                               sticky='nw', padx=0, pady=3)

    def acaoMostrarAlugados(self, event):
        erroProcesso = False
        try:
            if not self.usuarioAdministrador:
                raise ErroSoftware('Usuário não autorizado!')

            informacoes = self.mepb.appMostrarAlugadosBiblioteca()
            self.saidaScrolledText(texto=informacoes, janela=self.frameFuncao, height=15, width=64, column=1, row=0,
                                   sticky='nw', padx=0, pady=3)
        except Exception as erro:
            erroProcesso = True

    def acaoGastoTotal(self, event):
        erroProcesso = False
        try:
            if not self.usuarioAdministrador:
                raise ErroSoftware('Usuário não autorizado!')

            gasto = self.mepb.appGastoTotalLivros()
            self.saidaTexto(texto=gasto, janela=self.frameFuncao, height=1, width=10, column=1, row=0, sticky='nw')
        except Exception as erro:
            erroProcesso = True

    def acaoAdministrador(self, event):
        senha, janela = event

        erroProcesso = False
        try:
            self.usuarioAdministrador = self.appValidarEntrada(senha.get())

        except Exception as erro:
            erroProcesso = True

        self.mensagemStatusSaida('Senha correta', erroProcesso, janela, column=3, row=1, sticky='e', ipadx=7)

    def principal(self):
        self.frameFuncao.destroy()
        self.frameFuncao = tb.Labelframe(self.frameJanela)
        self.frameFuncao.config(text='Principal')

        membros = self.carregarImagem(self.frameFuncao, self.configuracao.imagens + 'membros.png', 2)

        nomeArquivo = self.configuracao.info + 'historia.json'
        informacoes = ''

        with open(nomeArquivo) as f:
            jsonArquivo = json.load(f)

        with open(nomeArquivo, 'r') as arquivo:
            for info in jsonArquivo['historia']:
                informacoes += info

        self.saidaScrolledText(texto=informacoes, janela=self.frameFuncao, height=9, width=74, column=0, row=1,
                               sticky='nw', padx=10, pady=3)

        membros.grid(column=0, row=0)
        self.frameFuncao.grid(row=1, column=1, sticky='nw', ipadx=0, ipady=10)

    def criarLabel(self, janela, textLabel):
        return tb.Label(janela, text=textLabel, font=self.fonte), tb.Entry(janela, font=self.fonte)

    @staticmethod
    def criarBotao(janela, textBotao, comando, textoComando):
        return tb.Button(janela, text=textBotao, bootstyle='info', command=lambda: comando(textoComando))

    def janelaCadastrar(self, notebookCadastro):
        janelaAdicionar = tb.Frame(notebookCadastro)
        nomeLabel, nomeEntry = self.criarLabel(janelaAdicionar, 'Nome:    ')
        autorLabel, autorEntry = self.criarLabel(janelaAdicionar, 'Autor:    ')
        editoraLabel, editoraEntry = self.criarLabel(janelaAdicionar, 'Editora:    ')
        paginasLabel, paginasEntry = self.criarLabel(janelaAdicionar, 'Páginas:    ')
        generoLabel, generoEntry = self.criarLabel(janelaAdicionar, 'Gênero:    ')
        precoLabel, precoEntry = self.criarLabel(janelaAdicionar, 'Preço:    ')
        infoCadastro = (nomeEntry, autorEntry, editoraEntry, paginasEntry, generoEntry, precoEntry, janelaAdicionar)
        cadastrarButton = self.criarBotao(janelaAdicionar, 'Adicionar', self.acaoCadastrar, infoCadastro)
        self.saidaTexto(texto='', janela=janelaAdicionar, height=1, width=10, column=1, row=6, sticky='e')
        nomeLabel.grid(column=0, row=0, sticky='nw', pady=10)
        nomeEntry.grid(column=1, row=0, ipadx=100, sticky='nw')
        autorLabel.grid(column=0, row=1, sticky='nw', pady=10)
        autorEntry.grid(column=1, row=1, ipadx=100, sticky='nw')
        editoraLabel.grid(column=0, row=2, sticky='nw', pady=10)
        editoraEntry.grid(column=1, row=2, ipadx=100, sticky='nw')
        paginasLabel.grid(column=0, row=3, sticky='nw', pady=10)
        paginasEntry.grid(column=1, row=3, sticky='nw')
        generoLabel.grid(column=0, row=4, sticky='nw', pady=10)
        generoEntry.grid(column=1, row=4, ipadx=100, sticky='nw')
        precoLabel.grid(column=0, row=5, sticky='nw', pady=10)
        precoEntry.grid(column=1, row=5, sticky='nw')
        cadastrarButton.grid(column=1, row=6, sticky='nw', pady=10)
        notebookCadastro.add(janelaAdicionar, text='Adicionar')

    def janelaRemover(self, notebookCadastro):
        janelaRemover = tb.Frame(notebookCadastro)
        codigoLivroLabel, codigoLivroTexto = self.criarLabel(janelaRemover, 'Código do livro:    ')
        remover = (codigoLivroTexto, janelaRemover)
        removerButton = self.criarBotao(janelaRemover, 'Remover', self.acaoRemover, remover)
        self.saidaTexto(texto='', janela=janelaRemover, height=1, width=10, column=3, row=1, sticky='e')
        codigoLivroLabel.grid(column=0, row=0, sticky='nw', pady=10)
        codigoLivroTexto.grid(column=1, row=0, sticky='nw')
        removerButton.grid(column=1, row=1, sticky='nw', pady=10)
        notebookCadastro.add(janelaRemover, text='Remover')

    def cadastro(self):
        self.frameFuncao.destroy()
        self.frameFuncao = tb.Labelframe(self.frameJanela)
        self.frameFuncao.config(text='Cadastro')

        notebookCadastro = tb.Notebook(self.frameFuncao, bootstyle='dark')
        notebookCadastro.pack(padx=20)

        self.janelaCadastrar(notebookCadastro)
        self.janelaRemover(notebookCadastro)

        self.frameFuncao.grid(row=1, column=1, ipadx=95, ipady=10, sticky='nw')

    def janelaAlugar(self, notebookAluguel):
        janelaAlugar = tb.Frame(notebookAluguel)
        codigoLivroLabel, codigoLivroEntry = self.criarLabel(janelaAlugar, 'Código do livro:    ')
        nomePessoaLabel, nomeEntry = self.criarLabel(janelaAlugar, 'Nome completo:    ')
        alugar = (codigoLivroEntry, nomeEntry, janelaAlugar)
        alugarButton = self.criarBotao(janelaAlugar, 'Alugar', self.acaoAlugar, alugar)
        self.saidaTexto(texto='', janela=janelaAlugar, height=1, width=10, column=1, row=2, sticky='e')
        codigoLivroLabel.grid(column=0, row=0, sticky='nw', pady=10)
        codigoLivroEntry.grid(column=1, row=0, sticky='nw')
        nomePessoaLabel.grid(column=0, row=1, sticky='nw')
        nomeEntry.grid(column=1, row=1, ipadx=100, sticky='nw')
        alugarButton.grid(column=1, row=2, sticky='nw', pady=10)
        notebookAluguel.add(janelaAlugar, text='Alugar')

    def janelaDevolver(self, notebookAluguel):
        janelaDevolver = tb.Frame(notebookAluguel)
        codigoLivroLabel, codigoLivroEntry = self.criarLabel(janelaDevolver, 'Código do livro:    ')
        devolver = (codigoLivroEntry, janelaDevolver)
        devolverButton = self.criarBotao(janelaDevolver, 'Devolver', self.acaoDevolver, devolver)
        self.saidaTexto(texto='', janela=janelaDevolver, height=1, width=10, column=3, row=1, sticky='e')
        codigoLivroLabel.grid(column=0, row=0, sticky='nw', pady=10)
        codigoLivroEntry.grid(column=1, row=0, sticky='nw')
        devolverButton.grid(column=1, row=1, sticky='nw', pady=10)
        notebookAluguel.add(janelaDevolver, text='Devolver')

    def aluguel(self):
        self.frameFuncao.destroy()
        self.frameFuncao = tb.Labelframe(self.frameJanela)
        self.frameFuncao.config(text='Aluguel')

        notebookAluguel = tb.Notebook(self.frameFuncao, bootstyle='dark')
        notebookAluguel.pack(padx=20)

        self.janelaAlugar(notebookAluguel)
        self.janelaDevolver(notebookAluguel)

        self.frameFuncao.grid(row=1, column=1, ipadx=68, ipady=101, sticky='nw')

    def janelaPesquisarLivro(self, janela, textoSaida, tipoJanela, titulo):
        if tipoJanela == 'disponibilidade':
            label = tb.Label(janela, text='Disponibilidade:', font=self.fonte)
            botaoDisponivel = self.criarBotao(janela, 'Disponível', self.acaoPesquisarLivro,
                                              ('Disponível', janela, tipoJanela, titulo))
            botaoIndisponivel = self.criarBotao(janela, 'Indisponível', self.acaoPesquisarLivro,
                                                ('Indisponível', janela, tipoJanela, titulo))
            self.saidaScrolledText(texto=textoSaida, janela=janela, height=12, width=50, column=1, row=1, sticky='nw',
                                   padx=0, pady=0)

            label.grid(column=0, row=0, sticky='nw', pady=10)
            botaoDisponivel.grid(column=1, row=0, sticky='w')
            botaoIndisponivel.grid(column=1, row=0, sticky='w', padx=100)
        else:
            label, entry = self.criarLabel(janela, titulo)
            self.saidaScrolledText(texto=textoSaida, janela=janela, height=10, width=50, column=1, row=1, sticky='nw',
                                   padx=0, pady=0)
            pesquisa = (entry, janela, tipoJanela, titulo)
            button = self.criarBotao(janela, 'Pesquisar', self.acaoPesquisarLivro, pesquisa)
            label.grid(column=0, row=0, sticky='nw', pady=10)
            entry.grid(column=1, row=0, sticky='nw')
            button.grid(column=1, row=2, sticky='nw', pady=10)

    def funcaoFramePesquisarLivro(self, notebookPesquisar, nomeJanela, tipoJanela):
        janela = tb.Frame(notebookPesquisar)

        self.janelaPesquisarLivro(janela, '', tipoJanela, nomeJanela + ':    ')
        notebookPesquisar.add(janela, text=nomeJanela)

    def pesquisarLivro(self):
        self.frameFuncao.destroy()
        self.frameFuncao = tb.Labelframe(self.frameJanela)
        self.frameFuncao.config(text='Pesquisar Livro')

        notebookPesquisar = tb.Notebook(self.frameFuncao, bootstyle='dark')
        notebookPesquisar.pack(padx=20)

        self.funcaoFramePesquisarLivro(notebookPesquisar, 'Código', 'codigo')
        self.funcaoFramePesquisarLivro(notebookPesquisar, 'Nome', 'nome')
        self.funcaoFramePesquisarLivro(notebookPesquisar, 'Autor', 'autor')
        self.funcaoFramePesquisarLivro(notebookPesquisar, 'Editora', 'editora')
        self.funcaoFramePesquisarLivro(notebookPesquisar, 'Gênero', 'genero')
        self.funcaoFramePesquisarLivro(notebookPesquisar, 'Disponibilidade', 'disponibilidade')

        self.frameFuncao.grid(row=1, column=1, ipadx=35, ipady=16, sticky='nw')

    def janelaPesquisarAluguel(self, janela, textoSaida, tipoJanela, titulo):
        label, entry = self.criarLabel(janela, titulo)
        self.saidaScrolledText(texto=textoSaida, janela=janela, height=10, width=50, column=1, row=1, sticky='nw',
                               padx=0, pady=0)
        pesquisa = (entry, janela, tipoJanela, titulo)
        button = self.criarBotao(janela, 'Pesquisar', self.acaoPesquisarAluguel, pesquisa)
        label.grid(column=0, row=0, sticky='nw', pady=10)
        entry.grid(column=1, row=0, ipadx=100, sticky='nw')
        button.grid(column=1, row=2, sticky='nw', pady=10)

    def funcaoFramePesquisarAluguel(self, notebookPesquisar, nomeJanela, tipoJanela):
        janela = tb.Frame(notebookPesquisar)
        self.janelaPesquisarAluguel(janela, '', tipoJanela, nomeJanela + ':    ')
        notebookPesquisar.add(janela, text=nomeJanela)

    def pesquisarAluguel(self):
        self.frameFuncao.destroy()
        self.frameFuncao = tb.Labelframe(self.frameJanela)
        self.frameFuncao.config(text='Pesquisar Aluguel')

        notebookPesquisar = tb.Notebook(self.frameFuncao, bootstyle='dark')
        notebookPesquisar.pack(padx=20)

        self.funcaoFramePesquisarAluguel(notebookPesquisar, 'Nome da pessoa', 'nomePessoa')
        self.funcaoFramePesquisarAluguel(notebookPesquisar, 'Código do livro', 'codigoLivro')
        self.funcaoFramePesquisarAluguel(notebookPesquisar, 'Nome do livro', 'nomeLivro')
        self.funcaoFramePesquisarAluguel(notebookPesquisar, 'Data de aluguel', 'dataAluguel')
        self.funcaoFramePesquisarAluguel(notebookPesquisar, 'Data de entrega', 'dataEntrega')

        self.frameFuncao.grid(row=1, column=1, ipadx=20, ipady=16, sticky='nw')

    def mostrarLivros(self):
        self.frameFuncao.destroy()
        self.frameFuncao = tb.Labelframe(self.frameJanela)
        self.frameFuncao.config(text='Mostrar Livros')

        mostrarDadosLabel = tb.Label(self.frameFuncao, text='Dados:    ', font=self.fonte)
        self.saidaScrolledText(texto='', janela=self.frameFuncao, height=15, width=64, column=1, row=0, sticky='nw',
                               padx=0, pady=3)
        mostrarLivrosButton = self.criarBotao(self.frameFuncao, 'Pesquisar', self.acaoMostrarLivros, 'mostrarLivros')
        mostrarDadosLabel.grid(column=0, row=0, sticky='nw', padx=10, pady=10)
        mostrarLivrosButton.grid(column=1, row=1, sticky='nw', pady=10)

        self.frameFuncao.grid(row=1, column=1, ipadx=6, ipady=3, sticky='nw')

    def mostrarAlugados(self):
        self.frameFuncao.destroy()
        self.frameFuncao = tb.Labelframe(self.frameJanela)
        self.frameFuncao.config(text='Mostrar Alugados')

        mostrarDadosLabel = tb.Label(self.frameFuncao, text='Dados:    ', font=self.fonte)
        self.saidaScrolledText(texto='', janela=self.frameFuncao, height=15, width=64, column=1, row=0, sticky='nw',
                               padx=0, pady=3)
        mostrarAlugadosButton = self.criarBotao(self.frameFuncao, 'Pesquisar', self.acaoMostrarAlugados,
                                                'mostrarAlugados')
        mostrarDadosLabel.grid(column=0, row=0, sticky='nw', padx=10, pady=10)
        mostrarAlugadosButton.grid(column=1, row=1, sticky='nw', pady=10)

        self.frameFuncao.grid(row=1, column=1, ipadx=6, ipady=3, sticky='nw')

    def gastoTotal(self):
        self.frameFuncao.destroy()
        self.frameFuncao = tb.Labelframe(self.frameJanela)
        self.frameFuncao.config(text='Gasto Total')

        mostrarDadosLabel = tb.Label(self.frameFuncao, text='Gasto Total:    ', font=self.fonte)
        self.saidaTexto(texto='', janela=self.frameFuncao, height=1, width=10, column=1, row=0, sticky='nw')
        gastoTotalButton = self.criarBotao(self.frameFuncao, 'Pesquisar', self.acaoGastoTotal, 'gastoTotal')
        mostrarDadosLabel.grid(column=0, row=0, sticky='nw', padx=10, pady=10)
        gastoTotalButton.grid(column=1, row=1, sticky='nw', pady=10)

        self.frameFuncao.grid(row=1, column=1, ipadx=241, ipady=133, sticky='nw')

    def administrador(self):
        self.frameFuncao.destroy()
        self.frameFuncao = tb.Labelframe(self.frameJanela)
        self.frameFuncao.config(text='Administrador')

        senhaLabel = tb.Label(self.frameFuncao, text='Senha:    ', font=self.fonte)
        senhaEntry = tb.Entry(self.frameFuncao, font=self.fonte, show='*')
        senha = (senhaEntry, self.frameFuncao)
        senhaButton = self.criarBotao(self.frameFuncao, 'Entrar', self.acaoAdministrador, senha)
        self.saidaTexto(texto='', janela=self.frameFuncao, height=1, width=12, column=3, row=1, sticky='e')

        senhaLabel.grid(column=0, row=0, sticky='nw', padx=10, pady=10)
        senhaEntry.grid(column=1, row=0, sticky='nw', padx=0, pady=3)
        senhaButton.grid(column=1, row=1, sticky='nw', pady=10)

        self.frameFuncao.grid(row=1, column=1, ipadx=152, ipady=133, sticky='nw')

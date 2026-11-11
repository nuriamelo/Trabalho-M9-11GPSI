class Livro:
    def __init__(self, titulo, autor, codigo):
        self.titulo = titulo
        self.autor = autor
        self.codigo = codigo
        self.disponivel = True 

    def mostrar_dados(self):
        if self.disponivel:
            estado = "disponível"
        else:
            estado = "emprestado"
        return f"Código: {self.codigo}, Título: {self.titulo}, Autor: {self.autor}, Disponibilidade: {estado}"


class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.livros_emprestados = []  

    def mostrar_dados(self):
        return f"Matrícula: {self.matricula}, Nome: {self.nome}, Livros emprestados: {len(self.livros_emprestados)}" #O len é tamanho ou quantos itens tem na lista


class Biblioteca:
    def __init__(self):
        self.catalogo_livros = []  
        self.cadastro_alunos = []  


    def registar_livro(self):
        titulo = input("Título do livro: ").strip()
        autor = input("Autor: ").strip()
        if titulo == "" or autor == "":
            print("Título e autor não podem estar vazios.")
            return
        codigo = len(self.catalogo_livros) + 1
        novo_livro = Livro(titulo, autor, codigo)
        self.catalogo_livros.append(novo_livro)
        print(f"Livro registado com o código {codigo}.")

    def registar_aluno(self):
        nome = input("Nome do aluno: ").strip()
        if nome == "":
            print("O nome não pode estar vazio.")
            return
        matricula = len(self.cadastro_alunos) + 1
        novo_aluno = Aluno(nome, matricula)
        self.cadastro_alunos.append(novo_aluno)
        print(f"Aluno registado com a matrícula {matricula}.")


    def procurar_livro(self, codigo):
        for livro in self.catalogo_livros:
            if livro.codigo == codigo:
                return livro
        return None

    def procurar_aluno(self, matricula):
        for aluno in self.cadastro_alunos:
            if aluno.matricula == matricula:
                return aluno
        return None

    def consultar_livros_disponiveis(self):
        encontrou = False
        for livro in self.catalogo_livros:
            if livro.disponivel:
                print(livro.mostrar_dados())
                encontrou = True
        if not encontrou:
            print("Não há livros disponíveis.")


    def emprestar_livro(self):
        if not self.catalogo_livros:
            print("Não há livros registados.")
            return
        if not self.cadastro_alunos:
            print("Não há alunos registados.")
            return

        print("Livros disponíveis:")
        self.consultar_livros_disponiveis()

        try:
            matricula = int(input("Matrícula do aluno: "))
            codigo = int(input("Código do livro: "))
        except ValueError:
            print("Erro! Escreva só números.")
            return

        aluno = self.procurar_aluno(matricula)
        livro = self.procurar_livro(codigo)

        if aluno is None:
            print("Aluno não encontrado.")
        elif livro is None:
            print("Livro não encontrado.")
        elif not livro.disponivel:
            print("Esse livro já está emprestado.")
        else:
            livro.disponivel = False
            aluno.livros_emprestados.append(livro)
            print(f"O livro '{livro.titulo}' foi emprestado a {aluno.nome}.")

    def devolver_livro(self):
        try:
            matricula = int(input("Matrícula do aluno: "))
        except ValueError:
            print("Erro! Escreva só números.")
            return

        aluno = self.procurar_aluno(matricula)
        if aluno is None:
            print("Aluno não encontrado.")
            return
        if not aluno.livros_emprestados:
            print("Este aluno não tem livros emprestados.")
            return

        print("Livros emprestados a este aluno:")
        for livro in aluno.livros_emprestados:
            print(livro.mostrar_dados())

        try:
            codigo = int(input("Código do livro a devolver: "))
        except ValueError:
            print("Erro! Escreva só números.")
            return

        for livro in aluno.livros_emprestados:
            if livro.codigo == codigo:
                livro.disponivel = True
                aluno.livros_emprestados.remove(livro)
                print(f"O livro '{livro.titulo}' foi devolvido.")
                return
        print("Esse livro não está emprestado a este aluno.")

    def mostrar_livros_do_aluno(self):
        try:
            matricula = int(input("Matrícula do aluno: "))
        except ValueError:
            print("Erro! Escreva só números.")
            return

        aluno = self.procurar_aluno(matricula)
        if aluno is None:
            print("Aluno não encontrado.")
        elif not aluno.livros_emprestados:
            print(f"{aluno.nome} não tem livros emprestados.")
        else:
            print(f"Livros emprestados a {aluno.nome}:")
            for livro in aluno.livros_emprestados:
                print(livro.mostrar_dados())

    def estado_livro(self):
        total = len(self.catalogo_livros)
        emprestados = 0
        for livro in self.catalogo_livros:
            if not livro.disponivel:
                emprestados += 1
        print("estado de livro")
        print(f"Total de livros: {total}")
        print(f"Livros emprestados: {emprestados}")
        print(f"Livros disponíveis: {total - emprestados}")

biblioteca = Biblioteca()

while True:
    print("   Menu   ")
    print("1 - Registar aluno")
    print("2 - Registar livro")
    print("3 - Consultar livros disponíveis")
    print("4 - Emprestar livro")
    print("5 - Devolver livro")
    print("6 - Livros emprestados por um aluno")
    print("7 - Sair")

    try:
        opc = int(input("Escolha uma opção: "))
    except ValueError:
        print("Erro! Escreva só números.")
        continue

    if opc == 1:
        biblioteca.registar_aluno()
    elif opc == 2:
        biblioteca.registar_livro()
    elif opc == 3:
        biblioteca.consultar_livros_disponiveis()
    elif opc == 4:
        biblioteca.emprestar_livro()
    elif opc == 5:
        biblioteca.devolver_livro()
    elif opc == 6:
        biblioteca.mostrar_livros_do_aluno()
    elif opc == 7:
        biblioteca.estado_livro()
        print("Encerrou o programa.")
        break
    else:
        print("Opção inválida, escolha um número de 1 a 7.")
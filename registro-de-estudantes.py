import sys

def adicionarAluno():
    nome = input("Digite o nome do estudante: ")
    id  = int(input("Digite o ID do aluno: "))
    notas = input("Digite as notas do aluno(separadas por espaço): ").split()

    notas = [eval(i) for i in notas]
    print(notas)
        
    print(f"{nome} adicionado a lista de Aluno!")    
    
    return estudantes.append({"id": id, "nome": nome, "notas": notas})

def exibirAlunos():
    for estudante in estudantes:
        print(f"{estudante}")

def procurarAlunoPeloId(id):

    for estudante in estudantes:
        if estudante['id'] == id:
            print(f"Encontrado: {estudante}")
            return  
        
        
    print(f"Aluno com o ID: {id}, não encontrado!")

def calcularMediaGeral():
    quantidadeDeNotas = 0
    somaDasNotas = 0
    for estudante in estudantes:
        print(estudante)
        somaDasNotas += sum(estudante['notas'])
        quantidadeDeNotas += len(estudante['notas'])

    media = somaDasNotas/quantidadeDeNotas

    print(f"A média das notas dos estudantes foi: {media}")

def salvarRegistrosEmTxt():
    with open('alunos.txt', 'w') as arquivo_de_alunos:
        for estudante in estudantes:            
            arquivo_de_alunos.write(f"{estudante['id']}, {estudante['nome']}, {estudante['notas']}\n")

def carregarRegistroTxt():
    listaDeRetorno = []
    with open('alunos.txt')as arquivo_de_alunos:
        for line in arquivo_de_alunos:
            aluno = line.split(sep=',')
            for i in range(0, len(aluno)):

                aluno[i] = aluno[i].strip().replace("[", "").replace("]", "")                
            listaDeRetorno.append(aluno)
    #print(listaDeRetorno)

    for lista in listaDeRetorno:
        registroDeAluno = {"id": 0, "nome": "", "notas": []}
        for i in range(0, len(lista)):
            if i == 0:
                registroDeAluno["id"] = int(lista[0])
            elif i == 1:
                registroDeAluno["nome"] = lista[1]
            elif i > 1:
                registroDeAluno['notas'].append(int(lista[i]))
        estudantes.append(registroDeAluno)
    print("Carregamento Realizado com sucesso!")

estudantes = []
while(True):
    print("-\n| Sistema de Gerenciamento de Registro de Estudantes |\n-\n" +
          "1. Adicionar Registro de Estudante\n"+
          "2. Exibir Registro de Estudantes\n" +
          "3. Procurar por um Estudante\n" +
          "4. Calcular Média das Notas\n" +
          "5. Salvar Registros em Arquivo\n" +
          "6. Carregar Registros de Arquivo\n" +
          "7. Sair\n---\n")
    
    opcao = input("Digite sua escolha (1-7): ")

    match opcao:
        case "1":            
            adicionarAluno()
        case "2":
            exibirAlunos()
        case "3":
            procurarAlunoPeloId(int(input("Digite o ID do aluno que deseja pesquisar: ")))
        case "4":            
            calcularMediaGeral()
        case "5":
            salvarRegistrosEmTxt()
        case "6":
            carregarRegistroTxt()
        case "7":
            sys.exit()
        case _:
            print(f"Opção {opcao} inválida, tenta novamente!")
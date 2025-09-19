#Lucas Lima Silva Nº16 / Geovana Kaori Nº7 / Kaua de Souza Nº13
# Sistema de Cadastro e Busca de Alunos

def cadastrar_aluno(alunos):
    nome = input("Digite o nome do aluno: ").strip()
    idade = input("Digite a idade do aluno: ").strip()
    curso = input("Digite o curso do aluno: ").strip()

    aluno = {
        "nome": nome,
        "idade": idade,
        "curso": curso
    }
    alunos.append(aluno)
    print(f"\n✅ Aluno '{nome}' cadastrado com sucesso!\n")


def listar_alunos(alunos):
    if not alunos:
        print("\n⚠️ Nenhum aluno cadastrado.\n")
    else:
        print("\n--- Lista de Alunos ---")
        for i, aluno in enumerate(alunos, start=1):
            print(f"{i}. Nome: {aluno['nome']} | Idade: {aluno['idade']} | Curso: {aluno['curso']}")
        print()


def pesquisar_aluno(alunos):
    busca = input("Digite o nome do aluno que deseja pesquisar: ").strip().lower()
    encontrados = [a for a in alunos if a['nome'].lower() == busca]

    if encontrados:
        print("\n🎯 Aluno(s) encontrado(s):")
        for aluno in encontrados:
            print(f"Nome: {aluno['nome']} | Idade: {aluno['idade']} | Curso: {aluno['curso']}")
        print()
    else:
        print("\n❌ Aluno não encontrado.\n")


def menu():
    alunos = []
    while True:
        print("=== Sistema de Cadastro de Alunos ===")
        print("1 - Cadastrar aluno")
        print("2 - Listar todos os alunos")
        print("3 - Pesquisar aluno por nome")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_aluno(alunos)
        elif opcao == "2":
            listar_alunos(alunos)
        elif opcao == "3":
            pesquisar_aluno(alunos)
        elif opcao == "4":
            print("\nPrograma encerrado. Até mais!")
            break
        else:
            print("\nOpção inválida! Tente novamente.\n")



if __name__ == "__main__":
    menu()

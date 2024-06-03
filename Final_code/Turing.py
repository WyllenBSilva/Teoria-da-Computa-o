def contabiliza_estados(arquivo):
    estados = set()
    with open(arquivo, 'r') as f:
        for linha in f:
            linha = linha.strip()
            if linha and not linha.startswith(';'):
                partes = linha.split()
                if len(partes) >= 5:
                    estados.add(partes[0])  # Adiciona o estado atual
                    estados.add(partes[4])  # Adiciona o novo estado
    return estados


def Simula_MTD_em_Sipser(arquivo):

    arquivo_saida = open("saida.out",'w')

    Cria_condicao_inicial = [
    "q0 1 % R q1",
    "q0 0 & R q1",
    "q1 * * R q1",
    "q1 _ _ R q2",
    "q2 _ $ L q3",
    "q3 _ _ L q3",
    "q3 1 _ R q4",
    "q4 _ 1 L q3",
    "q3 0 _ R q5",
    "q5 _ 0 L q3",

    "q3 % # R q6",
    "q3 & # R q7",

    "q6 _ 1 L q8",
    "q7 _ 0 L q8",

    "q8 # * R 0"
    ]

    for linha in Cria_condicao_inicial:
        #print(linha)
        arquivo_saida.write(linha+"\n")
    
    
    maquina_original = "\n\n\n; Transicoes da maquina de Turing original\n"
    #print(maquina_original)
    arquivo_saida.write(maquina_original)

    arquivo_entrada = open(arquivo, 'r')
    for linha in arquivo_entrada:
        arquivo_saida.write(linha)
    

    Verifica_Final = "\n\n\n;transicoes para leitura de $ no final da fita\n"
    arquivo_saida.write(Verifica_Final)

    Estados = contabiliza_estados(path)

    initial = 10

    transitions = []

    transitions.append(";transicoes para leitura de $ no final da fita\n")
    for estado in Estados:
        if(estado!="halt-accept"):
            transitions.append(f"{estado} $ _ R q{initial}\n")
            transitions.append(f"q{initial} _ $ L q{initial + 1}\n")
            transitions.append(f"q{initial + 1} _ * * {estado}\n")
            initial += 2
            transitions.append("\n")

    transitions.append("\n\n;transicoes para leitura de # no começo da fita\n")
    for estado in Estados:
        if(estado!="halt-accept"):
            transitions.append(f"{estado} # * R q{initial}\n")
            transitions.append(f"q{initial} * * R q{initial}\n")
            transitions.append(f"q{initial} $ _ R q{initial + 1}\n")
            transitions.append(f"q{initial + 1} _ $ L q{initial + 2}\n")
            transitions.append(f"q{initial + 2} _ _ L q{initial + 2}\n")
            transitions.append(f"q{initial + 2} 1 _ R q{initial + 3}\n")
            transitions.append(f"q{initial + 3} _ 1 L q{initial + 2}\n")
            transitions.append(f"q{initial + 2} 0 _ R q{initial + 4}\n")
            transitions.append(f"q{initial + 4} _ 0 L q{initial + 2}\n")
            transitions.append(f"q{initial + 2} # * R {estado}\n")
            initial += 5
            transitions.append("\n")

    for transition in transitions:
        #print(transition)
        arquivo_saida.write(transition)


def imprimir_conteudo_arquivo(arquivo):
    with open(arquivo, 'r') as f:
        for linha in f:
            content = linha, end=''
            return content

#Funções para Simular uma MT de sipser em uma MT Duplamente infinita:
def Simula_Sipser_em_MTD(arquivo):

    arquivo_saida = open("saida.out",'w')

    cria_condição_inicial_SIPSER_EM_MTD = ";USE STANDARD e q0 como simbolo inicial.\n;Insercao inicial do simbolo \'#\' no inicio da fita se ainda nao estiver presente\nq0 * * L q1\nq1 * # R 0"

    arquivo_saida.write(cria_condição_inicial_SIPSER_EM_MTD)

    maquina_original = "\n\n; Transicoes da maquina de Turing original\n"
    arquivo_saida.write(maquina_original)

    arquivo_entrada = open(arquivo, 'r')
    for linha in arquivo_entrada:
        arquivo_saida.write(linha)

    Estados = contabiliza_estados(path)
    #print("Estados da máquina: ")

    movimento_estacionario = "\n; Transicoes para gerenciar a leitura de \'#\'"
    arquivo_saida.write(movimento_estacionario)
    for estado in Estados:

        #if(estado != "halt-accept"):
        movimento_estacionario = "\n" + estado + " # * R " + estado
        #print(movimento_estacionario)
        arquivo_saida.write(str(movimento_estacionario))





if __name__ == "__main__":

    path_MT_Siper = "Casos_de_teste\\odd.in" 
    path_MT_Duplamente_Infinita = "Casos_de_teste\\sameamount10.in" 

    path = path_MT_Siper
    
    
    #Ler arquivo e verificar qual é o conteúdo da primeira linha, se é ;S ou ;I
    with open(path, 'r') as f:
        primeira_linha = f.readline().strip()

    if primeira_linha == ";S":
        print("\nO arquivo lido é uma MT de Sipser\n")
        print("**** Realizando conversão para simular essa MT Sipser em uma MT Duplamente Infinita *******")
        Simula_Sipser_em_MTD(path)
        print("\nSUCESSO! VERIFIQUE O ARQUIVO: \"saida.out\"\n")
        print("No simulador Use STANDARD e q0 como símbolo inicial")
    elif primeira_linha == ";I":
        print("\nO arquivo lido é uma MT Duplamente Infinita\n")
        print("**** Realizando conversão para simular essa MT Duplamente Infinita em uma MT Sipser *******")
        Simula_MTD_em_Sipser(path)
        print("\nSUCESSO! VERIFIQUE O ARQUIVO: \"saida.out\"\n")
        print("No simulador Use Semi-Infinite Tape e q0 como simbolo inicial")
    else:
        print("A primeira linha não é ';I' nem ';S'")

    
    









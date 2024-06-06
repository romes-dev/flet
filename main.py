import csv 

def ler_dados_csv(nome_arquivo):
    alunos = []
    with open(nome_arquivo, mode='r') as arquivo:
        leitor_csv = csv.DictReader(arquivo) 
        #print(f"Arquivo: {nome_arquivo} aberto com sucesso!")
        for linha in leitor_csv:
            alunos.append(linha)
            #print(f"{linha} foi adicionado ao sistema!")
    return alunos

def calcular_media_notas(alunos):
    total_notas = 0
    for aluno in alunos:
        total_notas += float(aluno['nota'])
    media_notas = total_notas / len(alunos)
    return media_notas

def escrever_dados_csv(nome_arquivo, alunos, media_notas):
    try:
        with open(nome_arquivo, mode='w', newline='') as arquivo:
            campos = ['id', 'nome', 'idade', 'nota']
            escritor_csv = csv.DictWriter(arquivo, fieldnames=campos)
            
            escritor_csv.writeheader()
            for aluno in alunos:
                escritor_csv.writerow(aluno)
            
            escritor_csv.writerow({'id': '','nome': 'Média', 'idade': '', 'nota':f"{media_notas}"})
    
    except Exception as e:
        print("O sistema não conseguiu realizar a ação de escrever. Erro! Contate o administrador do sistema")        
        
    
     
alunos = ler_dados_csv("students.csv")

media_notas = calcular_media_notas(alunos)
print(f"A média das notas é: {media_notas:.2f}")

escrever_dados_csv("novo_5.csv", alunos, media_notas)
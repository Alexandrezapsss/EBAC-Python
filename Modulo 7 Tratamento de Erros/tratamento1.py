#nessa aula vamos aprender:
#identificar tipos de erros
#tratar erros de sintaxe
#tratar erros com tempo de execução

#erro de sintaxe
pessoa = {"nome" : "Alexandre", "idade" : 30}

if pessoa["idade"] > 18 #aqui está faltando dois pontos ":" porem o python não fala exatamente o que falta
    print(True)

#Erro de tempo de execução: Erros de uso incorreto de Dados e Erros de Lógica

#erro de divisão de 0 porem nesse caso o python já fala qual é o erro

divisao_zero = 2 / 0
print(divisao_zero) # aqui temos que tratar o erro usando try e cath

#Erros de Lógicas são os piores Ex Loop Infinito
i = 0

while True:
    #bloco de código
    i += 1
    print(i)#aqui vai imprimir infinitamento o i pois sempre o laço está em true e não tem um break ou condição que saia deste laço

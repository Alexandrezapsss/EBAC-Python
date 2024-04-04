#Aqui vou ver um tipo de erro que geralmente é associado ao tempo de execução
pessoa = {"nome" : "Alexandre", "idade" : 30}
nome = pessoa["nome"];
idade = pessoa["idade"]

#print('Meu nome é: '+nome+' e tenho: '+idade+' anos')#aqui vai dar erro de execução e o python vai falar o motivo deste erro

#para enteder o erro acima temos que ver o que está aocntecendo que estamos concatenando uma cadeia de strings com uma INT a variavel idade
#para acertar isso é entender o erro pelo terminal e saber que o Python é fortemente tipado e converter o valor para string para concatenar
idade_str = str(idade)#zqui estamos convertendo a variavel para uma string

print('Meu nome é: '+nome+' e tenho: '+idade_str+' anos')

#claro que dependendo do caso não precisamos converter podemos usar recusos do python para exibir a mensagem

print(f'Meu nome é: {nome} e tenho: {idade} anos.')
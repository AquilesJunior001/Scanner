import json
palavras_reservadas = ['while', 'do']
operadores = ['<', '=', '+']
terminador = ';'
identificadores = ['i','j']
numeros = ['0','1','2','3','4','5','6','7','8','9']

arq = open('codigo.txt', 'r')
arquivo = arq.read().split(' ')
arq.close()

tokens = []
simbolos = []
erro = None
cont = 0
x = 0
while x<len(arquivo) and erro == None:
    if arquivo[x] in palavras_reservadas:
        aux = {'token':arquivo[x],'identificação':'palavra reservada','tamanho':str(len(arquivo[x])),'posição(lin,col)':'(0,'+str(cont)+')'}
        tokens.append(aux)
    elif arquivo[x] in operadores:
        aux = {'token':arquivo[x],'identificação':'operador','tamanho':str(len(arquivo[x])),'posição(lin,col)':'(0,'+str(cont)+')'}
        tokens.append(aux)
    elif arquivo[x] in identificadores:
        if arquivo[x] in simbolos:
            aux = {'token':arquivo[x],'identificação':'[identificador,'+str(simbolos.index(arquivo[x])+1)+']','tamanho':str(len(arquivo[x])),'posição(lin,col)':'(0,'+str(cont)+')'}
            tokens.append(aux)
        else:
            simbolos.append(arquivo[x])
            aux = {'token':arquivo[x],'identificação':'[identificador,'+str(len(simbolos))+']','tamanho':str(len(arquivo[x])),'posição(lin,col)':'(0,'+str(cont)+')'}
            tokens.append(aux)
    elif arquivo[x][-1] == ';':
        j = arquivo[x].split(';')
        if j[0] in palavras_reservadas:
            aux = {'token':j[0],'identificação':'palavra reservada','tamanho':str(len(j[0])),'posição(lin,col)':'(0,'+str(cont)+')'}
            tokens.append(aux)
        elif j[0] in operadores:
            aux = {'token':j[0],'identificação':'operador','tamanho':str(len(j[0])),'posição(lin,col)':'(0,'+str(cont)+')'}
            tokens.append(aux)
        elif j[0] in identificadores:
            if j[0] in simbolos:
                aux = {'token':j[0],'identificação':'[identificador,'+str(simbolos.index(j[0])+1)+']','tamanho':str(len(j[0])),'posição(lin,col)':'(0,'+str(cont)+')'}
                tokens.append(aux)
            else:
                simbolos.append(j[0])
                aux = {'token':j[0],'identificação':'[identificador,'+str(len(simbolos))+']','tamanho':str(len(j[0])),'posição(lin,col)':'(0,'+str(cont)+')'}
                tokens.append(aux)
        elif j[0][0] in numeros:
            if j[0] in simbolos:
                aux = {'token':j[0],'identificação':'[numero,'+str(simbolos.index(j[0])+1)+']','tamanho':str(len(j[0])),'posição(lin,col)':'(0,'+str(cont)+')'}
                tokens.append(aux)
            else:
                simbolos.append(j[0])
                aux = {'token':j[0],'identificação':'[numero,'+str(len(simbolos))+']','tamanho':str(len(j[0])),'posição(lin,col)':'(0,'+str(cont)+')'}
                tokens.append(aux)
        else:
            erro = 'Erro '+j[0]+' '+'(0,'+cont+')'
        if erro == None:
            aux = {'token':arquivo[x][-1],'identificação':'terminador','tamanho':str(len(arquivo[x][-1])),'posição(lin,col)':'(0,'+str(cont+len(j[0]))+')'}
            tokens.append(aux)
    elif arquivo[x][0] in numeros:
        if arquivo[x] in simbolos:
            aux = {'token':arquivo[x],'identificação':'[numero,'+str(simbolos.index(arquivo[x])+1)+']','tamanho':str(len(arquivo[x])),'posição(lin,col)':'(0,'+str(cont)+')'}
            tokens.append(aux)
        else:
            simbolos.append(arquivo[x])
            aux = {'token':arquivo[x],'identificação':'[numero,'+str(len(simbolos))+']','tamanho':str(len(arquivo[x])),'posição(lin,col)':'(0,'+str(cont)+')'}
            tokens.append(aux)
    else:
        erro = 'Erro '+arquivo[x]+' '+'(0,'+str(cont)+')'
    cont+=len(arquivo[x])+1
    x+=1

i = 0
while i<len(simbolos):
    simbolos[i] = {'indice':str(i+1),'símbolo':simbolos[i]}
    i+=1
tabela = {}
if erro != None:
    tabela = {'Tokens':tokens,'Símbolos':simbolos,'Erro':erro}
else:
    tabela = {'Tokens':tokens,'Símbolos':simbolos}

with open("scanner.json", 'w', encoding="utf8") as f:
    json.dump(tabela, f, ensure_ascii=False)



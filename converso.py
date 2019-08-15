import json
arq = open('scanner.json', 'r', encoding="utf8")
conteudo = arq.read()
parsed_json = json.loads(conteudo)
arq.close()
arquivo = open('resul.csv', 'w')
arquivo.write('token_identificação_tamanho_posição(lin,col)\n')
for i in parsed_json['Tokens']:
    arquivo.write(i['token']+'_'+i['identificação']+'_'+i['tamanho']+'_'+i['posição(lin,col)']+'\n')
arquivo.write('\n')
arquivo.write('indice_símbolo\n')
for i in parsed_json['Símbolos']:
    arquivo.write(i['indice']+'_'+i['símbolo']+'\n')
if 'Erro' in parsed_json:
    arquivo.write('\n')
    arquivo.write(parsed_json['Erro'])
arquivo.close()


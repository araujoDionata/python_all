'''
Comentário de multiplas linhas
Movendo arquivos específicos
'''

import shutil
import os

caminho_origem = 'C:\\Users\\Dionata\\Desktop\\pasta_origem'
caminho_destino_fotos = 'C:\\Users\\Dionata\\Desktop\\pasta_destino_fotos'
caminho_destino_txt = 'C:\\Users\\Dionata\\Desktop\\pasta_destino_txt'

#caminho_destino_txt = 'C:\\Users\\Dionata\\Desktop\\pasta_destino_outros'

try:
    os.mkdir(caminho_destino_fotos)
except FileExistsError as e:
    print('Pasta {} já existe.'.format(caminho_destino_fotos))

try:
    os.mkdir(caminho_destino_txt)
except FileExistsError as e:
    print('Pasta {} já existe.'.format(caminho_destino_txt))


for pasta_raiz, diretorios_internos, arquivos in os.walk(caminho_origem):
    for arquivo in arquivos:
        
        caminho_antigo_arquivo = os.path.join(pasta_raiz, arquivo)
        caminho_novo_arquivo_fotos = os.path.join(caminho_destino_fotos, arquivo)
        caminho_novo_arquivo_txt = os.path.join(caminho_destino_txt, arquivo)
        #caminho_novo_arquivo_outros = os.path.join(caminho_destino_outros, arquivo)

        if '.txt' in arquivo:
            shutil.copy(caminho_antigo_arquivo, caminho_novo_arquivo_txt)
            print('Arquivo {} movido com sucesso!'.format(arquivo))
        elif '.jpg' in arquivo:
            shutil.copy(caminho_antigo_arquivo, caminho_novo_arquivo_fotos)
            print('Arquivo {} movido com sucesso!'.format(arquivo))
        else:
            print('Arquivo não atende aos critérios de seleção')
            #shutil.copy(caminho_antigo_arquivo, caminho_novo_arquivo_outros)
            #print('Arquivo {} movido com sucesso!'.format(arquivo))































#### criado por u46o Davi Bortolotti ####

#### ESTE SCRIPT GERA UMA PASTA NO PWD CHAMADA WELLS_EXPORT, ONDE SERÃO COLOCADOS 
#### OS DADOS DE SAIDA ####

import re # importa modulo para usar regular expressions
import os

# Abre uma janela para encontrar o arquivo
from Tkinter import Tk
from tkFileDialog import askopenfilename
petrelexport = askopenfilename() 

# criando pasta onde sera colocado o resultado do script
if not os.path.exists('wells_export'):
    os.makedirs('wells_export')
# limpa a pasta caso o script seja rodado novamente
else:
    fileList = os.listdir('wells_export')
    for f in fileList:
        os.remove('wells_export/'+ f)

# abre o arquivo de entrada
with open(petrelexport) as infile:
            
    for line in infile:
        #regular expression para capturar as informacoes relevantes do arquivo
        match = re.search('([\d.]+)\s([\d.]+)\s([\-\d.]+)\s([\d.]+)\s["]'
        '(.+?)["]\s([\d.]+)\s+([\d.]+)\s\d\s+["](.+?)["]', line)                 
        line = line.rstrip()
        
        if match > 0:
            wellfile = 'wells_export/' + match.group(5) + '.txt'
            with open(wellfile, 'a') as outfile: # cria e define o arquivo de saida	
                #### escreve no arquivo de saida
                # cabecario :)
                if os.path.getsize(wellfile) == 0:
                    outfile.write('#X\tY\tZ\tDip-azimuth\tDip\tType\n')
                    outfile.write('#Metres\tMetres\tMetres\tDegrees\tDegrees\n')
                # corpo
                else: 
                    outfile.write(match.group(1) + '\t' + 
                    match.group(2) + '\t' + match.group(4) +'\t' + match.group(6) +
                    '\t' + match.group(7) + '\t' + match.group(8) + '\n') 
			
print '***\nfeito!\n***'



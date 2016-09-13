# ---------------------------
# ESTE SCRIPT DEVE SER COLOCADO DENTRO DA PASTA FED DO CENARIO QUE SE DESEJA UNIR AS FRATURAS
# ---------------------------

import os # importa modulo para mexer em funcoes do sistema operacional
import re # importa modulo para usar regular expressions
import Tkinter, tkFileDialog # importa modulo para usar gui de busca de arquivos


### buscando o arquivo

Tkinter.Tk().withdraw()
path = tkFileDialog.askdirectory()

os.chdir(path)

print "*** caminho escolhido: " + path
f = []
d = []


# criando uma lista dos diretorios no diretorio escolhido
for (dirpath, dirnames, filenames) in os.walk('./'): 
    d.extend(dirnames)
    break

	
	

# criando pasta onde sera colocado o resultado do script
if not os.path.exists('gridsUnidos'):
    os.makedirs('gridsUnidos')

typenumber = None	

print "*** criada pasta 'gridsUnidos'! ***"	
	
# unindo os dados de fratura dos grids
with open('gridsUnidos/allgridfractures.txt', 'w') as outfile: # cria e define o arquivo de saida
    
    # cabecario :)
    outfile.write('#GRID\tX\tY\tZ\tDip-azimuth\tDip\tType\n')
    outfile.write('#\tMetres\tMetres\tMetres\tDegrees\tDegrees\n')
    print '*** cabecalho escrito!!'
    # corpo	
    for dname in d:
        if re.match('(Grid)', dname): # regular expression para garantir que so utilize pastas de grids
            for (dirpath, dirnames, filenames) in os.walk(dname+'./'): # itera pelos arquivos da pasta do grid
                f.extend(filenames)
                for fname in f:
                    with open(dname+'/'+fname) as infile:
                        for line in infile:
                            match = re.search('(Grid\d+)', dname) #regular expression para pegar o nome do grid
                            line = line.rstrip()
                            match2 = re.search('_(.+)_', fname) # regular expression para pegar o tipo da fratura
                            if match is not None and match2 is not None: # error check
                                if match2.group(1) == 'Tensional':
                                    typenumber = 0
                                elif match2.group(1) == 'Normal_1':
                                    typenumber = 1
                                elif match2.group(1) == 'Normal_2':
                                    typenumber = 2
                                elif match2.group(1) == 'Reverse_1':
                                    typenumber = 3
                                elif match2.group(1) == 'Reverse_2':
                                    typenumber = 4
                                elif match2.group(1) == 'Dextral':
                                    typenumber = 5
                                elif match2.group(1) == 'Sinistral':
                                    typenumber = 6    
                                outfile.write(match.group(1) + '\t' + line + '\t' + match2.group(1) + '\t' + str(typenumber) + '\n') # escreve no arquivo de saida
                            else:
                                continue
                f = [] # esvazia a lista de arquivos para preencher com outra pasta
        else:
            continue # pula as pastas com outros dados que nao interessam
        print dname + " feito!"
			
print '***\nprocesso finalizado!\n***'

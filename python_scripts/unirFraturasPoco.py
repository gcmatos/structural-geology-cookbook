# ---------------------------
# ESTE SCRIPT DEVE SER COLOCADO DENTRO DA PASTA FED DO CENARIO QUE SE DESEJA UNIR AS FRATURAS
# ---------------------------

import os # importa modulo para mexer em funcoes do sistema operacional
import re # importa modulo para usar regular expressions



f = []
d = []
# criando uma lista dos diretorios no mesmo path do script
for (dirpath, dirnames, filenames) in os.walk('./'): 
	d.extend(dirnames)
	break

	
	

# criando pasta onde sera colocado o resultado do script
if not os.path.exists('unidas'):
    os.makedirs('unidas')

typenumber = None	
	
	
# unindo os dados de fratura dos pocos
with open('unidas/allfractures.txt', 'w') as outfile: # cria e define o arquivo de saida

	# cabecario :)
	outfile.write('#WELL\t\t\t\tX\t\t\tY\t\t\tZ\t\tDip-azimuth\tDip\t\t\tType\n')
	outfile.write('#\t\t\t\t\tMetres\t\tMetres\t\tMetres\tDegrees\t\tDegrees\t\t\t\n')

	# corpo	
	for dname in d:
		if re.match('(\d-.+?)', dname): # regular expression para garantir que so utilize pastas de pocos
			for (dirpath, dirnames, filenames) in os.walk(dname+'./'): # itera pelos arquivos da pasta do poco
				f.extend(filenames)
				for fname in f:
					with open(dname+'/'+fname) as infile:
						for line in infile:
							match = re.search('(\d-.+)', dname) #regular expression para pegar o nome do poco
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
			
			
print '***\nfeito!\n***'

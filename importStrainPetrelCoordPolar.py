# -*- coding: utf-8 -*-
"""
Criado em 29/06/2016

@author: u46o - Davi Bortolotti Batista - davibortolotti@gmail.com

a partir dos scripts de transformacao de coordenada por Rick Allmendinger
em "Structural Geology Algorithms: Vectors and Tensors" e com a colaboracao de 
Thiago da Cruz Falcao.
"""
#==============================================================================
# SCRIPT PARA IMPORTAR PLANO E1 DO MODELO DO TRAPTESTER
# Pontos importantes: os dados de direcao dos planos E1 do TrapTester sao ex-
# portados no formato de Vetores (vector x, y, z). Estas informacoes ja sao
# os cossenos diretores dos vetores.
# Alem disso, a posicao e orientacao dos planos no TrapTester utiliza a notacao
# de polos e nao planos. Por isso, este script ja da conta de adicionar ou
# subtrair os angulos necessarios para a transformacao. 
#
# Obs: tendo como variaveis plg = plunge e trd = trend do plano.
#==============================================================================

import math
import os
import Tkinter, tkFileDialog # importa modulo para usar gui de busca de arquivos

#==============================================================================
#  criando pasta onde sera colocado o resultado do script
#==============================================================================

if not os.path.exists('results'):
    os.makedirs('results')

#==============================================================================
# Funcao ZeroTwoPi - certifica-se de que o valor se encontra entre zero e dois
# pi.
#==============================================================================

def ZeroTwoPi(a):
    b = a
    twopi = 2 * math.pi
    if b < 0:
        b = b + twopi
    elif b >= twopi:
        b = b - twopi
    return float(b)
    
#==============================================================================
# Funcao car_to_pol - coordenada cartesiana para polar
#==============================================================================

def car_to_pol(x, y, z):
    # cossenos diretores dos vetores: east, north e down
    ce, cn, cd = float(x), float(y), float(z)
    
    # o arco do cosseno ja da a orientacao do plano do mergulho, enquanto o 
    # arco do seno daria a orientacao do polo
    plg = math.acos(cd) 
    plg_graus = round(math.degrees(plg)) # radianos para graus

    # a seguir, o script checa qual e o quadrante em que se encontra o azimute
    # do polo e adiciona o valor necessario para regularizar a orientacao
    if cn == 0:
        if ce < 0:
            trd = 3/2*math.pi
        else:
            trd = math.pi/2
    else:
        trd = math.atan(ce/cn)
        if cn < 0:
            trd = trd + math.pi
    trd = ZeroTwoPi(trd) # checa se o valor encontra-se entre zero e dois pi
    trd_graus = round(math.degrees(trd)) # radianos para graus
    
    # transformando o azimute de polo para plano
    if trd_graus > 180:
        trd_graus = trd_graus - 180
    else:
        trd_graus = trd_graus + 180

    # o TrapTester contem um bug que permite que os planos de mergulho
    # ultrapassem 90 graus. Nesse caso, o script espelha este plano para
    # o quadrante inverso:
    if plg_graus > 90:
        plg_graus = 180 - plg_graus
        if trd_graus > 180:                    
            trd_graus = trd_graus - 180
        else:
            trd_graus = trd_graus + 180
        
        
         
    # fim da funcao e retorna o valor final em graus
    return str(plg_graus) + "\t" + str(trd_graus)


#==============================================================================
#  lendo os dados de E1 exportados do traptester e escrevendo o output
#==============================================================================

# pede a pasta onde se encontram os dados de E1 do grid
Tkinter.Tk().withdraw()
path = tkFileDialog.askdirectory()

os.chdir(path)

print "*** caminho escolhido: " + path

f = []
for (dirpath, dirnames, filenames) in os.walk('./'): # itera pelos arquivos da pasta do poco
    f.extend(filenames)

for filename in f: 
    if filename.startswith('Grid'):
        print filename
        with open('results/e1polares.txt', 'w') as outfile:        
            with open(filename) as infile:            
                for _ in xrange(5):
                    next(infile)
                for line in infile:
                    linelist = line.split()
                    x, y, z = linelist[3], linelist[4], linelist[5]
                
                    outfile.write(str(filename) + '\t' + linelist[0] + '\t' + linelist[1] + 
                    '\t' + linelist[2] + '\t' + car_to_pol(x, y, z) + '\n')
    else:
        continue
print 'done'
            

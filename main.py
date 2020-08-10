import os.path as os

path = 'ez_mmr'
file = path+'.csv'
#Creacion de archivo

if(os.exists(file)):
    file_csv = open(file,'a')
    file_csv.write('1.0,2000-01-12,2000.0\n')
    print('exitste')
else:
    file_csv = open(file,'w')
    file_csv.write('N,date,mmr\n')
    print('no exitste')
#Validacion del archivo
#csv.write(titulo)

#print(os.exists(file))

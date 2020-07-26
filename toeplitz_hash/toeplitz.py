import numpy as np


BitsSetTable256 = [0] * 256
  
def initialize(): 

    BitsSetTable256[0] = 0
    for i in range(256): 
        BitsSetTable256[i] = ((i & 1) + BitsSetTable256[i // 2])%2 
        
def countone(n):
    result=0
    for i in range(int(1024/8)):
        result = result+BitsSetTable256[n>>(8*i) & 0xff]
    return result%2
    

def matrix_gen(m,n):
    
    matrix=[None]*m
    for i in range(m):
        matrix[i]=[None]*n
    
    
    
    array_n=np.random.randint(0,2,n)
    array_m=np.random.randint(0,2,m-1)
    
    
    for i in range(n):
        x=0
        y=n-i-1
        matrix[x][y]=str(array_n[n-i-1])
        
        while(x<m-1 and y<n-1):
            x+=1
            y+=1
            matrix[x][y]=str(array_n[n-i-1])
            
    
    for i in range(1,m):
        x=i
        y=0
        matrix[x][y]=str(array_m[i-1])
        
        while(x<m-1 and y<n-1):
            x+=1
            y+=1
            matrix[x][y]=str(array_m[i-1])
    
    result_matrix = []
    for i in range(m):
        result_matrix.append(int(''.join(matrix[i]),2))
    
    return result_matrix
    
    
file=f'../test_files/{fl}.bin'
output_file=f'result_files/{fl}.bin'


initialize()
m=1024
n=768
seed = matrix_gen(n,m)

with open(f'{file}','rb') as fr, open(f'{output_file}','wb') as fw:
    data = fr.read(128)
    while(data):
        result = ''
        number = int.from_bytes(data, 'big')
        for i in range(n):
            result=result+str(countone(seed[i] & number))
        fw.write((int(result, 2)).to_bytes(96, 'big'))
        data=fr.read(128)


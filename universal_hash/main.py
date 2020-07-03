import numpy as np
import time

time_file='time.txt'
file_arr=['50m','100m','500m','1g']


def hash_fun(p, k, m):
    a = np.random.randint(1,p)
    b = np.random.randint(0,p)
    return ((a*k+b)%p)%m



p = 65537
m=4096

for fl in file_arr:
    start_time = time.time()
    file=f'../test_files/{fl}.bin'
    output_file=f'result_files/{fl}.bin'


    with open(f'{file}','rb') as fr, open(f'{output_file}','wb') as fw:
        data=fr.read(2)
        while(data):
            integer = int.from_bytes(data, 'big')
            result1 = hash_fun(p, integer, m)
            data=fr.read(2)
            integer = int.from_bytes(data, 'big')
            result2 = hash_fun(p, integer, m)
            result1=result1<<12
            result=result1+result2
            fw.write(result.to_bytes(3, 'big'))
            data=fr.read(2)

    with open(f'{time_file}','a') as fw:
        fw.write(str((time.time())-start_time)+'\n\n')

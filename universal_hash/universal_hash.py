import numpy as np
import argparse


def hash_fun(p, k, m):
    a = np.random.randint(1,p)
    b = np.random.randint(0,p)
    return ((a*k+b)%p)%m



p = 65537
m=4096

parser = argparse.ArgumentParser()

parser.add_argument("-i", "--input", dest = "input", help="input binary file", type=str, required=True)
parser.add_argument("-o", "--output", dest = "output", help="output binary file", default = "output.bin", type=str)
    
args = parser.parse_args()


with open(f'{args.input}','rb') as fr, open(f'{args.output}','wb') as fw:
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


import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-i", "--input", dest = "input", help="input binary file", type=str, required=True)
parser.add_argument("-o", "--output", dest = "output", help="output binary file", default = "output.bin", type=str)
    
args = parser.parse_args()
    

with open(f'{args.input}','rb') as fr, open(f'{args.output}','wb') as fw:
    read_data = fr.read(1)
    output_data=''
    while(read_data):
        byte_string = "{0:08b}".format(read_data[0])
        while(len(byte_string)>1):
            temp_output='' if (byte_string[0]==byte_string[1]) else byte_string[0]
            byte_string = byte_string[2:]
            output_data+=temp_output
        if(len(output_data)>=8):
            fw.write(bytes([int(output_data[:8],2)]))
            output_data=output_data[8:] 
        read_data=fr.read(1)

import time

time_file='time.txt'
file_arr=['50m','100m','500m','1g']
for fl in file_arr:
    start_time = time.time()
    file=f'../test_files/{fl}.bin'
    output_file=f'result_files/{fl}.bin'


    with open(f'{file}','rb') as fr, open(f'{output_file}','wb') as fw:
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

    with open(f'{time_file}','a') as fw:
        fw.write(str((time.time())-start_time)+'\n\n')
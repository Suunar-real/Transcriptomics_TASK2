dir_path = './ProtSeq/'
file_name = 'seq_'

seq_list = []
for i in range(1,5):
    with open(dir_path + file_name + str(i) + '.fasta') as file:
        con = file.read() 
        seq_list.append(con)

sequences = []

for str in seq_list:
    li = []
    lines = str.split(sep = '\n')
    for line in lines:
        if line.startswith(">") or line == "":
            continue
        else:
            li.append(line)
    sequences.append(li)

res_seq = []

for seq in sequences:
    seq = ''.join(seq)
    res_seq.append(seq)

obj = [[543, 'G'], [568, 'L'], [24, 'D'], [240, 'G']]

for seq in res_seq:
    obj_i = obj[res_seq.index(seq)]
    idx, replacement = obj_i[0], obj_i[1]
    res = seq[:idx] + replacement + seq[idx+1:]
    print(res)
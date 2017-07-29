#generates a dictionary of genes in the genome
import re
genes = open('genes.txt', 'r')
gene_list = genes.readlines()
annotations = []
for line in gene_list:
    if line[0] == '>':
        annotations.append(line)

gene_dict = {}
for i in range(len(annotations)):
    match = re.search(r'(gene=)(\w+).+(location=)([a-z(]*)(\d+)(..)(\d+)', annotations[i])
    if match != None:
        forward = match.group(4)
        if (forward == '' or forward == 'complement('):
            name = match.group(2)
            start = match.group(5)
            end = match.group(7)
            if forward == '':
                forward = True
            elif forward == 'complement(':
                forward = False
            gene_dict[name] = [int(start), int(end), forward]

# generates the whole genome as a string
seq = open('sequence.txt', 'r')
seq_list = seq.readlines()
seq_string = ''
for i in range(1, len(seq_list) - 1):
    seq_string += seq_list[i][:-1]
seq_string += seq_list[i]

#names where the genes are in the
#genome and in what direction
index_list = [0] * len(seq_string)
for key in gene_dict.keys():
    start = gene_dict[key][0]
    end = gene_dict[key][1]
    if gene_dict[key][2]:
        index_list[start:end] = [1] * (end - start)
    else:
        index_list[start:end] = [-1] * (end - start)

#checks whether consensus sequences are present on the complement strand
consensus = 'TATA'
back_consensus = 'ATAT'
len_con = len(consensus)
forwards = [1] * len_con
backs = [-1] * len_con
new_forwards = [2] * len_con
new_backs = [-2] * len_con
for i in range(len(seq_string) - len_con):
    if index_list[i:i+len_con] == forwards and seq_string[i:i+len_con] == back_consensus:
        index_list[i:i+len_con] = new_forwards
    elif index_list[i:i+len_con] == backs and seq_string[i:i+len_con] == consensus:
        index_list[i:i+len_con] = new_backs

#adds the location of the reverse tata relative to the gene location
ratio_list = []
start_index = 1
stop_index = 0
tata_index = 0
while start_index < len(index_list):
    if index_list[start_index-1] == 0 and index_list[start_index] == 1:
        for j in range(start_index, len(seq_string)):
            if index_list[j-1] == 1 and index_list[j] == 0:
                stop_index = j
                length = stop_index - start_index
                tata_index = start_index
                break
        while tata_index < stop_index:
            if index_list[tata_index] == 2:
                ratio_list.append((tata_index-start_index)/float(length))
                tata_index += 4
            else:
                tata_index += 1
        start_index = stop_index
    else:
        start_index += 1
    print start_index

print ratio_list
print len(ratio_list)

















#some space

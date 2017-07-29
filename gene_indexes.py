genes = open('genes', 'r')
genes_list = genes.readlines()
annotations = []

for i in range(1000):
    if genes_list[i][0] == '>':
        annotations.append(genes_list[i][0])

print annotations

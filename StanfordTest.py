from Stanford_tree import parse_tree
from Stanford_tree import MultiTreePaths

tree = parse_tree("What is the national flower of Vicente_del_Bosque's place of birth",'en')

pathlist = MultiTreePaths(tree)
alllist= []
for i in range(10):
    subname = 'NP'+str(i+1)
    sublist = []
    for p in pathlist:
        p = p[:-1]
        p = p.split('->')
        if subname in p:
           sublist.append(p[-1])
        else:
           pass
    if sublist != []:
       para = ''
       for w in sublist:
           para += w+' '
       para = para.replace(' _','_')
       para = para.replace(" 's","'s")
       alllist.append(para) 

print(pathlist)
for line in alllist:
    print(line)

tree.draw()    

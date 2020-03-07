#coding=utf-8

# -*- coding: cp936 -*-
import os

def read_files(dirpath,lan1,lan2,lan1_list,lan2_list): 
    for root,dirs,files in os.walk(dirpath):
        for file in files:
            path = (os.path.join(root,file))
            if 'r2r' in path:
                print(path)
                if '_'+lan1+'_'+lan2+'_' in path and '3-hop' not in path:
                    with open(path,encoding='utf-8') as f:
                        for line in f:
                            line = line.replace('\n','')
                            line = line.split('\t')[1]
                            line = line.split('###')
                            t_lan1 = line[0].split('@@@')
                            t_lan2 = line[1].split('@@@')
                            
                            if t_lan1[0] not in lan1_list:
                                lan1_list.append(t_lan1[0])
                            if t_lan1[2] not in lan1_list:
                                lan1_list.append(t_lan1[2])
                                
                            if t_lan2[0] not in lan2_list:
                                lan2_list.append(t_lan2[0])
                            if t_lan2[2] not in lan2_list:
                                lan2_list.append(t_lan2[2])
                                
                elif '_'+lan2+'_'+lan1+'_' in path and '3-hop' not in path:
                    with open(path,encoding='utf-8') as f:
                        for line in f:
                            line = line.replace('\n','')
                            line = line.split('\t')[1]
                            line = line.split('###')
                            t_lan1 = line[0].split('@@@')
                            t_lan2 = line[1].split('@@@')
                            
                            if t_lan1[0] not in lan2_list:
                                lan2_list.append(t_lan1[0])
                            if t_lan1[2] not in lan2_list:
                                lan2_list.append(t_lan1[2])
                                
                            if t_lan2[0] not in lan1_list:
                                lan1_list.append(t_lan2[0])
                            if t_lan2[2] not in lan1_list:
                                lan1_list.append(t_lan2[2])
                                
                elif '_'+lan1+'_'+lan2+'_'+lan1+'_' in path:
                    with open(path,encoding='utf-8') as f:
                        for line in f:
                            line = line.replace('\n','')
                            line = line.split('\t')[1]
                            line = line.split('###')
                            t_lan1 = line[0].split('@@@')
                            t_lan2 = line[1].split('@@@')
                            t_lan3 = line[2].split('@@@')
                            
                            if t_lan1[0] not in lan1_list:
                                lan1_list.append(t_lan1[0])
                            if t_lan1[2] not in lan1_list:
                                lan1_list.append(t_lan1[2])
                                
                            if t_lan2[0] not in lan2_list:
                                lan2_list.append(t_lan2[0])
                            if t_lan2[2] not in lan2_list:
                                lan2_list.append(t_lan2[2])
                                
                            if t_lan3[0] not in lan1_list:
                                lan1_list.append(t_lan3[0])
                            if t_lan3[2] not in lan1_list:
                                lan1_list.append(t_lan3[2]) 
                                
                elif '_'+lan1+'_'+lan1+'_'+lan2+'_' in path:
                    with open(path,encoding='utf-8') as f:
                        for line in f:
                            line = line.replace('\n','')
                            line = line.split('\t')[1]
                            line = line.split('###')
                            t_lan1 = line[0].split('@@@')
                            t_lan2 = line[1].split('@@@')
                            t_lan3 = line[2].split('@@@')
                            
                            if t_lan1[0] not in lan1_list:
                                lan1_list.append(t_lan1[0])
                            if t_lan1[2] not in lan1_list:
                                lan1_list.append(t_lan1[2])
                                
                            if t_lan2[0] not in lan1_list:
                                lan1_list.append(t_lan2[0])
                            if t_lan2[2] not in lan1_list:
                                lan1_list.append(t_lan2[2])
                                
                            if t_lan3[0] not in lan2_list:
                                lan2_list.append(t_lan3[0])
                            if t_lan3[2] not in lan2_list:
                                lan2_list.append(t_lan3[2])  

                elif '_'+lan1+'_'+lan2+'_'+lan2+'_' in path:
                    with open(path,encoding='utf-8') as f:
                        for line in f:
                            line = line.replace('\n','')
                            line = line.split('\t')[1]
                            line = line.split('###')
                            t_lan1 = line[0].split('@@@')
                            t_lan2 = line[1].split('@@@')
                            t_lan3 = line[2].split('@@@')
                            
                            if t_lan1[0] not in lan1_list:
                                lan1_list.append(t_lan1[0])
                            if t_lan1[2] not in lan1_list:
                                lan1_list.append(t_lan1[2])
                                
                            if t_lan2[0] not in lan2_list:
                                lan2_list.append(t_lan2[0])
                            if t_lan2[2] not in lan2_list:
                                lan2_list.append(t_lan2[2])
                                
                            if t_lan3[0] not in lan2_list:
                                lan2_list.append(t_lan3[0])
                            if t_lan3[2] not in lan2_list:
                                lan2_list.append(t_lan3[2])      

                elif '_'+lan2+'_'+lan1+'_'+lan2+'_' in path:
                    with open(path,encoding='utf-8') as f:
                        for line in f:
                            line = line.replace('\n','')
                            line = line.split('\t')[1]
                            line = line.split('###')
                            t_lan1 = line[0].split('@@@')
                            t_lan2 = line[1].split('@@@')
                            t_lan3 = line[2].split('@@@')
                            
                            if t_lan1[0] not in lan2_list:
                                lan2_list.append(t_lan2[0])
                            if t_lan1[2] not in lan2_list:
                                lan2_list.append(t_lan2[2])
                                
                            if t_lan2[0] not in lan1_list:
                                lan1_list.append(t_lan1[0])
                            if t_lan2[2] not in lan1_list:
                                lan1_list.append(t_lan1[2])
                                
                            if t_lan3[0] not in lan2_list:
                                lan2_list.append(t_lan2[0])
                            if t_lan3[2] not in lan2_list:
                                lan2_list.append(t_lan2[2]) 
                                
                elif '_'+lan2+'_'+lan2+'_'+lan1+'_' in path:
                    with open(path,encoding='utf-8') as f:
                        for line in f:
                            line = line.replace('\n','')
                            line = line.split('\t')[1]
                            line = line.split('###')
                            t_lan1 = line[0].split('@@@')
                            t_lan2 = line[1].split('@@@')
                            t_lan3 = line[2].split('@@@')
                            
                            if t_lan1[0] not in lan2_list:
                                lan2_list.append(t_lan2[0])
                            if t_lan1[2] not in lan2_list:
                                lan2_list.append(t_lan2[2])
                                
                            if t_lan2[0] not in lan2_list:
                                lan2_list.append(t_lan1[0])
                            if t_lan2[2] not in lan2_list:
                                lan2_list.append(t_lan1[2])
                                
                            if t_lan3[0] not in lan1_list:
                                lan1_list.append(t_lan2[0])
                            if t_lan3[2] not in lan1_list:
                                lan1_list.append(t_lan2[2])  

                elif '_'+lan2+'_'+lan1+'_'+lan1+'_' in path:
                    with open(path,encoding='utf-8') as f:
                        for line in f:
                            line = line.replace('\n','')
                            line = line.split('\t')[1]
                            line = line.split('###')
                            t_lan1 = line[0].split('@@@')
                            t_lan2 = line[1].split('@@@')
                            t_lan3 = line[2].split('@@@')
                            
                            if t_lan1[0] not in lan2_list:
                                lan2_list.append(t_lan2[0])
                            if t_lan1[2] not in lan2_list:
                                lan2_list.append(t_lan2[2])
                                
                            if t_lan2[0] not in lan1_list:
                                lan1_list.append(t_lan1[0])
                            if t_lan2[2] not in lan1_list:
                                lan1_list.append(t_lan1[2])
                                
                            if t_lan3[0] not in lan1_list:
                                lan1_list.append(t_lan2[0])
                            if t_lan3[2] not in lan1_list:
                                lan1_list.append(t_lan2[2])      
    return lan1_list,lan2_list

def read_files_2(dirpath,lan1,lan2,lan1_list,lan2_list): 
    for root,dirs,files in os.walk(dirpath):
        for file in files:
            path = (os.path.join(root,file))
            if 'r2r' in path:
                print(path)
                if '_'+lan1+'_'+lan2+'_' in path and '3-hop' not in path:
                    with open(path,encoding='utf-8') as f:
                        for line in f:
                            line = line.replace('\n','')
                            line = line.split('\t')[1]
                            line = line.split('###')
                            t_lan1 = line[0]
                            t_lan2 = line[1]
                            if t_lan1 not in lan1_list:
                                lan1_list.append(t_lan1)
                            if t_lan2 not in lan2_list:
                                lan2_list.append(t_lan2)
                                
                elif '_'+lan2+'_'+lan1+'_' in path and '3-hop' not in path:
                    with open(path,encoding='utf-8') as f:
                        for line in f:
                            line = line.replace('\n','')
                            line = line.split('\t')[1]
                            line = line.split('###')
                            t_lan1 = line[0]
                            t_lan2 = line[1]
                            if t_lan1 not in lan2_list:
                                lan2_list.append(t_lan1)
                            if t_lan2 not in lan1_list:
                                lan1_list.append(t_lan2)
                                
                elif '_'+lan1+'_'+lan2+'_'+lan1+'_' in path:
                    with open(path,encoding='utf-8') as f:
                        for line in f:
                            line = line.replace('\n','')
                            line = line.split('\t')[1]
                            line = line.split('###')
                            t_lan1 = line[0]
                            t_lan2 = line[1]
                            t_lan3 = line[2]
                            if t_lan1 not in lan1_list:
                                lan1_list.append(t_lan1)
                            if t_lan2 not in lan2_list:
                                lan2_list.append(t_lan2)
                            if t_lan3 not in lan1_list:
                                lan1_list.append(t_lan3)
                                
                elif '_'+lan1+'_'+lan1+'_'+lan2+'_' in path:
                    with open(path,encoding='utf-8') as f:
                        for line in f:
                            line = line.replace('\n','')
                            line = line.split('\t')[1]
                            line = line.split('###')
                            t_lan1 = line[0]
                            t_lan2 = line[1]
                            t_lan3 = line[2]
                            if t_lan1 not in lan1_list:
                                lan1_list.append(t_lan1)
                            if t_lan2 not in lan1_list:
                                lan1_list.append(t_lan2)
                            if t_lan3 not in lan2_list:
                                lan2_list.append(t_lan3)

                elif '_'+lan1+'_'+lan2+'_'+lan2+'_' in path:
                    with open(path,encoding='utf-8') as f:
                        for line in f:
                            line = line.replace('\n','')
                            line = line.split('\t')[1]
                            line = line.split('###')
                            t_lan1 = line[0]
                            t_lan2 = line[1]
                            t_lan3 = line[2]
                            if t_lan1 not in lan1_list:
                                lan1_list.append(t_lan1)
                            if t_lan2 not in lan2_list:
                                lan2_list.append(t_lan2)
                            if t_lan3 not in lan2_list:
                                lan2_list.append(t_lan3)

                elif '_'+lan2+'_'+lan1+'_'+lan2+'_' in path:
                    with open(path,encoding='utf-8') as f:
                        for line in f:
                            line = line.replace('\n','')
                            line = line.split('\t')[1]
                            line = line.split('###')
                            t_lan1 = line[0]
                            t_lan2 = line[1]
                            t_lan3 = line[2]
                            if t_lan1 not in lan2_list:
                                lan2_list.append(t_lan2)
                            if t_lan2 not in lan1_list:
                                lan1_list.append(t_lan1)
                            if t_lan3 not in lan2_list:
                                lan2_list.append(t_lan2)
                                
                elif '_'+lan2+'_'+lan2+'_'+lan1+'_' in path:
                    with open(path,encoding='utf-8') as f:
                        for line in f:
                            line = line.replace('\n','')
                            line = line.split('\t')[1]
                            line = line.split('###')
                            t_lan1 = line[0]
                            t_lan2 = line[1]
                            t_lan3 = line[2]
                            if t_lan1 not in lan2_list:
                                lan2_list.append(t_lan2)
                            if t_lan2 not in lan2_list:
                                lan2_list.append(t_lan1)
                            if t_lan3 not in lan1_list:
                                lan1_list.append(t_lan2)

                elif '_'+lan2+'_'+lan1+'_'+lan1+'_' in path:
                    with open(path,encoding='utf-8') as f:
                        for line in f:
                            line = line.replace('\n','')
                            line = line.split('\t')[1]
                            line = line.split('###')
                            t_lan1 = line[0]
                            t_lan2 = line[1]
                            t_lan3 = line[2]
                            if t_lan1 not in lan2_list:
                                lan2_list.append(t_lan2)
                            if t_lan2 not in lan1_list:
                                lan1_list.append(t_lan1)
                            if t_lan3 not in lan1_list:
                                lan1_list.append(t_lan2)
    return lan1_list,lan2_list                                                            
                    
            #statistc(path)

en=[]
zh=[]
fr=[]
zh,fr = read_files_2('zh-fr','zh','fr',zh,fr)
en,zh = read_files_2('en-zh','en','zh',en,zh)
fr,en = read_files_2('fr-en','fr','en',fr,en)

print(len(en),len(zh),len(fr))

new = open('extracted_en_KG','w',encoding='utf-8')
for t in en:
    new.write(t+'\n',)
new.close()
new = open('extracted_zh_KG','w',encoding='utf-8')   
for t in zh:
    new.write(t+'\n',)
new.close()
new = open('extracted_fr_KG','w',encoding='utf-8')
for t in fr:
    new.write(t+'\n',)
new.close()


'''
new_en = open('KG_en_r2r_selected','w',encoding='utf-8')
f = open('onlyer_triple_KG_en_r2r',encoding='utf-8').readlines()
scale = len(f)
i = 0
with open('onlyer_triple_KG_en_r2r',encoding='utf-8') as f:
    for line in f:
        i+=1
        if i%5000 == 0:
            a = '*'*int(i/5000)
            b = '.'*int((scale-i)/5000)
            c = (i/scale)*100
            print("{:^3.0f}%[{}->{}]".format(c,a,b))   
        line = line.replace('\n','')
        l = line.split('@@@')
        if l[0] in en or l[2] in en:
            new_en.write(line,)
new_en.close()

new_zh = open('KG_zh_r2r_selected','w',encoding='utf-8')
f = open('onlyer_triple_KG_zh_r2r',encoding='utf-8').readlines()
scale = len(f)
i = 0
with open('onlyer_triple_KG_zh_r2r',encoding='utf-8') as f:
    for line in f:
        i+=1
        if i%5000 == 0:
            a = '*'*int(i/5000)
            b = '.'*int((scale-i)/5000)
            c = (i/scale)*100
            print("{:^3.0f}%[{}->{}]".format(c,a,b))  
        line = line.replace('\n','')
        l = line.split('@@@')
        if l[0] in zh or l[2] in zh:
            new_zh.write(line,)
new_zh.close()

new_fr = open('KG_fr_r2r_selected','w',encoding='utf-8')
f = open('onlyer_triple_KG_fr_r2r',encoding='utf-8').readlines()
scale = len(f)
i = 0
with open('onlyer_triple_KG_fr_r2r',encoding='utf-8') as f:
    for line in f:
        i+=1
        if i%5000 == 0:
            a = '*'*int(i/5000)
            b = '.'*int((scale-i)/5000)
            c = (i/scale)*100
            print("{:^3.0f}%[{}->{}]".format(c,a,b))  
        line = line.replace('\n','')
        l = line.split('@@@')
        if l[0] in fr or l[2] in fr:
            new_fr.write(line,)
new_fr.close()
'''            


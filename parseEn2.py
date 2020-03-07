from Stanford_tree import parse_tree
from Stanford_tree import MultiTreePaths
from buildList import *


def findPredict(question):
    entity=''
    ques=question.split(' ')
    for q in ques:
        if q[-2:]=='\'s':
            q=q[:-2]
        if q in enResourceDic:
            entity=q
    if entity=='':
        print('No entity! '+question)
    else:
        question=question.replace(entity,'entity')
    entityResource=entity
    entity='entity'
    tree = parse_tree(question, 'en')
    pathlist = MultiTreePaths(tree)
    result=[]
    prex=''
    entityPredict=[]
    for p in pathlist:
        path=p[:-1].split('->')
        if entity in path:
            i=path.index(entity)
            i-=1
            while True:
                i-=1
                if path[i][:2]!='NP':
                    break
            prex='->'.join(path[:i+2])
            #print(prex)
            for p in pathlist:
                if prex in p:
                    l=p.split('->')
                    if len(l[-1])==1:
                        continue
                    if l[-1][:-1]==entity or l[-1][-3:-1]=='\'s':
                        continue
                    entityPredict.append(l[-1][:-1])
    if len(entityPredict)>0:
        result.append(' '.join(entityPredict))
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
           para=' '.join(sublist)
           if entity in para:
               continue
           para = para.replace(' _','_')
           para = para.replace(" 's","'s")
           para=para.replace(' the ','')
           if para[:4]=='the ':
               para=para[4:]
           result.append(para)
    words=[]
    for line in result:
        words.append(''.join(line.split(' ')))
    result=list(set(result+words))
    result.append(entityResource)
    #print(result)
    #tree.draw()
    return result
#findPredict("What is the capital name of the nationality of Allan_Ramsay_(poet)")
questionList=[]
with open('./data/MLPQ/question/en-zh/3-hop/r2r_en_en_zh_question_en','r',encoding='utf-8')as f:
    for line in f:
        if line=='\t\n':
            continue
        q=line.split('\t')[0]
        if q[-1]=='?':
            q=q[:-1]
        #print(q)
        questionList.append(q)
with open('./phrase/aaaaaaa','a',encoding='utf-8')as file:
    n=0
    for i in range(0,734):
        phrase=findPredict(questionList[i])
        print(phrase)
        file.write(questionList[i]+'###'+'@@@'.join(phrase)+'\n')
        n+=1
        if n%100==0:
            print(n)

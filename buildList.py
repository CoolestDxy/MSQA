import re
rule = re.compile(r'\[(.*?)\]')
rule1=re.compile(r'\<(.*?)\>')
rule2=re.compile(r'\'(.*?)\'')
#find answer:

enKG=[]
zhKG=[]
frKG=[]
zhResourceDic={}
zhPropertyList=[]
enResourceDic={}
enPropertyList=[]
frResourceDic={}
frPropertyList=[]
ZhEnAlignment={}
ZhFrAlignment={}
EnFrAlignment={}

# with open('./data/extracted_fr_KG','r',encoding='utf8')as f:
#     for line in f:
#         tri=rule.findall(line)
#         res=[]
#         for i in tri:
#             resource=rule1.findall(i)
#             for ii in resource:
#                 res.append(ii.split('/')[-1])
#         if len(res)==2:
#             answer=line.split(',')[-1][3:-3]
#             res.append(answer)
#         frKG.append(res)

with open('./data/extracted_en_KG','r',encoding='utf8')as f:
    for line in f:
        t = line.split('@@@')
        t[2] = t[2][:-1]
        if len(t) == 3:
            tt = (t[0], t[1], t[2])
            enResourceDic[t[0]]=''
            enResourceDic[t[2]]=''
            enPropertyList.append(t[1])
            enKG.append(tt)
with open('./data/extracted_zh_KG','r',encoding='utf8')as f:
    for line in f:
        t = line.split('@@@')
        t[2] = t[2][:-1]
        if len(t) == 3:
            tt = (t[0], t[1], t[2])
            zhResourceDic[t[0]] = ''
            zhResourceDic[t[2]] = ''
            zhPropertyList.append(t[1])
            zhKG.append(tt)
# with open('./data/extracted_fr_KG','r',encoding='utf8')as f:
#     for line in f:
#         t = line.split('@@@')
#         t[2] = t[2][:-1]
#         if len(t) == 3:
#             tt = (t[0], t[1], t[2])
#             frResourceDic[t[0]] = ''
#             frResourceDic[t[2]] = ''
#             frPropertyList.append(t[1])
#             frKG.append(tt)

with open('./data/en_zh_alignment_extracted', 'r', encoding='UTF-8')as sameAs:
    for line in sameAs:
        pair=line.split('&&&')
        ZhEnAlignment[pair[0]]=pair[1][:-1]
        ZhEnAlignment[pair[1][:-1]] = pair[0]

# with open('./data/fr_zh_alignment_extracted', 'r', encoding='UTF-8')as sameAs:
#     for line in sameAs:
#         pair = line.split('&&&')
#         ZhFrAlignment[pair[0]]=pair[1][:-1]
#         ZhFrAlignment[pair[1][:-1]] = pair[0]
#
# with open('./data/fr_en_alignment_extracted', 'r', encoding='UTF-8')as sameAs:
#     for line in sameAs:
#         pair = line.split('&&&')
#         EnFrAlignment[pair[0]]=pair[1][:-1]
#         EnFrAlignment[pair[1][:-1]] = pair[0]
